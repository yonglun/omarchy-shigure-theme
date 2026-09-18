# Shigure / 時雨

**Four quiet landscapes. One indigo desktop.**

English · [日本語](README.ja.md) · [简体中文](README.zh-CN.md)

![Shigure — a timber bridge in slanting rain](preview.png)

A dark theme for **Omarchy 4.0**, pairing warm paper text with ink-blue surfaces,
mist-blue focus borders and a small touch of vermilion. Four distinct wallpapers
bring **rain, snow, mountain and water** to the same calm workspace.

## A landscape to work in

Shigure draws its inspiration from **Utagawa Hiroshige's ukiyo-e**. Fine ink
contours, flat printed colors, bokashi gradations and paper-white snow preserve
the character of Japanese woodblock prints. Wide asymmetric compositions and
generous negative space bring that language to a modern desktop.

The inspiration is compositional: diagonal rain, cropped foregrounds, distant
layers and the relationship between ink and unprinted paper. Hiroshige's
[Sudden Shower over Shin-Ōhashi Bridge and Atake](https://www.metmuseum.org/art/collection/search/55433)
offers historical context. The wallpapers here are newly generated contemporary
interpretations, not scans, reproductions or works by Hiroshige.

Vermilion acts like a small punctuation mark. Indigo gives the desktop its
structure; warm text keeps it welcoming through long working sessions.

## Install

On **Omarchy 4.0.x**, after this repository has been published:

```bash
omarchy theme install https://github.com/yonglun/omarchy-shigure-theme
```

The installer derives the name `shigure` and applies the theme. To select it again
or move to the next wallpaper:

```bash
omarchy theme set shigure
omarchy theme bg next
```

**Using a downloaded folder before publication:** from inside that folder, copy
the theme into Omarchy's user-theme directory. If `shigure` already exists, back
it up first; these commands replace files with matching names.

```bash
mkdir -p ~/.config/omarchy/themes/shigure/backgrounds
cp colors.toml icons.theme preview.png ~/.config/omarchy/themes/shigure/
cp backgrounds/*.png ~/.config/omarchy/themes/shigure/backgrounds/
omarchy theme set shigure
```

On a fresh activation, **Rain** is first in filename order. Subsequent selection
behavior follows your Omarchy version. The preview above shows the wallpaper,
not a live desktop screenshot.

## Four studies

| Rain · 雨 | Snow · 雪 |
|:---:|:---:|
| [![Rain](docs/images/01-rain.jpg)](backgrounds/01-rain.png) | [![Snow](docs/images/02-snow.jpg)](backgrounds/02-snow.png) |
| A diagonal timber bridge, two umbrella-bearing travelers and finely cut rain lines. | Snow-covered inns, a plum branch and travelers on a curving white path. |

| Mountain · 山 | Water · 水 |
|:---:|:---:|
| [![Mountain](docs/images/03-mountain.jpg)](backgrounds/03-mountain.png) | [![Water](docs/images/04-water.jpg)](backgrounds/04-water.png) |
| Mount Fuji beyond blue foothills, framed by a boldly cropped pine. | Irises and two carp among flowing lines and broad blue water. |

Click an image for the full wallpaper. All four are text-free **4096 × 2304 PNGs,
16:9, sRGB**. Each has its own subject and composition; none contains a boat.
They share one palette, so switching landscapes does not require a new theme.

The generated sources were **1672 × 941**, resampled for delivery. The files have
4K-class dimensions; they do not contain native 4K generated detail.

## The palette

![Shigure palette](docs/images/palette.svg)

| Role | Color | Purpose |
|---|---|---|
| Ink | `#101F2B` | Main background |
| Raised indigo | `#1B3040` | Secondary surfaces |
| Warm paper | `#E3DDCF` | Main text |
| Snow | `#F3EFE6` | Cursor and brightest text |
| Mist blue | `#84A7BD` | Blue syntax and focus border |
| Water green | `#8FB8B5` | Cyan syntax and gradient endpoint |
| Pine | `#9CAC89` | Green syntax |
| Vermilion | `#D58B72` | Selected controls and UI accent |
| Ochre | `#D3B57D` | Yellow syntax |

These are custom Shigure colors, not claims of standardized historical pigments.
Main text has **12.38:1** contrast against the background; all eight base named
colors exceed **5.9:1** on that background. Selected text is **7.75:1**.
These measurements cover opaque palette pairs, not every application's rendering.

## Omarchy compatibility

[`colors.toml`](colors.toml) supplies the complete semantic palette, explicit
`mode = "dark"`, bright colors and a supported cool border gradient. Omarchy
generates the terminal, editor, Hyprland and shell configuration from its own
templates. `icons.theme` selects the documented `Yaru-prussiangreen` variant.
There are no executable theme hooks or application config overrides to maintain.

Compatibility is checked against the **v4.0.0** color resolver and templates.
See [verification details and limitations](docs/COMPATIBILITY.md). A live Omarchy
desktop installation has not been tested in this macOS workspace.

## Artwork & reuse

The collection is inspired by Utagawa Hiroshige's ukiyo-e.
The [artwork record](docs/ARTWORK.md) documents image production and processing.
Omarchy is an independent upstream project; Shigure is a community theme.

Configuration, documentation and supplied artwork are distributed under the
[MIT License](LICENSE). If you share a screenshot or a variation, a link back to
Shigure helps others find it.

Suggested repository description: *A quiet indigo theme for Omarchy — rain,
snow, mountains and water, inspired by Utagawa Hiroshige's ukiyo-e.*

Suggested topics: `omarchy-theme`, `omarchy`, `hiroshige`, `ukiyo-e`, `dark-theme`,
`wallpaper`, `indigo`.
