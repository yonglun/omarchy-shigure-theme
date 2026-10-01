# Shigure II · 月下

**Moon, rain, snow and tide. A quiet indigo desktop under moonlight.**

English · [日本語](README.ja.md) · [简体中文](README.zh-CN.md)

![Shigure II — moon above a distant bay](preview.png)

A dark theme for **Omarchy 4.0**, pairing ink-blue surfaces and warm paper text
with old-gold interaction accents, a moon-white cursor and an old-gold-to-mist-blue
focus border. Four distinct wallpapers bring **moon, rain, snow and tide** to one
calm workspace. Moon is the default wallpaper.

## A landscape to work in

Shigure II draws its inspiration from **Utagawa Hiroshige's ukiyo-e**: fine ink
contours, flat printed colors, bokashi gradations and the relationship between
ink and unprinted paper. Asymmetric widescreen compositions and generous negative
space bring that language to a modern desktop.

Hiroshige's [Eight Views of Kanazawa at Night](https://www.clevelandart.org/art/1924.967)
provides historical context for the moonlight, low shore and horizontal layers.
The collection develops four separate compositions: a distant moonlit bay,
two umbrellas in rain, an unoccupied snowy lane and the tide seen from above.
Old gold marks interaction; indigo gives the desktop structure.

## Install

This is a **local Shigure II candidate**. From inside the downloaded theme folder,
install it in a new `shigure-ii` directory on **Omarchy 4.0.x**. It can coexist with
a first-edition `shigure` installation. If `shigure-ii` already exists, back it up
before copying; matching files will be replaced.

```bash
mkdir -p ~/.config/omarchy/themes/shigure-ii/backgrounds
cp colors.toml icons.theme preview.png ~/.config/omarchy/themes/shigure-ii/
cp backgrounds/*.png ~/.config/omarchy/themes/shigure-ii/backgrounds/
omarchy theme set shigure-ii
```

To switch wallpapers when desired (Moon → Rain → Snow → Tide):

```bash
omarchy theme bg next
```

On fresh activation, **Moon** is first in filename order. Subsequent wallpaper
selection follows your Omarchy version. The image above is a **1600 × 900 wallpaper
display copy**, not a live desktop screenshot.

**After this candidate has been published to the repository**, URL installation
will be available:

```bash
omarchy theme install https://github.com/yonglun/omarchy-shigure-theme
```

The URL installer derives the name `shigure` and applies the theme. That path uses
the first edition's directory name; back up an existing `shigure` before using it.
The candidate has not been published or installed in a live Omarchy session here.

## Four studies

| Moon · 月 | Rain · 雨 |
|:---:|:---:|
| [![Moon](docs/images/01-moon.jpg)](backgrounds/01-moon.png) | [![Rain](docs/images/02-rain.jpg)](backgrounds/02-rain.png) |
| A moon above a distant bay, low shores and reeds; open sky and water at the center. | Cropped eaves, slanting rain and two umbrella-bearing travelers; warmth in umbrellas and road. |

| Snow · 雪 | Tide · 潮 |
|:---:|:---:|
| [![Snow](docs/images/03-snow.jpg)](backgrounds/03-snow.png) | [![Tide](docs/images/04-tide.jpg)](backgrounds/04-tide.png) |
| An unoccupied snow scene with pine, houses and an S-shaped snowy lane. | A close overhead view of rocks and curving tidal water, with no sky or horizon. |

Click an image for the original wallpaper. All four are text-free **1672 × 941
PNG / RGB** files, with **no embedded ICC profile**. They preserve the actual
generated dimensions, approximately 16:9, without enlargement or additional color
grading; they are not native 4K images. The gallery uses **1024 × 576 JPEG** display
copies. All four share one theme palette.

## The palette

![Shigure II palette](docs/images/palette.svg)

| Role | Color | Purpose |
|---|---|---|
| Ink | `#101F2B` | Main background |
| Raised indigo | `#1B3040` | Secondary surfaces |
| Warm paper | `#E3DDCF` | Main text |
| Moon white | `#F0E7D5` | Cursor and brightest text |
| Old gold | `#CBB98B` | Selected controls, UI accent and focus-gradient start |
| Mist blue | `#84A7BD` | Blue syntax and focus-gradient end |
| Water green | `#8FB8B5` | Cyan syntax |
| Pine | `#9CAC89` | Green syntax |
| Vermilion | `#CE887D` | Red semantic color |
| Ochre | `#D3B57D` | Yellow syntax |

The focus border is `rgba(CBB98Bee) rgba(84A7BDee) 45deg`. Relative to the first
edition, only `accent`, `bright_foreground` and `hyprland_active_border` change;
other semantic colors remain intact. These are custom colors, not standardized
historical pigments.

Main text has **12.38:1** contrast against the main background; selected text is
**7.24:1**. Old gold measures **8.66:1** against the main background and **7.03:1**
against the raised surface. These are measurements of specified opaque color
pairs, not every application's final rendering.

## Omarchy compatibility

[`colors.toml`](colors.toml) supplies the semantic palette, explicit `mode = "dark"`,
bright colors and a supported focus gradient. Omarchy generates the terminal,
editor, Hyprland and shell configuration from its own templates.
[`icons.theme`](icons.theme) selects `Yaru-prussiangreen`. The theme contains no
executable hooks or application configuration overrides.

Verification targets official **v4.0.0**. See [coverage and limitations](docs/COMPATIBILITY.md)
and the [validation record](docs/VALIDATION.json). A live Omarchy desktop
installation has not been tested in this macOS workspace.

## Artwork & reuse

The collection is inspired by Utagawa Hiroshige's ukiyo-e. The images are newly
generated contemporary interpretations, not historical prints or scans.
Technical production used OpenAI's built-in ImageGen on 2026-10-01; the
[artwork record](docs/ARTWORK.md) links the complete prompts, revision comparisons
and actual source metadata.

Shigure II is a community theme, independent of Omarchy. The first edition is
preserved in Git commit `ceb04250c1e9816c83f909e599e924f12b57467c`.
Configuration, documentation and supplied artwork are distributed under the
[MIT License](LICENSE). A link back to Shigure is welcome when sharing a variation.

Suggested repository description: *A moonlit indigo theme for Omarchy — moon,
rain, snow and tide, inspired by Utagawa Hiroshige's ukiyo-e.*

Suggested topics: `omarchy-theme`, `omarchy`, `hiroshige`, `ukiyo-e`, `dark-theme`,
`wallpaper`, `indigo`.
