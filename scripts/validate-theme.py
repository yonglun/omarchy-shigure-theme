#!/usr/bin/env python3
"""Check theme assets; optionally render against a local Omarchy source checkout.

Python 3.11+. Runtime checks need Bash 4+ (Bash 5 is recommended).
No network access, desktop changes or third-party Python packages.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import struct
import subprocess
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
BASE = 'red yellow orange green cyan blue magenta brown'.split()
BRIGHT = 'bright_red bright_yellow bright_green bright_cyan bright_blue bright_magenta'.split()
NEUTRAL = 'background dark_background darker_background lighter_background foreground dark_foreground light_foreground bright_foreground'.split()


def luminance(color):
    rgb = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
    return sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    low, high = sorted((luminance(a), luminance(b)))
    return (high + 0.05) / (low + 0.05)


def png_size(path):
    with path.open('rb') as stream:
        header = stream.read(24)
    assert header[:8] == b'\x89PNG\r\n\x1a\n' and header[12:16] == b'IHDR', path
    return struct.unpack('>II', header[16:24])


def validate_assets():
    colors = tomllib.loads((ROOT / 'colors.toml').read_text())
    for key in BASE + BRIGHT + NEUTRAL + ['accent', 'selection', 'muted']:
        assert re.fullmatch(r'#[0-9a-fA-F]{6}', colors[key]), key
    assert colors['mode'] == 'dark'
    assert re.fullmatch(r'rgba\([0-9a-fA-F]{8}\) rgba\([0-9a-fA-F]{8}\) 45deg', colors['hyprland_active_border'])
    assert (ROOT / 'icons.theme').read_text().strip() == 'Yaru-prussiangreen'
    ramp = ['darker_background', 'dark_background', 'background', 'lighter_background', 'selection', 'muted', 'dark_foreground', 'foreground', 'light_foreground', 'bright_foreground']
    assert all(luminance(colors[a]) < luminance(colors[b]) for a, b in zip(ramp, ramp[1:]))
    for key in BASE + BRIGHT + ['foreground', 'dark_foreground', 'muted', 'accent']:
        for surface in ['background', 'lighter_background']:
            assert contrast(colors[key], colors[surface]) >= 4.5, (key, surface)
    assert contrast(colors['bright_foreground'], colors['selection']) >= 7
    print(f"PASS palette: {len(colors)} keys; body {contrast(colors['foreground'], colors['background']):.2f}:1; selected text {contrast(colors['bright_foreground'], colors['selection']):.2f}:1")
    names = ['01-rain.png', '02-snow.png', '03-mountain.png', '04-water.png']
    assert sorted(p.name for p in (ROOT / 'backgrounds').iterdir()) == names
    for name in names:
        path = ROOT / 'backgrounds' / name
        assert png_size(path) == (4096, 2304), path
        assert path.stat().st_size < 50_000_000, path
    assert png_size(ROOT / 'preview.png') == (1600, 900)
    print('PASS assets: four 4096 x 2304 wallpapers and 1600 x 900 preview')
    for path in list(ROOT.glob('README*.md')) + list((ROOT / 'docs').glob('*.md')):
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if not re.match(r'https?://|#', link):
                assert (path.parent / link.split('#')[0]).exists(), (path.name, link)
    for name in ['README.md', 'README.ja.md', 'README.zh-CN.md', 'LICENSE']:
        assert (ROOT / name).is_file(), name
    print('PASS documentation: language files and all relative Markdown links')
    return colors


def validate_upstream(source, bash, colors):
    source = source.resolve()
    templates = sorted((source / 'default/themed').glob('*.tpl'))
    assert len(templates) == 17, 'Expected all 17 templates from Omarchy v4.0.0'
    bash_path = shutil.which(bash)
    assert bash_path, f'Bash executable not found: {bash}'
    def run(args, env):
        result = subprocess.run(args, env=env, text=True, capture_output=True, check=True)
        assert not result.stderr, result.stderr
        return result.stdout
    with tempfile.TemporaryDirectory(prefix='shigure-validate-') as directory:
        sandbox = Path(directory)
        stage = sandbox / '.local/state/omarchy/current/next-theme'
        stage.mkdir(parents=True)
        shutil.copy2(ROOT / 'colors.toml', stage / 'colors.toml')
        wrappers = sandbox / 'bin'
        wrappers.mkdir()
        helper = wrappers / 'omarchy-theme-color'
        helper.write_text('#!/bin/sh\nexec ' + shlex.join([bash_path, str(source / 'bin/omarchy-theme-color')]) + ' "$@"\n')
        helper.chmod(0o755)
        env = dict(os.environ, HOME=str(sandbox), OMARCHY_PATH=str(source), PATH=str(wrappers) + os.pathsep + os.environ.get('PATH', ''))
        raw = run([bash_path, str(source / 'bin/omarchy-theme-color'), '--file', str(stage / 'colors.toml'), '--all'], env)
        resolved = dict(line.split('\t', 1) for line in raw.splitlines())
        ansi = ['background', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'foreground', 'muted', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_foreground']
        for index, key in enumerate(ansi):
            assert resolved[f'color{index}'] == colors[key], key
        assert resolved['selection_foreground'] == colors['bright_foreground']
        assert resolved['selection_background'] == colors['selection']
        assert resolved['cursor'] == colors['bright_foreground']
        assert resolved['mode'] == 'dark'
        run([bash_path, str(source / 'bin/omarchy-theme-set-templates')], env)
        for template in templates:
            output = stage / template.name.removesuffix('.tpl')
            text = output.read_text()
            assert text.strip() and '{{' not in text and '}}' not in text, output.name
            if output.suffix == '.toml':
                tomllib.loads(text)
            elif output.suffix == '.json':
                json.loads(text)
        shell = tomllib.loads((stage / 'shell.toml').read_text())
        assert shell['hyprland']['active-border'] == colors['hyprland_active_border']
        border = (stage / 'hyprland.lua').read_text()
        assert '"rgba(84A7BDee)", "rgba(8FB8B5ee)"' in border and 'angle = 45' in border
        print('PASS upstream: ANSI aliases, cursor, selection, 17 templates, TOML/JSON parsing and gradient output')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upstream', type=Path, help='Local official Omarchy v4.0.0 source directory')
    parser.add_argument('--bash', default='bash', help='Bash 4+ executable; use /opt/homebrew/bin/bash on macOS')
    args = parser.parse_args()
    palette = validate_assets()
    if args.upstream:
        validate_upstream(args.upstream, args.bash, palette)
    else:
        print('SKIP upstream rendering (provide --upstream and Bash 4+)')
