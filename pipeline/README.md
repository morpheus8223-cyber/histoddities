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

## Audio pacing — generate narration before assembly, then check duration

`explainer_video` forces every block into a fixed window (10s if that's what
the clip was generated at): a shorter voice take gets centered with silence
padding, a longer one gets sped up "pitch-safely" to fit. That speed-up is
audible and, on the Molasses Flood video, hit **23 of 60 blocks** — several
by 60-80% (worst cases ran ~17.5s crammed into 10s) — because narration was
written to *read* like a ~10s beat without ever checking the actual TTS
output length against the fixed block duration. The fix that worked:

1. After generating each `seed_audio` take, check its `durationSec` in the
   job result.
2. If it's off from the target block length by more than ~5%, regenerate
   with the `speech_rate` param (range -50..100, positive = faster) rather
   than letting `explainer_video` stretch it. Rough calibration from the
   Molasses Flood video: rendering at `speech_rate=20` sped a 12.0s take up
   to ~9.8s. **Update from the B1 short: this calibration does not reliably
   transfer to other text.** Two documented cases where it was actively
   non-monotonic — a *lower* speech_rate produced a *shorter* result than a
   higher one, and vice versa on the slow-down side. Treat speech_rate as a
   rough one-shot nudge, not a solvable formula; if a correction attempt
   doesn't converge, don't keep tuning the number — either trim/reword the
   line itself (this reliably works, unlike the parameter), or accept
   whichever take errs *under* the target rather than over it (padding is
   inaudible, the pitch-safe speedup is not).
3. Only then feed that block into `explainer_video`.

Doing this check-then-correct pass *before* assembly — not after noticing
the final video sounds rushed — is the real fix. For the next video, budget
one `job_display` duration check per audio take as a standard pipeline step,
not an optional one.

## Default voice change (Gideon → Cillian)

User feedback on the Molasses Flood video: Gideon (`1ad38ba4-9cc4-4f2f-9fde-b0fefdf67ae5`)
reads as "too dreary." Compared 4 alternatives via `seed_audio` on the same test line;
user picked **Cillian** (`d8ba9f14-8a24-44db-932b-99e16c45bd32`, preset). Use Cillian as
the default `voice_id` for all narration going forward.

## Vox-style upgrade — see `scripts/vox-style-production-plan.md`

Adds a third scene type — **Data-Explainer** (flat-vector maps, graphs, stat
callouts, brand-safe hand-drawn style via `recraft_v4_1`) — alongside the
existing Narrative (AI cinematic) and Archival (real photo) paths. **Prompting
rule discovered during testing: never write "Vox" in a generation prompt** —
`recraft_v4_1` reproduces the real Vox wordmark/logo when the brand is named
directly; describe the visual attributes (hand-drawn wobbly ink, off-white
background, ink-speckle texture, one accent color, no logos) instead, which
gives the same look with zero brand risk.

**First real build, and a correction**: the first attempt at a Data-Explainer
beat (B1's wild-vs-farm-rabbit mechanism) used a single flat merged image run
through `ken_burns_clip()` — user feedback was that this "was just an added
still basic drawing," i.e. it read as static despite the pan/zoom. Fixed with
`layered_reveal_clip()`: generate each visual element as its own transparent-
background cutout (`recraft_v4_1` with `background_color: null`), then stage
their fade/slide/scale-in entrances on independent timers synced to the
narration, plus text bands that fade up separately. This is what actually
makes a Data-Explainer beat feel like built-up motion graphics instead of a
still with camera movement — the pan/zoom alone was never the missing piece.

## Short-form script structure — hook / body / payoff-with-loop

Researched what actually drives retention on short-form (WebSearch, see
`scripts/series-shorts-production-log.md`'s B1 rebuild section for sources).
The structure that keeps viewers watching:
1. **Hook (first ~3s of the block)**: a bold claim, contradiction, or
   curiosity-gap opener, in short sentences — not a scene-setting intro.
2. **Body (escalating)**: setup, then a twist/mechanism beat that resolves the
   hook's tension — this is exactly where a Data-Explainer beat earns its
   place, giving the mechanism its own clear visual instead of burying it in
   narration.
3. **Payoff, with a callback loop**: resolve the hook's specific claim by name
   ("that undefeated record? gone") rather than just narrating the ending —
   the callback is what makes a viewer mentally rewatch the opening, which is
   the single biggest lever for retention/replays on this format.
Apply this structure to every future short's script draft, not just B1's.

## Smoke-tested, not yet a finished shot

Everything above has been run end-to-end on real files (the actual public-domain
Molasses Flood photo, a real CC0 marble bust) to prove the mechanics work —
these are reusable primitives, not a finished rendered sequence. Building an
actual video block still means picking real shots per script beat and calling
these functions with real framing choices, the same way each Higgsfield
generation call is chosen per block today.
