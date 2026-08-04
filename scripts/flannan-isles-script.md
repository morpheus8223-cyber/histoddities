# Next Longform Script — The Flannan Isles Lighthouse Mystery

Topic selected via evidenced research, not guesswork — see chat: our own catalog data
shows mystery/vanishing-declarative titles (Roanoke 5.8K views, Kaspar Hauser 3.5K)
outperform absurd-event titles (Emu War 322, Stray Dog War 350) by 10-15x. This story
matches Roanoke's exact shape (people vanish, no trace, real investigation) and stacks
a second proven mechanic — myth-correction — on top: the "eerie final log entry" most
retellings use for atmosphere appears to be a later embellishment, not real.

**Visual style — new direction for this video**: photoreal cinematic generation
(Seedream/Seedance tier, proven in the B1 short test), not the established Ashcan-
painterly look. Goal per user direction: "watching the events unfold in real time as
if we were there" — immersive POV/close-third camera language, a consistent recurring
character face across shots (matching the reference thumbnails' reused actor-like
identity) representing the keepers, real archival photos where they exist (the actual
lighthouse, real Northern Lighthouse Board documents/photos if sourceable), bold
high-contrast thumbnail text (red/yellow, heavy outline) replacing the current amber/
gold refined brand for this video. Test still (b2f85d4c) confirmed this style works.

**Thumbnail text — use AI text rendering, not manual compositing.** First pass used
PIL to composite text onto a generated still (the faux-condensed technique from the
Molasses thumbnails); user feedback: use AI for the text instead. Retested with
`nano_banana_pro` (called out specifically for strong text rendering) prompting the
scene AND the bold text together in one generation — result (24559b2f) is crisp,
correctly kerned, genuinely impact-style lettering, no manual compositing artifacts.
**This is now the standard approach for every thumbnail on this video and going
forward**: describe the full thumbnail (scene + exact text + placement) in a single
`nano_banana_pro` prompt rather than generating a clean plate and adding text after.

**Runtime target: 5-7 minutes**, down from the ~10 minute Molasses Flood length —
applies to this video and all future longforms. The 6-chapter structure below
should compress comfortably into that window; block count will be tuned down
accordingly at the production-blocks stage (roughly 30-42 blocks at 10s each vs.
Molasses Flood's 60, or fewer/longer blocks if using Seedance's up-to-15s range).

**Video style reference**: user provided a Drive folder of 3 reference videos
(`Pompeii_Volcano_2.mp4`, `venice_5min_doc_prob4.mp4`, `ocean_music.mp4`) — downloaded
and run through `video_analysis_create` for scene-by-scene breakdown, same method
used for the Vox and Bright Side research. Findings pending (analysis in progress).

## Titles (question-hook, our strongest proven mechanic)
1. **Why Did Three Lighthouse Keepers Vanish Without A Trace In 1900?** — my pick,
   direct match to the History Matters question-hook pattern that's the single
   strongest performer in the evidenced dataset.
2. The Lighthouse Where Three Men Disappeared Without A Trace (mystery-declarative,
   Roanoke's exact winning shape)
3. The Flannan Isles Logbook's Last Entry Wasn't What You Think (myth-correction)

---

## COLD OPEN (~15-20s, Narrative, immersive POV)
"December 1900. A remote island in the North Atlantic, seventeen miles from the
nearest shore. Three men are stationed at a lighthouse there, alone, for weeks at a
time. On the twenty-sixth of December, a relief ship arrives. The light is off. The
door is unlocked. The table is set for a meal no one finished. And all three men are
gone." (Visual: cold, immersive push-in on the lighthouse through fog/sea spray,
establishing the isolation before the mystery lands.)

## CHAPTER 1 — Three Men, One Rock (Narrative, character establishing)
**Hook:** "James Ducat had kept lighthouses for over twenty years. He wasn't new to
isolation, or to storms."
**Body:** "In 1900, Ducat was Principal Keeper at the Flannan Isles Lighthouse — a
station so remote it had only been operational for a year. His crew: Thomas Marshall,
the second assistant, and Donald McArthur, filling in for a keeper on leave. Three
men, one rock, weeks between supply visits."
**Button:** "None of them would leave that island alive — and no one would ever
prove why."
(Visual: photoreal reconstruction of the three men going about lighthouse duties —
lighting the lamp, checking instruments, the physical isolation of the rock itself.)

