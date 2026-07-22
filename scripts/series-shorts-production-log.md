# Series Shorts Production Log — A1 & B3

Pipeline: nano_banana_pro still (style key referenced) → kling3_0_turbo 1080p 10s 9:16 → seed_audio (Gideon) → explainer_video assembly → local ffmpeg vertical check.

## A1 — It's Illegal To Wear Armor In Parliament
STYLE_KEY (reused): cf074148-fc16-4fbc-8dba-b80f8307d0a5
STILLS: 1:5abb1d8f-cbf6-4eba-b8b8-9ea5acf5e361 2:4cab96b1-7c16-49a2-b880-d84b6493fb8c 3:886e5130-1771-47cd-95d1-241bd5678684 4:5ca5ef05-2313-4d12-a8d9-b964086e95e2
CLIPS: 1:a1ffa785-d605-4fb0-bacf-c38d6abed9c4 2:286476a6-5971-4775-b5cc-6fe7d1cdda2a 3:703a39e0-d83c-4846-a712-9ac3de8dd3d7 4:a3df87d3-ff45-4dde-abc9-95c1d556677e
AUDIO: 1:e0fc3cf8-f6b0-422e-8231-840397d1db34 2:88fc34f8-0eda-4c62-a1b7-b975fb756325 3:41b61f56-7281-493f-9551-9c4c99ebd27d 4:6d543c49-1d65-4292-b88e-5ff7f382701d
A1 PRODUCTION COMPLETE (submitted). Pending completion check + assembly.

## B3 — Why Did Molasses Outrun People Through Boston? (re-cut from Molasses Flood longform blocks, per synergy note)
VISUALS (reused from molasses-flood-production-blocks.md, no new stills/clips generated):
  1: block30 clip 68b3995d-a275-4ca5-bc05-d9b28a0cbe39 (full wave bursting)
  2: block28 clip baf0bff0-1a60-4894-8149-3c1eaa99fbc4 (rivets popping)
  3: block33 real composite media 6e40538a-098a-47bf-8b81-d8e1ba40a527 (real aftermath photo)
  4: block50 clip 7e1ee2f5-fb27-46e7-ba35-a4daa65c20a8 (engineer stamping blueprint) -- verify completion before assembly
AUDIO (new, condensed short script wording): 1:b6363ca3-d4f7-42d0-8bc8-7a36d6fc07c9 2:afd2f2ac-579e-41e8-b61a-1029726469c7 3:c364f4c8-3be7-491c-a130-af52f38e47d3 4:52da5aef-8e8d-447b-bba5-0e0e8fe5e476

## ASSEMBLY
A1: 77f84dbe-ee41-469a-858d-4b92b37d280e (1080x1920, final)
B3: a040e033-0809-44e7-bd7c-958a526d6a94 (1920x1080, needs local vertical conversion after)

## B3 AUDIO FIX (user-reported: first few words immediately repeated in block 1)
Root cause: original block1 audio (b6363ca3, 11.0s) and two regeneration attempts (760599d9 13.1s,
3c191b4b 12.3s) all ran anomalously long with a repeated-phrase pattern visible in the waveform --
consistent with "In nineteen nineteen" (immediate word repetition) landing as the literal first
words spoken, a known TTS repeat-loop trigger. Fixed by rewording (same meaning, year moved
mid-sentence): "A wave of molasses moved through Boston in nineteen nineteen at thirty-five miles
per hour. People could not outrun it." New audio: dffa4ecb-a7a4-4d83-9c30-1be487a21a4b (7.47s,
natural duration, clean waveform, no repeat pattern).
Re-assembled: 36cd5d44-301b-48ed-8481-0a66523257a1 (1920x1080) -> local vertical conversion ->
shorts/series-b-episode-3/molasses-teaser.mp4 (40.02s, 1080x1920)

