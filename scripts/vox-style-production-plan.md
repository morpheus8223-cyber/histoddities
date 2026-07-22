# Next Longform Production Plan — Vox-Style Upgrade

Prompted by a reference video (youtube.com/watch?v=PaXuebdY75U) explaining how one
creator built a Claude+Higgsfield workflow to imitate Vox's documentary style.
Analyzed via `video_analysis_create`/`video_analysis_status` (59-scene breakdown).
That video is ~70% course-sales pitch; this doc extracts only the actual reusable
technique and adapts it to HistOddities' own brand rather than copying Vox's.

## What the reference video actually does (stripped of the sales pitch)
1. Script written to explicitly hit scene-type variety: a stat/number, a graph, a
   historical event, and a simple human story, all in ~60s / 6 scenes.
2. Narration recorded with a warm "cinematic narrator" voice (they used ElevenLabs'
   "Alex - Business Book Narrator"), not a flat/dreary read.
3. Every scene is built from 5 layered assets: **text, main object (with a
   paper-unfold reveal), background, secondary objects, camera move** (pan/zoom).
   This is a formalization, not a new idea — it's the same device list our own
   `pipeline/compositing.py` already partially covers.
4. Visual design system: aged cream paper, halftone/ink-speckle texture, one accent
   color, hand-drawn wobbly line art for charts/maps, character/object cutouts.
5. Assembly: designs → short animated clips → cut together with narration + a
   background music bed in an NLE.
6. Their reported cost: ~$20 in Higgsfield credits for a full 60s/6-scene piece —
   because most scenes are cheap flat-vector stills + simple motion, not full
   text-to-video generation. This is much cheaper than our current per-block
   cinematic AI video approach (Kling/Seedance run 20-90 credits per 10s clip alone).

## Live-tested finding: the capability is real, with one fix required
Tested `recraft_v4_1` (`model_type: vector`) directly:
- Prompting with "Vox documentary style" **reproduced Vox's actual wordmark/logo**
  on every asset (confirmed on 2/2 test images: a map and a line graph) — the
  model has clearly learned "Vox" as a literal brand mark, not just an aesthetic
  descriptor. Shipping that would be brand impersonation, not homage — a hard no.
- Fix: describe the visual attributes directly instead of naming the brand —
  "hand-drawn wobbly black ink line art, off-white background, ink-speckle
  texture, one accent color, no logos, no watermark, no brand marks." Retested:
  clean result, same look, zero logo. **This is the prompting rule for every
  infographic asset going forward — never write "Vox" in a generation prompt.**
- Conclusion: yes, Higgsfield can produce this style, reliably, once prompted
  correctly. Confirmed via `recraft_v4_1` vector mode; SVG output also means these
  assets scale/animate cleanly (no raster upscaling artifacts).

## New scene taxonomy for scripts (the actual "AI + real footage in harmony" answer)
Going forward, every block in a longform script gets tagged with one of three
production paths — this is the harmony model the user asked about:

| Scene type | When to use | Production path |
|---|---|---|
| **Narrative** | Human story beats, staged/invented scenes with no surviving photography | Existing cinematic AI pipeline (nano_banana_pro/Seedream stills → Kling/Seedance clips) |
| **Archival** | Real people/places/objects with surviving photos or footage | Existing `sourcing.py` + `archival_bw()`/`circle_callout()`/`ken_burns_clip()` |
| **Data-Explainer** *(new)* | Stats, numbers, geography, timelines, cause-and-effect | New flat-vector infographic devices (below) — cheap, fast, raises the "explained clearly" feel Vox is known for |

Mixing in Data-Explainer scenes for the numbers/geography beats both **raises
perceived production value** (this is the single most recognizable Vox signature)
**and lowers total cost**, since those scenes don't need 10s AI video clips at all
— a still + simple pan/zoom/draw-on reveal via `ken_burns_clip()`-style motion is
enough, the same way `definition_card()` already works today.

## New `compositing.py` additions needed
Existing devices (`archival_bw`, `circle_callout`, `definition_card`,
`ken_burns_clip`) already cover 3 of the reference video's 5 asset layers
(background, secondary objects/callouts, camera move). Two new devices to build:
- `map_reveal()` — a region/country outline with a marker + callout label,
  optionally with a slow line-draw-on animation for the outline itself.
- `graph_reveal()` — a line/bar chart with a draw-on animation and one circled
  data point + callout label (exactly the test asset above).
Both should default to the brand-safe prompt template above, with a single accent
color param so it can either match the existing Ashcan crimson/gold palette or use
a distinct color to visually mark "this is an explainer beat" the way Vox alternates
tone between narration and data scenes.

## Voice
Switched the default narration voice from **Gideon** (user feedback: "too dreary")
to **Cillian** — user's pick after comparing 4 test samples (Sterling, Harrison,
Orion, Cillian) rendered against the same line. Update every future `generate_audio`
call's `voice_id` to `d8ba9f14-8a24-44db-932b-99e16c45bd32` (Cillian, preset) going
forward; this replaces `1ad38ba4-9cc4-4f2f-9fde-b0fefdf67ae5` (Gideon) as default.

## Known gap: music bed
The reference workflow adds a synth-wave background music bed under narration.
Higgsfield's music model (`sonilo_music`) is restricted to the game-generation
pipeline per its own tool description and must not be used for standalone video —
so a background score needs a separate free/licensed source (e.g. YouTube Audio
Library) rather than an in-house generation call. Flagging this as an open sourcing
task, not solved yet.

## Script-writing checklist update (entertainment + education value)
Adopt the reference video's explicit scene-diversity requirement as a checklist for
every future longform script, not just an instinct:
- [ ] At least one hard number/statistic beat
- [ ] At least one graph/data beat (if the topic has quantifiable data)
- [ ] At least one geography/map beat (if the topic spans locations)
- [ ] At least one concrete historical-event beat
- [ ] At least one simple human-scale story beat (a specific person's experience,
      not just institutional facts)

## Next steps
1. Build `map_reveal()` and `graph_reveal()` in `pipeline/compositing.py`, smoke-test
   against a real dataset the way `archival_bw()`/`definition_card()` were proven.
2. Pick the next longform topic — the Series B shorts' pinned comments (B1/B2/B4/B5)
   are explicitly designed to let audience engagement decide this once they're live
   this week; recommend waiting for that signal rather than guessing now, per the
   channel's own established strategy.
3. Once a topic is picked, write the script using the checklist above, tag every
   block with its scene type (Narrative/Archival/Data-Explainer), and produce using
   the three-path pipeline with Cillian as narrator.
