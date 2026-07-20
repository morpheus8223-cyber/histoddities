# Long-Form Niche Analysis — July 2026

Data pulled from the /videos tabs (not Shorts) of five channels: Weird History, Simple History, HistoryDose, Bailey Sarian (Dark History), History Matters. ~150 videos sampled, ranked by lifetime views. Same caveat as the Shorts analysis: lifetime views aren't age-normalized, but the pattern consistency below is strong enough to act on.

## The headline finding: title formula consistency beats subscriber count

| Channel | Sample | View range | Consistency |
|---|---|---|---|
| **History Matters** | 30 videos | 365K – 2.1M | **Extremely tight** — 27 of 30 videos land 400K–2.1M |
| HistoryDose | 30 videos | 25K – 1.6M | Tight — most single-battle narratives land 200K–700K |
| Bailey Sarian | 30 videos | 25K – 2.4M | Wide — true-crime spikes to 2M+, "history" episodes cluster 700K–1.2M |
| Simple History | 30 videos | 20K – 1.2M | Moderate — shifted toward military-hardware content, 100K–250K typical |
| **Weird History** | 30 videos | 9.6K – 115K | **Weakest of the sample** — the niche's biggest brand (13M subs) now underperforms every peer channel per-video |

The single most surprising result: **Weird History, the dominant brand HistOddities is modeling itself on, has the weakest and least consistent long-form numbers in the entire sample.** Its own format may be cooling. History Matters — a channel most people in this niche haven't heard of — gets 5–20x the per-video performance with a far narrower, more repeatable formula.

## History Matters' formula (worth stealing outright)

Near every title follows: **"Why did/didn't [historical actor] [surprising action]?"** — always a question, always naming a specific real actor, always implying an unresolved tension.

- "Why didn't Castro try to retake Guantanamo Bay from America?" — 2.1M
- "Why did France get so much of Africa?" — 1.2M
- "Why didn't the US focus on Japan first in WW2?" — 1.1M
- "Why did China give up so much of Siberia to Russia?" — 1M
- "Was King John really such a bad king?" — 635K (myth-correction variant)

This is Mechanic 5 (question hook) from the Shorts analysis, but proven to scale losslessly to 8–12 minute long-form — something we hadn't confirmed before this pass. **The exact same title mechanic that wins Shorts wins long-form.** This should change how every HistOddities title gets written from here on, not just Shorts titles.

## HistoryDose's formula: the specific-conflict narrative

"[Side A] vs. [Side B]" or "The Battle of X": "The Russian vs. Native American War," "The Irish vs Viking Wars," "Queen Boudica's Brutal Revolt Against Rome." Two named forces, a real battle, big numbers in the description. Consistently 200K–1.6M. This is Mechanic 4 (hyper-specific detail) applied to a whole video rather than a single line.

## Bailey Sarian's formula: "the dark history of [thing you already love]"

Her true-crime episodes are a different niche, but her history-adjacent hits are directly transferable: "The Movie That Almost Killed Its Cast: The Dark History of The Wizard of Oz" (1.2M), "The Mysterious Cult Leader Who Inspired Jonestown" (845K), "The SHOCKING History Behind Exorcisms" (865K). Mechanic: attach an obscure/dark historical story to something the viewer already has affection for or cultural familiarity with. This is Weird History's own "The Real..." title pattern, just executed with more specificity.

## Where Weird History is losing ground

Its top recent videos are compilations stitched from old episodes (Timeline 1969, Oddities of the Victorian Era) rather than new single-topic stories — a sign the channel is coasting on its back catalog rather than producing fresh hooks. Its single-topic new uploads mostly land 15K–35K, a fraction of History Matters' or HistoryDose's per-video floor. **This is the gap HistOddities can exploit: the same curiosity-gap brand voice, married to History Matters' tighter question formula and HistoryDose's specific-numbers narrative discipline, aimed at a topic Weird History hasn't touched.**

## Topic selection criteria (applied below)

1. Not already covered by HistOddities' 18-video catalog or the Cadaver Synod script.
2. Fits a proven title mechanic (question-hook and/or hyper-specific-numbers).
3. Strong, thumbnail-able single visual moment (Mechanic 1: peak-moment-first still applies to long-form cold opens).
4. Well-documented enough for an honest Sources list (avoid conspiracy-tier topics without hedging).
5. Visually distinct from the Cadaver Synod's medieval-Rome palette, so the style choice is a deliberate fit to era/mood rather than a reused template.

## Topic chosen: The Great Molasses Flood (Boston, January 15, 1919)

**Why this one, over the runner-up (the 1962 Tanganyika Laughter Epidemic, held for a future video):**

- **Instant thumbnail:** a 25-foot wave of molasses burying a city block is one of the strongest single images available in the "weird disaster" category — stronger cold-open material than a crowd of laughing schoolgirls.
- **Numbers-driven title works immediately:** 2.3 million gallons, 35 mph, 21 dead, 150 injured — Mechanic 4 (hyper-specific detail) is built into the raw facts, no embellishment needed.
- **Pipeline synergy:** this story is already partially scripted as Shorts Series B, episode 3 ("Why Did Molasses Outrun People Through Boston?") — that short can now serve as a teaser/trailer for the long-form video instead of a stand-alone, exactly the shorts→longform promotion path from the strategy doc.
- **Sourcing is strong:** extensively documented (Stephen Puleo's *Dark Tide*, Boston Public Library archives, MIT engineering-failure case studies, contemporary court records from the 1925 negligence ruling) — an honest Sources line is easy.
- **Visually distinct from Cadaver Synod:** 1919 industrial Boston has nothing in common with 9th-century Rome. This is the reasoning for picking a different visual style below rather than reusing the medieval-oil-painting key.
- **Runner-up reserved:** Tanganyika Laughter Epidemic (1962) is a strong second pick — fresher (nobody in the sample has covered it), matches the question-hook formula ("Why Did A Laughing 'Disease' Shut Down Schools For Six Months?") — but needs more careful, respectful handling of a real community's history and softer sourcing (mostly secondary psychology literature). Good candidate for the video after next.

## Visual style: NOT the Cadaver Synod's medieval oil-painting key

The style should follow the era and mood, per your instruction. 1919 Boston is the first HistOddities topic to fall inside the photographic age — so instead of aged-oil-painting chiaroscuro, the pick is **early-20th-century American urban realism** (the "Ashcan School" painting tradition — John Sloan, George Bellows): visible brushy strokes, warm mustard/rust/brick palette, gritty tenement-and-harbor lighting, high figure-in-motion energy. It reads as "period-appropriate documentary painting" the same way the oil-painting key did for the papal story, but the palette and brushwork shift entirely — muddier, warmer, more industrial, less candlelit-gothic. Full style descriptor is in the script file below, ready to drop into a style-key generation call at production time.

## Full script

See `scripts/molasses-flood-script.md` — production-ready, same structure as the Cadaver Synod script (cold open → CTA → chaptered narrative → outro), with title options, thumbnail concept, style tokens, and sources.
