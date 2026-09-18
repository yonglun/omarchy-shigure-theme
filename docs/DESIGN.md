# Shigure — design and implementation notes

## Intent

Refresh the existing Shigure / 時雨 theme for Omarchy 4.0.0. Retain the original
Hiroshige-inspired indigo, warm paper and restrained vermilion. Preserve an
unmistakable ukiyo-e woodblock vocabulary: sumi keyblock contours, flat pigment
areas, bokashi gradations, carved botanical detail and paper-white snow.
Modernity comes from asymmetric widescreen crops and generous negative space.

Four distinct subjects: a bridge in rain, a snow-covered post town, Mount Fuji
framed by pine, and irises with carp. No boats, lettering or logos. Avoid
cinematic lighting, realistic volumes and digitally painted alpine landscapes.
The README inspiration credits refer to Utagawa Hiroshige's ukiyo-e only;
technical generation provenance is recorded separately in ARTWORK.md.

## Implementation plan

1. Compare the palette, installer and templates with official Omarchy v4.0.0.
   Update colors.toml using its semantic keys; preserve declarative installation.
2. Generate four independent widescreen wallpapers using the built-in ImageGen
   tool. Inspect all outputs and record actual dimensions and generation prompts.
   Replace backgrounds/01-rain.png through 04-water.png and refresh preview.png.
3. Write README.md, README.ja.md and README.zh-CN.md with equivalent installation,
   artwork, inspiration, palette, attribution and license information.
4. Validate TOML, image metadata, local links, contrast and upstream rendering.
   Record exact coverage and limitations in docs/COMPATIBILITY.md.

## Constraints

- One palette for all four backgrounds; dark desktop surfaces and legible syntax.
- No application overrides or executable theme payloads.
- No claim of native 4K detail unless verified from generated files.
- No claim of live Linux desktop testing from this macOS workspace.
- Existing folder is not a Git checkout; do not invent a remote or commit history.
- Preserve original files in an external temporary backup while replacing assets.