## B1 — Why Did Napoleon Retreat From Rabbits? (TEST: Seedream 5.0 Pro stills + Seedance 2.0 video, cinematic photoreal style, vs nano_banana_pro/kling3_0_turbo painterly brand)
STYLE: "Cinematic film still, dramatic natural lighting, shallow depth of field, rich color grading,
photorealistic historical epic drama style, 35mm film grain" -- deliberate departure from the
established painterly brand for direct model/style comparison per user request.
Cost: 3 credits/still (vs 2 for nano_banana_pro) -- confirmed via transactions.
STILLS (seedream_v5_pro, 9:16, 2k): 1:c6fdd488-64b7-461a-b32f-7bf87887c071 2:706323a1-f238-4989-a159-d8b60008e34e 3:99c0f836-28bc-4d36-8637-aeb47a4d2a50 4:e9d9ab0c-1263-406b-ac30-7c17c4efacd5

VIDEO MODEL CORRECTION: user clarified "seeddream 2.0" meant Seedance 2.0 (ByteDance video model),
not Kling. Two kling3_0_turbo clips were started on blocks 1-2 before the correction landed --
those job IDs are abandoned/unused, not in the final cut.
CLIPS (seedance_2_0, 9:16, 1080p, std mode, genre=epic, duration=10s, generate_audio=false):
  1: ad6565fd-1c04-4336-819c-ff79cf9b9479 (Napoleon push-in)
  2: 0b16db0b-11ec-44c1-b2ae-90771f5048ac (soldiers/crates)
  3: 9b8e9b16-11d6-4400-ac6a-cd5d518bc6eb (wave approaching chateau) -- hit the "IN THE DARK" preset
     interception, retried literal with declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612
  4: 6839a151-54cc-4866-a577-be32f46b783c (carriage racing away)
Cost: 90 credits/clip std 1080p (vs 20 credits/clip for kling3_0_turbo) -- confirmed via get_cost
preflight. 4.5x the price of the established pipeline's video step.

AUDIO (seed_audio, Gideon preset) -- speech_rate correction turned out unreliable for this text:
  Block 1: rate=0 -> 12.745s, rate=24 -> 7.859s, rate=13 -> 7.363s (non-monotonic: a LOWER rate
    produced a SHORTER duration than a higher one). Kept rate=24 take (3eaa7a6a-fca1-420e-b869-
    4b916d92750b, 7.859s) as least-bad: under target pads with silence rather than the audible
    speedup an over-length take would get in explainer_video.
  Block 2: rate=0 -> 8.62s (used, 990cc73b-8f84-4bcf-b4fe-3cee35587c2a), rate=-12 -> 13.475s,
    rate=-3 -> 14.2145s (again non-monotonic: less-negative rate produced a LONGER duration).
    Kept the original rate=0 take -- both "corrections" made it worse.
  Block 3: 02958ec4-0aa7-4d68-8df0-4a1a46e32465, 9.435s (rate=0, within ~6% of target, no
    correction needed).
  Block 4: d637882a-6e44-4dbe-a3db-0815524838ca, 9.405s (rate=0, within ~6% of target, no
    correction needed).
  Lesson for pipeline/README.md: the speech_rate-to-duration relationship documented from the
  Molasses Flood calibration does not reliably transfer across different narration text -- it can
  be non-monotonic for a given line. Treat it as a rough nudge to retry once, not a formula to
  solve for an exact target; if two attempts don't converge, keep whichever take errs under the
  target rather than over it.

## B1 REDO — clearer script + hybrid Narrative/Data-Explainer visuals (per user feedback)

User feedback on the original cut: "not completely sure... story needs to be more clear,
sometimes hard to follow, more boring... needs to be more clear and prioritize entertainment +
education." Diagnosis: the actual explanatory beat (wild vs. farm-raised rabbit behavior) was
crammed into dense narration with no dedicated visual -- the exact gap the Vox-style plan
(`scripts/vox-style-production-plan.md`) identifies as a Data-Explainer scene.

