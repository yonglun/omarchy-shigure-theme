# Omarchy 4.0 compatibility

Verification date: 2026-09-18. Target: the official **v4.0.0** tag, not a moving
branch or an inferred older theme format.

## Upstream references

- [Theme specification](https://github.com/omacom/omarchy/blob/v4.0.0/docs/theming.md)
- [Theme authoring manual](https://github.com/omacom/omarchy/blob/v4.0.0/manual/43-making-your-own-theme.md)
- [Color resolver](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-color)
- [Template renderer](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-set-templates)
- [Application templates](https://github.com/omacom/omarchy/tree/v4.0.0/default/themed)
- [Git installer](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-install)
- [Theme activation](https://github.com/omacom/omarchy/blob/v4.0.0/bin/omarchy-theme-set)

## Findings and changes

The original theme already used valid semantic names and a valid
`hyprland_active_border` gradient. Omarchy 4.0 does not require a legacy
`color0`–`color15` block alongside those names: its resolver supplies those aliases.
This refresh keeps the flat canonical format, explicitly sets `mode = "dark"`,
defines `brown` instead of accepting its derived fallback, and brightens readable
colors while retaining the indigo / warm-paper / vermilion direction.

The palette contains 25 six-digit sRGB color values, plus mode and a supported
Hyprland gradient. `selection_foreground` and the cursor resolve to
`bright_foreground`; `selection_background` resolves to `selection`. `muted`
resolves to ANSI color8. The neutral luminance ramp is strictly increasing from
`darker_background` through `bright_foreground`.

A theme does not need its own shell, terminal or editor configuration. Omarchy
renders those files from its templates. This package therefore contains no
application overrides, Lua payloads or executable theme hooks. The authoring
validator in `scripts/` is not an installation hook and is never required to
apply the theme.

Later Omarchy releases changed how downloaded executable theme overrides are
handled. This package does not depend on those files, and this report does not
attribute that later behavior to the original v4.0.0 installer.

## Checks performed

| Check | Result |
|---|---|
| TOML parsing and canonical fields | Pass; all color values are quoted six-digit hex strings |
| Explicit dark mode | Pass |
| Complete semantic and bright palette | Pass; 16 ANSI aliases resolve correctly |
| Original upstream color resolver | Pass; no stderr or rejected values |
| Original upstream template renderer | Pass; all 17 outputs produced without unresolved placeholders |
| Generated TOML / JSON | Pass; parsed with Python standard-library parsers |
| Hyprland gradient | Pass; Lua gradient table contains both RGBA colors and a 45-degree angle |
| Shell gradient | Pass; generated `[hyprland].active-border` matches the palette |
| Installer naming and cloning | Pass in a disposable local Git fixture; activation command receives `shigure` |
| Wallpapers | Pass; four fully decoded RGB PNGs, 4096 × 2304, 16:9, sRGB chunks |
| Preview | Pass; fully decoded 1600 × 900 PNG derived from Rain |
| Documentation | Pass; three language editions and relative Markdown links checked |

The 17 generated files are `alacritty.toml`, `btop.theme`, `chromium.theme`,
`claude.json`, `foot.ini`, `ghostty.conf`, `gum_env.lua`, `helix.toml`,
`hyprland-preview-share-picker.css`, `hyprland.lua`, `keyboard.rgb`, `kitty.conf`,
`neovim.lua`, `obsidian.css`, `pi.json`, `shell.toml`, and `vscode-theme.json`.

The installer smoke test used the unmodified installer, real `git clone` from a
temporary local repository named `omarchy-shigure-theme`, and an activation stub
that records the requested theme name. It verifies installer naming, cloning and
dispatch, not an end-to-end Linux desktop installation or GitHub availability.

## Contrast

Relative sRGB luminance, measured on opaque colors:

| Pair | Contrast |
|---|---:|
| Main text / background | 12.38:1 |
| Main text / raised surface | 10.05:1 |
| Selected text / selection | 7.75:1 |
| Eight base named colors / background | At least 5.94:1 |
| Eight base named colors / raised surface | At least 4.82:1 |

The validator also checks that muted text, secondary text, the accent and all
bright syntax colors achieve at least 4.5:1 on both main and raised backgrounds.
These are palette checks, not a blanket accessibility certification: application
mixing, opacity, wallpaper, font rendering and custom templates can affect results.

## Reproduce

For file, palette and documentation checks, use Python 3.11 or newer:

```bash
python3 scripts/validate-theme.py
```

To additionally execute the upstream resolver and all templates, obtain an
official Omarchy source checkout at **v4.0.0**, then pass its directory:

```bash
python3 scripts/validate-theme.py --upstream /path/to/omarchy
```

Bash 4+ is required by upstream's associative arrays; Bash 5 is recommended.
On macOS with Homebrew Bash installed:

```bash
python3 scripts/validate-theme.py \
  --upstream /path/to/omarchy \
  --bash /opt/homebrew/bin/bash
```

The upstream source is executed as local code: use the official release.
The validator uses a disposable home directory for those subprocesses and removes
its generated files afterwards. It never selects a theme on the current desktop.
The initial verification used Bash 5.3.20 on macOS. The original resolver and
renderer were invoked unchanged; a PATH wrapper selected the supported Bash for
the helper because macOS `/bin/bash` is version 3.2.

## Remaining runtime verification

A real Omarchy/Hyprland session was unavailable in this macOS workspace.
Consequently, shell rendering, actual Yaru icon availability, application reload
hooks, monitor cropping and visual appearance in running editors are **not**
claimed as tested. Generated Lua was inspected but not executed inside Hyprland
or Neovim. A future upstream version or user template can alter the result.

For final desktop acceptance on Omarchy 4.0.x: install the local theme as described
in the README, apply `shigure`, cycle through all four backgrounds, and inspect a
terminal, Neovim, the theme selector, notifications and the lock screen. Check
focused borders, selected text, diagnostic colors and dimmed comments.
