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

## B1 — Why Did Napoleon Retreat From Rabbits? (TEST: Seedream 5.0 Pro, cinematic photoreal style, vs nano_banana_pro painterly brand)
STYLE: "Cinematic film still, dramatic natural lighting, shallow depth of field, rich color grading,
photorealistic historical epic drama style, 35mm film grain" -- deliberate departure from the
established painterly brand for direct model/style comparison per user request.
Cost: 3 credits/still (vs 2 for nano_banana_pro) -- confirmed via transactions.
STILLS (seedream_v5_pro, 9:16, 2k): 1:c6fdd488-64b7-461a-b32f-7bf87887c071 2:706323a1-f238-4989-a159-d8b60008e34e 3:99c0f836-28bc-4d36-8637-aeb47a4d2a50 4:e9d9ab0c-1263-406b-ac30-7c17c4efacd5