NEW SCRIPT (clearer beat structure: hook -> setup -> mechanism -> punchline):
  1. "This is Napoleon. He conquered nearly all of Europe. In eighteen oh seven, in open
     country, he was defeated by rabbits."
  2. "His own staff planned the day as a triumph: a celebratory hunt. They gathered thousands
     of rabbits and let them loose for him to shoot."
  3. "Here's the problem. Wild rabbits run from people. These rabbits were farm raised. To
     them, a person meant food was coming."
  4. "The moment the cages opened, the entire horde charged the Emperor of Europe. He fled to
     his carriage. The rabbits held the field."
Cut vs. original: dropped the "This detail matters" narration crutch (telling the viewer to pay
attention instead of earning it visually) and gave the wild/farm mechanism -- the actual joke
engine -- its own dedicated beat instead of compressing it alongside the charge/retreat action.

VOICE: Cillian (d8ba9f14-8a24-44db-932b-99e16c45bd32), replacing Gideon per user's pick from the
4-way comparison. All 4 takes came back clean on the first try, no speech_rate correction needed:
  1: e17dd99e-4f04-4065-850d-b64a37b73a53 (7.61s) 2: 8eb9c4fe-24b3-49b9-a9d7-b3110d31a215 (8.43s)
  3: 901bb1cf-c802-49b1-b342-5d055e521137 (8.43s) 4: c9767ef0-325e-4ecd-8003-9a2c75689ad5 (10.60s)

