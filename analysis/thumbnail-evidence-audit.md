# Thumbnail Style Correction — Evidence Audit

## What went wrong

Every thumbnail produced so far (Cadaver Synod's 3 variants, the 3 Shorts, the 9 existing-catalog refreshes) used a "dramatic painterly illustration + gold gradient distressed serif text with heavy black outline" style. **That style was never checked against real thumbnails from the niche's actual top performers.** All prior research (channel analysis, Shorts mechanics, long-form title analysis) was text-only — titles and view counts — and the visual thumbnail style was extrapolated from the video's own art direction and a generic assumption about "history channel thumbnails," not evidence. That's a real gap the user caught.

## What the actual top performers' thumbnails look like

Pulled directly from the highest-viewed videos identified in the long-form niche analysis:

| Channel / video | Views | Thumbnail text treatment |
|---|---|---|
| History Matters — "Why didn't Castro try to retake Guantanamo Bay?" | 2.1M | Flat clip-art-simple illustration; plain bold white sans-serif; no gradient, no heavy stroke; the full question restated as the thumbnail text |
| History Matters — "Why did France get so much of Africa?" | 1.2M | Same flat style, same plain white bold sans-serif |
| HistoryDose — "What A Pistol Duel Really Looked Like" | 1.6M | Painterly/cinematic background (closer to what we assumed); text is 3 words ("THE GRIM REALITY"), bold white sans-serif, thin/no outline — legibility comes from contrast against the sky, not from a heavy black stroke |
| HistoryDose — "First Battle in History: Egypt vs Canaanites" | 1.3M | Painterly illustration; text is 3 words ("THE FIRST BATTLE"), solid red bold sans-serif, thin black outline |
| Simple History — "Why all the F-14 Tomcats were Shredded" | 1.2M | **No text on the thumbnail at all** — illustration alone carries it |
| Bailey Sarian — Thanksgiving murders episode | 2.3M | Bold white sans-serif on solid-color banners (different genre, same typography finding) |

**Not one of these uses a gold gradient, a serif font, or a heavy distressed black outline.** That combination doesn't exist anywhere in the real data — it was invented, not observed.

## The consistent, evidence-backed pattern

- **Font: bold, clean sans-serif.** Never a serif/distressed/"historical-looking" font.
- **Fill: solid color** — white is most common, red or yellow as an accent. **Never a gradient.**
- **Outline: thin or none.** Legibility comes from placing text against a naturally high-contrast part of the image (dark sky, plain background), not from a thick black stroke doing all the work.
- **Text length: short.** 2–4 words typically, sometimes the full question restated in a plain block, but never elaborate.
- **Illustration/background style still varies** by channel and can be photoreal, painterly, or flat clip-art — that part of our original approach (varying visual style by topic/era) is unaffected by this correction and still stands.

## The corrected template

Rebuilt as `overlay_v2.py` in the production scratch tools: same idea as before (composite text locally rather than letting the AI bake it in, so it's pixel-consistent across every thumbnail) but with the corrected typography — Liberation Sans Bold, solid white fill, thin black stroke (~4px) purely for edge definition, drop shadow for lift, short 1–3 word lines, top-left aligned to match the two highest-performing real examples (History Matters, HistoryDose). Demonstrated on the Olof Palme thumbnail: "NEVER CONVICTED" over the existing noir background.

## Follow-up: local text compositing turned out to be unnecessary

Built a local PIL overlay (background generated text-free, typography composited in code) as the guaranteed-consistent fix, reasoning that AI-rendered text can't be pixel-identical across separate generations. Tested it head-to-head against just re-prompting Nano Banana Pro directly with the corrected simple style (explicit "plain bold white sans-serif, thin black outline only, no gradient, no serif" instruction instead of the old ornate description).

**The direct one-step generation won.** It rendered the text cleanly with no glitches, and composed the scene better than the manual version (subject walking toward camera with a visible face, text integrated into the open sky naturally, rather than a rigid fixed block). The original Palme text glitch wasn't a sign that AI text rendering is unreliable — it was a symptom of the wrong, more ambiguous style prompt (ornate gradient/serif) inviting more room for the model to improvise. A simple, explicit style instruction removes that risk.

**Revised production method:** single-step Nano Banana Pro generation with a locked prompt template (scene description + explicit plain-sans-serif/no-gradient/thin-outline instruction + 1–3 word text), no local overlay step by default. Keep the overlay script (`overlay_v2.py`) in reserve only in case a large batch later shows visible font drift across images.

## Outstanding: everything shipped before this correction uses the wrong text style

This includes the Cadaver Synod thumbnail actually live on the channel right now, the 3 posted Shorts, and the 9 catalog-refresh images delivered earlier in this session. None are broken or unusable, but none match the evidence-backed pattern above. Regenerating them now means: one Nano Banana Pro generation each with the corrected prompt template (~2 credits, no separate overlay step needed). Scope/priority is a budget call for the user.
