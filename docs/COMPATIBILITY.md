# Shigure II — Omarchy 4.0 compatibility

Verification date: **2026-10-01**. Target: the official **v4.0.0** tag.
This report covers the local moon-gold second-edition candidate.

## Official interfaces

- [Theme specification](https://github.com/omacom/omarchy/blob/v4.0.0/docs/theming.md)
- [Theme authoring manual](https://github.com/omacom/omarchy/blob/v4.0.0/manual/43-making-your-own-theme.md)
- [Color resolver](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-color)
- [Template renderer](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-set-templates)
- [Application templates](https://github.com/omacom/omarchy/tree/v4.0.0/default/themed)
- [Git installer](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-install)
- [Theme activation](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-set)
- [Background cycling](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-bg-next)

The unchanged upstream resolver, renderer and 17 templates were obtained from
the official tag. All **20** entries in [the pinned SHA-256 list](upstream-v4.0.0.sha256)
matched before the final rendering check. Rendering uses a disposable HOME;
no theme is selected on this macOS desktop.

## Theme format and behavior

`colors.toml` uses 27 flat canonical fields: 25 six-digit color values, explicit
`mode = "dark"` and the supported gradient. Only `accent`, `bright_foreground`
and `hyprland_active_border` change from the first edition.
The resolver supplies `color0`–`color15` aliases; cursor and selection foreground
resolve to moon-white `bright_foreground`, and selection background to `selection`.
`icons.theme` retains `Yaru-prussiangreen`.

Omarchy renders application configuration from its own templates. This theme
contains no application overrides or executable installation hooks; the Python
authoring validator is not required to apply it.

Code inspection confirms that URL installation derives `shigure` from
`omarchy-shigure-theme` and replaces an existing same-name theme directory
before cloning. Local candidate instructions use a separate `shigure-ii`
directory so the first edition can remain installed. On a fresh theme selection
without additional user wallpapers, filename order starts with `01-moon.png`;
subsequent behavior and user wallpaper overrides follow the upstream selector.
The optional `bg next` command is separate from the installation block.

## Checks performed for this candidate

| Check | Result |
|---|---|
| TOML, canonical semantic fields and dark mode | Pass; 27 keys |
| Neutral luminance ramp and readable text colors | Pass |
| Original upstream resolver | Pass; 16 ANSI aliases, cursor and selection |
| Original upstream renderer | Pass; all 17 outputs, no unresolved placeholders or stderr |
| Generated TOML / JSON | Pass; standard-library parsers |
| Hyprland gradient | Pass; old gold and mist blue, angle 45 |
| Shell gradient | Pass; matches `hyprland_active_border` |
| Active wallpaper set | Pass; exactly Moon, Rain, Snow and Tide |
| Wallpaper full decoding and source hashes | Pass; unchanged 1672 × 941 RGB PNGs, no embedded ICC |
| Preview and gallery full decoding | Pass; Moon 1600 × 900 PNG; four 1024 × 576 JPEGs |
| Documentation | Pass; three language editions and relative links |

The outputs are `alacritty.toml`, `btop.theme`, `chromium.theme`, `claude.json`,
`foot.ini`, `ghostty.conf`, `gum_env.lua`, `helix.toml`,
`hyprland-preview-share-picker.css`, `hyprland.lua`, `keyboard.rgb`, `kitty.conf`,
`neovim.lua`, `obsidian.css`, `pi.json`, `shell.toml` and `vscode-theme.json`.

Precise image metadata, palette differences and local package checks are in
[VALIDATION.json](VALIDATION.json). Sources and processing are documented in
[ARTWORK.md](ARTWORK.md). Wallpapers keep the original generation dimensions;
no native 4K or embedded color-profile claim is made.

## Contrast

Relative sRGB luminance for specified opaque color pairs:

| Pair | Contrast |
|---|---:|
| Main text / background | 12.38:1 |
| Main text / raised surface | 10.05:1 |
| Moon-white selected text / selection | 7.24:1 |
| Old gold / background | 8.66:1 |
| Old gold / raised surface | 7.03:1 |
| Minimum of the 40 checked text / surface pairs | 4.64:1 |

These measurements do not certify every application's final rendering.

## Reproduce

Use Python 3.11+ for file, palette and documentation checks:

```bash
python3 scripts/validate-theme.py
```

To run the resolver and templates, use an official v4.0.0 checkout and Bash 4+.
The final check used Bash 5.3.20 on macOS:

```bash
python3 scripts/validate-theme.py \
  --upstream /path/to/omarchy-v4.0.0 \
  --bash /opt/homebrew/bin/bash
```

The CLI has no network behavior and uses a temporary home for rendering. Its
PNG checks inspect headers; the full image decoding and source-hash checks
recorded in VALIDATION.json were additionally performed with bundled Pillow.

## Remaining desktop verification

A live Omarchy/Hyprland session was unavailable. Actual Yaru icon availability,
application reloads, Lua execution in Hyprland or Neovim, monitor cropping and
visual appearance in running applications remain untested. This is a local
candidate; it has not been published or installed on a live Omarchy desktop.

For desktop acceptance, apply the local `shigure-ii` candidate on Omarchy 4.0.x,
cycle through Moon, Rain, Snow and Tide, and inspect a terminal, Neovim, the theme
selector, notifications and lock screen. Check focus borders, selected text,
diagnostic colors and dimmed comments. Later releases and user templates can
change the behavior.
