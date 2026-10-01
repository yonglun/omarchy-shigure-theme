# Shigure II · 月下 — artwork provenance

Visual inspiration: Utagawa Hiroshige's ukiyo-e, including sumi contours, flat
pigment areas, bokashi gradations, cropped foregrounds and unprinted-paper space.
The historical compositional reference is
[Eight Views of Kanazawa at Night](https://www.clevelandart.org/art/1924.967).
These are newly generated contemporary interpretations, not Hiroshige originals,
historical print scans or real Omarchy desktop screenshots.

## Production and selected sources

The four images were made with OpenAI's built-in ImageGen on **2026-10-01**.
Moon established the series' visual language; the first Rain, Snow and Tide
images used Moon as a style and palette reference. Rain was simplified; Snow and
Tide were revised after feedback about repeated compositions. The complete
[concept production and revision record](v2-concepts/ARTWORK.md) is retained.

| Delivered wallpaper | Selected original | Complete prompts | Final composition |
|---|---|---|---|
| [Moon](../backgrounds/01-moon.png) | [01-moon.png](v2-concepts/01-moon.png) | [Moon prompt](v2-concepts/moon-prompt.txt) | Distant moonlit bay, low shore, reeds; quiet central sky and water. |
| [Rain](../backgrounds/02-rain.png) | [02-rain-refined.png](v2-concepts/02-rain-refined.png) | [Initial prompt](v2-concepts/rain-prompt.txt) · [Refinement prompt](v2-concepts/rain-refine-prompt.txt) | Eaves, slanting rain, two umbrellas and road; lantern removed. |
| [Snow](../backgrounds/03-snow.png) | [03-snow-refined.png](v2-concepts/03-snow-refined.png) | [Initial prompt](v2-concepts/snow-prompt.txt) · [Refinement prompt](v2-concepts/snow-refine-prompt.txt) | Unoccupied snow night: pine, houses and an S-shaped snowy lane. |
| [Tide](../backgrounds/04-tide.png) | [04-tide-refined.png](v2-concepts/04-tide-refined.png) | [Initial prompt](v2-concepts/tide-prompt.txt) · [Refinement prompt](v2-concepts/tide-refine-prompt.txt) | Overhead close view of rocks and curved currents; no sky or horizon. |

The prompt files preserve the complete generation and editing instructions;
they are not abbreviated or reconstructed here. Initial
[Rain](v2-concepts/02-rain.png), [Snow](v2-concepts/03-snow.png) and
[Tide](v2-concepts/04-tide.png) remain as revision comparisons in the concept
record and are outside the active wallpaper set.

Rain's first draft had lettering-like texture on a lantern. An attempted
texture-only cleanup was not selected; the final edit removed the lantern while
retaining the eaves, diagonal rain, two umbrellas and road. Snow's straw-cloaked
traveler, staff and related traces were removed, leaving a fully unoccupied lane.
Tide was recomposed as an overhead close view, removing the sky, distant islands,
horizontal horizon and pine branch. Curved currents now distinguish it from
Moon's horizontal distant bay; Snow's empty scene distinguishes it from Rain's
travelers.

## Actual files and processing

All selected originals are **1672 × 941 PNG / RGB**, with **no embedded ICC
profile**. Active wallpapers retain those bytes and dimensions unchanged: no
upscaling, sharpening, retouching or additional color grading during integration.
The aspect ratio is approximately 16:9. Although initial prompts requested
3840 × 2160, the generated output is not native 4K.

The [source metadata](v2-concepts/image-metadata.json) records exact sizes and
SHA-256 hashes. The [concept validation record](v2-concepts/validation.json)
records the earlier source and palette checks; current integrated-theme results
are in [VALIDATION.json](VALIDATION.json) and [COMPATIBILITY.md](COMPATIBILITY.md).

`preview.png` is a **1600 × 900** Moon display copy made with macOS
`sips --resampleHeightWidth 900 1600`. Gallery JPEGs in `docs/images/` use the same
basenames as the active wallpapers and are **1024 × 576**, made with
`sips -Z 1024 -s format jpeg -s formatOptions 75`. These are presentation copies,
not live desktop captures or higher-resolution source artwork.

## Palette and edition history

Moon-gold interaction uses `accent = "#CBB98B"`, moon white uses
`bright_foreground = "#F0E7D5"`, and the focus border is
`rgba(CBB98Bee) rgba(84A7BDee) 45deg`. Only these three semantic values change
from the first edition. The current palette is [colors.toml](../colors.toml),
with its original candidate preserved in [v2-concepts/colors.toml](v2-concepts/colors.toml).

The first edition's Rain / Snow / Mountain / Water assets and provenance are
preserved in Git commit `ceb04250c1e9816c83f909e599e924f12b57467c`; they are not
part of this edition's active wallpaper directory. This is a local Shigure II
candidate, not a claim of publication or live Omarchy installation.

The configuration, documentation and supplied artwork use the repository's
[MIT License](../LICENSE).