VISUALS -- hybrid Narrative + Data-Explainer, first real use of the new scene taxonomy:
  Blocks 1, 2, 4: kept the existing Seedream/Seedance narrative clips (still fit the new script's
  hook/setup/punchline beats) -- ad6565fd-1c04-4336-819c-ff79cf9b9479, 0b16db0b-11ec-44c1-b2ae-
  90771f5048ac, 6839a151-54cc-4866-a577-be32f46b783c. No regeneration needed, saved ~270 credits.
  Block 3 (new Data-Explainer beat): `recraft_v4_1` vector-mode graphic, brand-safe prompt (no
  "Vox" wording, per the plan's rule) -- a rabbit calmly hand-fed beside a food bowl, labeled
  "RAISED ON FARMS. FED BY HAND EVERY DAY." First attempt (33f19187) was a two-panel wild-vs-farm
  arrow comparison, but both arrows rendered pointing the same direction -- the model couldn't
  reliably encode "runs away" vs. "runs toward" via arrow direction, which would have made the
  beat more confusing, not less. Simplified to one clear image with no directional encoding
  needed. Turned into a 10s clip locally via `pipeline/compositing.py`'s `ken_burns_clip()` (free
  -- no paid AI video generation for this beat, per the plan's cost model): padded the square
  graphic onto a 1080x1920 off-white canvas, slow zoom 1.0->1.12. Uploaded via media_upload/
  media_confirm (media_id 9bbbea43-23f8-46b3-ad85-b4883c9ba17b) for use in explainer_video.
  Note for next time: the padded canvas leaves a lot of empty space above/below the square
  graphic on a 9:16 frame -- design future Data-Explainer graphics natively vertical instead of
  padding a square one.

ASSEMBLY: aeea21aa-6f63-47ed-9405-9849a428e864 (1080x1920, native, 40.02s) -> replaced
shorts/series-b-episode-1/napoleon-rabbits.mp4.

## B1 REBUILD 2 — researched hook/body/payoff structure + real motion graphics (per user feedback)

User was still unhappy after REDO 1: "the vox 'style' was just an added still basic drawing" and
"theres no clear structure, hook, explanation, conclusion" -- explicit instruction to research
what actually works for viral shorts in this niche and replicate it, rather than guessing.

RESEARCH (WebSearch/WebFetch, see chat for full findings):
- [The Shorts Retention Blueprint](https://virvid.ai/blog/shorts-retention-blueprint-ai-data-signals)
- [Looping Structure: The Hidden Retention Trick](https://virvid.ai/blog/looping-structure-shorts-retention-2026)
- [10 Viral Hook Templates](https://virvid.ai/blog/ai-shorts-script-hook-ultimate-guide-2026)
- [14 YouTube Shorts Hook Patterns](https://shorta.ai/blog/2026-01-04-youtube-shorts-hook-patterns)
- [Short-Form Video Structure: Hook, Body, Payoff](https://www.socialync.io/blog/short-form-video-structure-guide-2026)
Core structure that survived across all sources: Hook (1-3s, bold claim/contradiction/curiosity
gap, short sentences) -> Body (70-80%, escalating: setup then twist/mechanism) -> Payoff (10-20%,
resolves the hook's specific claim, ideally as a callback loop -- ending echoes the opening so the
viewer mentally rewatches, the single biggest retention lever documented across sources).

SCRIPT v3 (hook/body/payoff+loop, contradiction-hook per "everything you knew about X is wrong" /
bold-claim pattern):
  1. HOOK: "Napoleon Bonaparte never lost a battle in open country. Except once. Against rabbits."
  2. BODY/setup: "His own staff planned it as a triumph, a hunt to celebrate a treaty. Thousands
     of rabbits, released just for him to shoot."
  3. BODY/twist (Data-Explainer beat): "But these weren't wild rabbits. They had been raised by
     hand, fed by hand, every day. To them, a person didn't mean danger. It meant dinner."
  4. PAYOFF+LOOP: "The cages opened. The horde charged the Emperor of Europe. He fled to his
     carriage. His undefeated record in open country? Gone." (trimmed from a first take that ran
     29 words/12.745s -- callback deliberately echoes the hook's "never lost a battle in open
     country" claim, closing the loop.)

AUDIO (Cillian, all fresh takes): 1: f42992ca-6ee1-48ae-a4c7-fc85766744b6 (5.58s -- short punchy
hook, intentionally under the 10s block; the research explicitly wants hooks terse, not padded)
2: 8a024a71-9303-4c7f-8aa1-935954b9f410 (9.08s) 3: 7d108c04-9137-43f6-b924-58f7a3872683 (10.09s)
4: b8f9f003-58d2-4cfe-97b8-a629add07b2f (9.73s, after trimming the original 12.75s take -- see
pipeline/README.md, speech_rate correction proved non-monotonic/unreliable here, trimming the
line itself is what actually worked).

VISUALS: blocks 1/2/4 unchanged (still fit the new script's beats). Block 3 rebuilt from scratch
as genuine layered motion graphics instead of REDO 1's single static image + Ken Burns pan (the
thing the user correctly flagged as "just an added still basic drawing"):
- 3 separate transparent-background cutouts via recraft_v4_1 (`background_color: null`): a
  sitting rabbit (750ac293), a food bowl (74f976b8), a hand offering food (522f59b8). First
  two-panel wild-vs-farm comparison attempt (efcf0434) was scrapped in REDO 1 already for
  ambiguous arrow direction -- this time skipped that concept entirely in favor of one clear
  feeding scene assembled from separately animatable pieces.
- New `pipeline/compositing.py` function `layered_reveal_clip()`: each cutout fades/slides/scales
  in on its own timer (bowl 0.0-0.6s, rabbit pop-in 0.6-1.2s, hand slides in 1.3-1.9s, two text
  bands fade up at 2.1s and 4.3s), plus a continuous slow zoom (1.0->1.05) under everything so
  there's always some motion, not just discrete pops. Rendered 300 frames at 30fps, encoded via
  ffmpeg. Iterated composition twice (bowl felt disconnected from the rabbit group; food wasn't
  reaching the rabbit's mouth) by checking rendered test frames before committing to the full
  render -- final layout reads clearly as "rabbit being hand-fed beside its bowl."
  Uploaded as media_id 7d65cf4e-afda-4e17-a347-76b062c5d617.

ASSEMBLY: 0649658c-052c-42ad-94e0-73383c3e0316 (1080x1920, native, 40.02s) -> replaced
shorts/series-b-episode-1/napoleon-rabbits.mp4 again.