## CHAPTER 2 — The Light Goes Dark (Narrative, tension build)
**Hook:** "On the night of December 15th, a passing steamer noticed something wrong."
**Body:** "The Archtor sailed past Flannan Isles after dark and saw no light at all
— a serious problem, immediately reported once the ship reached port. But bad weather
delayed any response for eleven days. The relief ship Hesperus couldn't reach the
island until December 26th."
**Button:** "By the time anyone set foot on that rock again, whatever happened there
had already been over for nearly two weeks."
(Visual: the steamer passing in darkness, the dark lighthouse tower against a storm
sky — immersive POV from the ship's deck looking toward the unlit light.)

## CHAPTER 3 — What The Relief Keeper Found (Narrative + Archival if real photos exist)
**Hook:** "When Joseph Moore finally reached the lighthouse, nothing answered his
signal flare."
**Body:** "Inside: an overturned chair. A meal left half-eaten on the table. Clocks
that had stopped. The beds unmade. Two sets of oilskin coats were missing from their
hooks — the third keeper's coat was still there."
**Button:** "Whatever happened, at least one of the three men appears to have gone
outside without stopping to put on a coat, into North Atlantic weather in December."
(Visual: this is the emotional core of the episode — slow, quiet, immersive walkthrough
of the empty lighthouse interior, POV camera discovering each detail in sequence.)

## CHAPTER 4 — The Official Investigation (Data-Explainer: real inquiry findings)
**Hook:** "The Northern Lighthouse Board sent its own superintendent to find an answer.
He did — sort of."
**Body:** "Robert Muirhead, who had personally hired all three men, concluded it was
an accident: two keepers had gone to secure equipment near the island's west landing,
a dangerously exposed spot, and a freak wave swept them into the sea. The third,
he theorized, saw it happen and ran out after them without his coat — and was taken
by a second wave."
**Button:** "It's the most boring possible explanation for one of the eeriest
disappearances in maritime history. It's also the only one with actual physical
evidence behind it — the landing gear was found damaged, exactly where you'd expect
if a wave really did hit that spot."
(Visual: Data-Explainer beat — a simple map/diagram of the island showing the west
landing, the wave's path, matching our layered_reveal_clip() device.)

## CHAPTER 5 — The Legend vs. The Log (myth-correction — mechanic #2, stacked)
**Hook:** "If you've heard this story before, you've probably heard about a
terrifying final log entry. It's the best part of the legend. It's also not real."
**Body:** "Later poems and retellings describe entries about screaming wind and a
crew 'in fear' shortly before the vanishing. But researchers who've examined the
actual logbook found no such dramatic entries — the last real note, from December
13th, is routine. The most famous version of this mystery was written by a poet in
1912, not by the keepers themselves."
**Button:** "The true version doesn't need the embellishment. Three trained
professional men still vanished from a locked, orderly lighthouse, and the real
explanation is a guess — an educated one, but still a guess."
(Visual: side-by-side Data-Explainer showing the real routine log entry vs. the
famous fictionalized poem lines, making the correction visually explicit.)

## CHAPTER 6 — What The Rock Became (Archival/legacy)
**Hook:** "The Flannan Isles Lighthouse was automated in 1971. No keeper has lived
there since."
**Body:** "The mystery never got a confirmed answer, and by the time it could have,
there was no one left to ask. Today the lighthouse still stands, unmanned, its light
running on its own."
**Button:** "Three men went to keep a light burning for other sailors. In the end,
the light outlasted all three of them — running alone, the way they were found."
(Visual: real archival/modern photo of the actual automated lighthouse today if
sourceable via Wikimedia/NLB, slow pull-back.)

## OUTRO (~15s)
"That's the Flannan Isles mystery — the real version, not the poem. Subscribe to
HistOddities for more of history's true unsolved cases, and let us know in the
comments what you think actually happened out on that rock."

---

## Kling vs. Seedance 2.0 pricing (confirmed via get_cost preflight)

| Model | Resolution/mode | Cost/10s clip | Cost/sec |
|---|---|---|---|
| kling3_0_turbo | 1080p | 20 credits | 2.0 credits/s |
| seedance_2_0 | 720p, fast mode | 35 credits | 3.5 credits/s |
| seedance_2_0 | 1080p, std mode | 90 credits | 9.0 credits/s |
| seedance_2_0 | 4k, std mode | 220 credits | 22.0 credits/s |

Both scale linearly with duration (confirmed: Kling 5s = 10 credits, Seedance
1080p/std 5s = 45 credits). **Seedance 1080p/std is 4.5x Kling's price; Seedance 4k
is 11x.** For a 5-7 min video at ~30-40 blocks, full Seedance 1080p would run
~2,700-3,600 credits vs. ~600-800 for Kling — a meaningful budget decision, not a
rounding error. Recommend: Seedream stills (photoreal quality, 3 credits/still)
animated with Kling for most blocks, reserving Seedance for a handful of hero shots
if the budget allows, rather than Seedance throughout — pending your call.

## Production notes
- Fact base: Northern Lighthouse Board records, Robert Muirhead's official report,
  Wikipedia/History Hit/All That's Interesting cross-referenced (see chat sources).
  The 1912 poem is Wilfrid Wilson Gibson's "Flannan Isle" — real, citable, safe to
  name directly since it's the actual documented source of the "embellished log"
  legend, not a claim we're making up.
- Visual style pivot flagged above — recommend one test still (photoreal Seedream-
  tier character, period 1900 lighthouse-keeper dress) before committing to full
  production, mirroring the B1 short's single-test-still validation step.
- Chapter 4 and Chapter 5 are both natural Data-Explainer beats (map/wave diagram,
  log-entry side-by-side) — reuse `layered_reveal_clip()`.
- Not yet broken into 10s production blocks — script-level document, parallel to
  `molasses-flood-script.md`.
