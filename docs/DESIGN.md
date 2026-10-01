# Shigure II · 月下 — design and implementation notes

## Intent

Develop the confirmed moon-gold second edition of Shigure for Omarchy 4.0.0.
Retain Hiroshige-inspired ink-blue surfaces, warm paper text and an ukiyo-e
woodblock vocabulary: sumi contours, flat pigment areas, bokashi gradations and
paper-white snow. Use old gold for interaction and moon white for the cursor.
Asymmetric widescreen compositions and negative space support a quiet desktop.

The historical compositional reference is Hiroshige's
[Eight Views of Kanazawa at Night](https://www.clevelandart.org/art/1924.967).
README inspiration sections foreground that visual source; technical ImageGen
provenance is documented separately in [ARTWORK.md](ARTWORK.md).

## Confirmed compositions

- **Moon / 月**, the default: distant moonlit bay, low shore and reeds; quiet central sky and water.
- **Rain / 雨**: cropped eaves, diagonal rain and two umbrella-bearing travelers; localized warm color in umbrellas and road.
- **Snow / 雪**: an unoccupied night scene with snow-covered pine, houses and an S-shaped snowy lane. The traveler from the initial concept was removed.
- **Tide / 潮**: an overhead close view of rocks and curved tidal currents. There is no sky or horizon; it differs from Moon's distant bay.

The four scenes share a palette without repeating the same composition. No
lettering, seals, boats or modern glowing elements belong to the selected artwork.
See the [confirmed integration design](superpowers/specs/2026-10-01-shigure-v2-integration-design.md)
and [concept revision record](v2-concepts/ARTWORK.md).

## Palette

Only three values change relative to the first edition:

| Semantic key | Shigure II value | Role |
|---|---|---|
| `accent` | `#CBB98B` | Old-gold interaction accent |
| `bright_foreground` | `#F0E7D5` | Moon-white cursor and brightest text |
| `hyprland_active_border` | `rgba(CBB98Bee) rgba(84A7BDee) 45deg` | Old-gold-to-mist-blue focus gradient |

Warm-paper body text, red `#CE887D`, yellow and all other semantic colors remain
unchanged. `icons.theme` retains `Yaru-prussiangreen`. Measured body contrast is
12.38:1 against the main background; selected text is 7.24:1. Old gold measures
8.66:1 against the main background and 7.03:1 against the raised surface.
These measurements apply to opaque specified pairs, not all final app rendering.

## Delivery and installation

Selected concept PNGs are copied unchanged to `backgrounds/01-moon.png`,
`02-rain.png`, `03-snow.png` and `04-tide.png`. Their actual dimensions are
1672 × 941, RGB, with no embedded ICC profile; they are not enlarged.
`preview.png` is a 1600 × 900 Moon display copy. The four matching gallery JPEGs
in `docs/images/` are 1024 × 576. Display copies are not desktop screenshots.

Local installation uses `~/.config/omarchy/themes/shigure-ii`, allowing coexistence
with first-edition `shigure`. URL installation is documented only for after this
candidate is published; the repository-derived name remains `shigure`.
The first edition is preserved in Git commit
`ceb04250c1e9816c83f909e599e924f12b57467c`.

## Verification boundaries

The theme stays declarative: no executable hooks, application overrides or added
dependencies. Verification targets official Omarchy v4.0.0 with palette checks,
image decoding and hashes, local documentation links and isolated upstream
rendering where available. See [COMPATIBILITY.md](COMPATIBILITY.md) and
[VALIDATION.json](VALIDATION.json) for actual results and limitations.

This stage produces a local installable candidate. It does not establish a
remote release or a successful live Linux/Omarchy desktop installation.
