# Documentary Compositing Pipeline

Built from directly analyzing the Pythia V2 video (real footage, downloaded and
frame-sampled — see `scripts/pythia-v2-upload-package.md`) and the existing
19-thumbnail in-house brand audit (`analysis/thumbnail-full-audit-and-licensing.md`).
This is a **complement** to the pure AI-generation pipeline (Higgsfield
kling3_0_turbo / nano_banana_pro), not a replacement — future videos mix both:
AI-generated clips for scenes with no surviving visual record, real sourced
photos + this template system for anything with actual historical
photography, art, or artifacts.

## Why this exists

Pythia V2's main body (everything except its uncleared-footage outro, flagged
separately below) uses real archival material — engravings, statue
photography, museum artifact photos — run through a small, repeatable set of
motion-graphics templates, not one-off manual edits. Those templates are the
same devices already proven in HistOddities' own thumbnail brand (circle
callouts, color-coded accents). This pipeline rebuilds those devices as
scriptable steps so they can be applied consistently across future videos.

## Modules

### `sourcing.py` — real, license-free images
```python
from sourcing import search_wikimedia, download_wikimedia_file
results = search_wikimedia("Boston Molasses Flood 1919", limit=5)
path, license_txt = download_wikimedia_file(results[0], "out_dir/")
```
- Wikimedia Commons is the default, no API key needed. Every download writes
  a `.license.txt` sidecar recording the exact license/credit/artist found on
  that specific file — **the per-file tag is what matters, never assume
  "hosted on Commons" means usable.**
- Live-tested against the real `BostonMolassesDisaster.jpg` (public domain)
  for the next planned longform video.
- Smithsonian Open Access helper included (`search_smithsonian`, needs a free
  api.data.gov key) for topics Commons doesn't cover well.

### `compositing.py` — the four recurring devices

| Function | Device | Source evidence |
|---|---|---|
| `archival_bw()` | desaturated archival look | every real photo/engraving in Pythia V2's main body |
| `circle_callout()` | yellow "look here" evidence circle | Pythia V2 (Socrates' face) + thumbnail brand (Palme suspect, Cleopatra's ochre bowl, Tulip price tag) |
| `definition_card()` | cutout portrait on a solid accent-color circle + serif label + bracketed subtitle + body text | Pythia V2's "Mantis" / "Gaia" term cards |
| `ken_burns_clip()` | slow zoom/pan turning a still into a clip | every real-photo shot in Pythia V2 |

**`definition_card()` needs a subject-only cutout with a transparent
background**, not a plain rectangular photo — otherwise the portrait's own
background just covers the accent circle instead of letting it show around
the silhouette, which is the entire point of the device. For real sourced
photos with a busy or non-plain background, run the image through
Higgsfield's `remove_background` tool first (upload → confirm → remove →
download the RGBA result), then pass that cutout in. Proven live: a real
CC0 marble-bust photo, background-removed, correctly floats on the yellow
circle with the label box and body text.

`ken_burns_clip()` auto-detects the sandboxed ffmpeg binary
(`imageio_ffmpeg`) if plain `ffmpeg` isn't on PATH — no extra setup needed.

## Per-block production workflow

For each block in a script's production-blocks doc, decide real vs. generated:
1. **Real photo/artifact exists** (people, places, objects with surviving
   photography or art) → `sourcing.py` → `archival_bw()` →
   `circle_callout()` (if the block is highlighting a specific detail) →
   `ken_burns_clip()` to turn it into a timed clip.
2. **No surviving visual record** (ancient staged scenes, invented
   likenesses) → stays on the existing Higgsfield AI-generation path
   (kling3_0_turbo / nano_banana_pro), exactly as done for Cadaver Synod and
   planned for the Molasses Flood script.
3. **A term/concept needs defining** → `definition_card()`, portrait either a
   real cutout (background-removed) or an AI-generated stylized portrait,
   accent color cycling per card the way the source alternates yellow/green.

Final assembly (mixing real-photo clips and AI-generated clips into one
timeline) still goes through the same ffmpeg concat step already used for
Cadaver Synod's 51-block assembly.

## Known gap — do not reuse as-is

Pythia V2's outro montage (last ~10-15s, under the Subscribe/bell overlay)
appears to be uncleared Hollywood film footage, not license-free stock —
one shot reads as a *Gladiator*-style arena scene, another as an
epic-crowd/procession scene. Do not pull B-roll from that segment into any
future video without confirming its actual source; treat it as a Content
ID / copyright-strike risk until then. One earlier B&W athletic sequence in
the main body (stroboscopic multi-exposure javelin throwers) also resembles
Riefenstahl's 1936 Olympics footage, whose licensing is murkier than plain
public domain — worth a quick check before reuse as well.

## Smoke-tested, not yet a finished shot

Everything above has been run end-to-end on real files (the actual public-domain
Molasses Flood photo, a real CC0 marble bust) to prove the mechanics work —
these are reusable primitives, not a finished rendered sequence. Building an
actual video block still means picking real shots per script beat and calling
these functions with real framing choices, the same way each Higgsfield
generation call is chosen per block today.
