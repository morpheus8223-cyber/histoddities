# Next Longform Script — "7 True Historical Events That Sound Completely Made Up"

Format adapted from analyzing BRIGHT SIDE's compilation style (video_analysis_create
on "11 Mysterious Discoveries in Places They Shouldn't Be" — 46-scene breakdown,
see chat). Adopted: punchy declarative per-segment hooks, fact-dense body with hard
numbers, closing button line, a recurring connective device between segments.
**Deliberately not adopted**: Bright Side's uncritical "ancient mystery" framing on
segments like the Yonaguni formation or Quimbaya "airplane" artifacts, which lean on
unresolved pseudo-archaeology with little evidentiary backing — every fact below is
resolved, sourced history, presented with "this really happened" energy instead of
"unexplained mystery" energy, matching this channel's existing honesty standard
(hedged claims stay hedged, e.g. B1's "the story goes").

All 7 segments reuse fact bases already audited in `scripts/shorts-series-episode-scripts.md`
— no new research risk, and this doubles as the payoff video for A2/A3/A5/B1/B2/B4/B5's
pinned-comment teases once their shorts are live.

**Target runtime**: ~10-11 min (intro ~20s + 7 segments x ~80-90s).

## Title options
1. **7 True Historical Events That Sound Completely Made Up** (my pick — direct
   curiosity-gap hook, matches Bright Side's superlative-title pattern without
   overclaiming "mystery")
2. History's 7 Strangest True Stories (100% Real)
3. 7 Real Events Stranger Than Any Movie Script

## Recurring connective device (our version, not a copy of Bright Side's mascot)
Every segment opens on the same 2-shot beat: a slow globe rotation zooming into a
highlighted region/date-stamp (Data-Explainer scene type, built with `recraft_v4_1` +
`layered_reveal_clip()` — reuse the same brand-safe prompting rule: describe the
visual, never name a source channel), then cuts straight into the segment's opening
visual. This is the anchor that makes 7 unrelated stories read as one series instead
of a random grab-bag, without copying anyone's literal mascot/branding.

---

## INTRO (~20s)
**Hook (Narrative, cinematic wide shot montage of blocks to come):**
"Seven things you're about to hear happened. Not legend, not exaggeration — happened,
on record. A war that ended before breakfast. A wave that outran people through the
street. An emperor who lost a battle to farm animals. If any single one of these
appeared in a movie, you'd say the writer went too far."

---

## SEGMENT 1 — The Shortest War in Recorded History (Data-Explainer: date/duration stamp)
**Hook:** "The shortest war in recorded history lasted thirty-eight minutes, start to
finish. It began at two minutes past nine in the morning. By nine-forty, it was over."
**Body:** "August 27th, 1896, Zanzibar. The sultan died. His cousin Khalid seized the
palace without British approval, so Britain sent an ultimatum, then five warships.
Khalid had three thousand men, a handful of cannons, and one royal yacht."
**Button:** "The bombardment lasted thirty-eight minutes. The palace fell, the yacht
sank, and Khalid was in the German consulate before his breakfast would have gone cold."
Fact base: Anglo-Zanzibar War, Aug 27 1896, ~09:02-09:40, Sultan Khalid bin Barghash,
~500 defender casualties, fled to German consulate.

## SEGMENT 2 — The Wave That Outran People Through Boston (Archival: real photos exist)
**Hook:** "In 1919, a wave moved through a city street at thirty-five miles an hour.
It wasn't water. It was two point three million gallons of molasses."
**Body:** "A steel storage tank in Boston's North End split open. Witnesses said the
rivets popped like gunfire. The wave stood twenty-five feet tall, and it moved faster
than anyone nearby could run."
**Button:** "Twenty-one people died in molasses. The disaster is also the reason every
building you've ever entered had its structural calculations checked by a licensed
engineer before it was allowed to be built."
Fact base: Great Molasses Flood, Jan 15 1919, 2.3M gallons, ~35mph, 21 dead, led to
engineering certification laws. (Longform companion already exists — link/callback.)

## SEGMENT 3 — The Emperor Defeated by Rabbits (Narrative: no surviving photography)
**Hook:** "Napoleon Bonaparte conquered most of Europe. In 1807, in open country, he
lost a battle. To rabbits."
**Body:** "His own staff planned a celebratory hunt and gathered thousands of rabbits
to release for him to shoot. The problem: these weren't wild rabbits. They'd been
raised on farms, fed by hand every day. To them, a person meant dinner, not danger."
**Button:** "The cages opened. The horde charged the Emperor of Europe. He fled to
his carriage, and the rabbits held the field." (Reuses B1's rebuilt hook/payoff
structure and Data-Explainer mechanism beat almost verbatim — proven to work.)
Fact base: July 1807 hunt arranged by Berthier after Tilsit — script hedges with
"the story goes" per the original episode script's sourcing note.

## SEGMENT 4 — The Beer Flood That Drowned a London Slum (Archival: real event, documented)
**Hook:** "In 1814, a fifteen-foot wave tore through a London neighborhood. The wave
was made of beer."
**Body:** "A twenty-two-foot brewery vat ruptured and took the neighboring vats with
it — over three hundred thousand gallons of porter, released at once, straight into
the crowded slum of St Giles. It flattened two houses and killed eight people."
**Button:** "The court ruled it an act of God. The brewery didn't pay a penny — and
got its beer tax refunded on top of it."
Fact base: London Beer Flood, Oct 17 1814, Meux's Horse Shoe Brewery, ~320,000+
gallons, 8 dead, "Act of God" ruling, excise rebate granted.

## SEGMENT 5 — Every Whale in Britain Legally Belongs to the King (Data-Explainer: legal statute)
**Hook:** "If a whale washes up on a British beach today, it does not belong to
whoever found it. By law, it belongs to the King."
**Body:** "The law dates to 1324. Whales and sturgeon were declared 'royal fish' —
Crown property, no matter where they landed. The reasoning was simple: a beached
whale was floating wealth, oil and bone and meat, and the Crown wanted first claim."
**Button:** "The law is still in force. In 2004, a Welsh fisherman who caught a
sturgeon was formally investigated — for taking property that, on paper, belonged to
the Queen."
Fact base: Prerogativa Regis c. 1324, "royal fish"; 2004 Robert Davies sturgeon case
(investigated, no charges).

## SEGMENT 6 — When America Legally Required Pink Butter (Data-Explainer: legal/product history)
**Hook:** "In the 1880s, several American states passed a law requiring a food
product to be dyed bright pink. This was not a prank. It was margarine."
**Body:** "Margarine was new, cheap, and colored just like butter — and dairy farmers
were furious that sellers kept passing it off as the real thing. So state legislatures
struck back: if margarine couldn't look like butter, make it look ridiculous instead."
**Button:** "The Supreme Court struck the pink laws down in 1898. Margarine survived.
The dairy lobby, by most accounts, never really forgave it."
Fact base: state anti-margarine laws 1880s (Vermont, NH, WV pink-dye laws), Collins
v. New Hampshire (1898) struck down, federal Margarine Act 1886 taxed it.

## SEGMENT 7 — The King Who Banned Tennis (For Everyone But Himself) (Narrative/Archival mix)
**Hook:** "In 1541, England made a popular sport illegal. Unless you were rich. The
king who signed the law was, personally, an avid player of that exact sport."
**Body:** "Henry the Eighth's problem was national security: England's army depended
on longbowmen, and the law required commoners to practice archery weekly. But archery
was steadily losing to tennis, bowls, and dice — so Parliament simply banned the
competition, all of it, for anyone who wasn't wealthy enough to be exempt."
**Button:** "The Unlawful Games Act stayed on the books for three hundred years. The
king, naturally, kept his own private court. And his racquet."
Fact base: Unlawful Games Act 1541 (33 Hen. VIII c. 9), protecting archery practice;
largely repealed 1845; Henry VIII's Hampton Court tennis court.

---

## OUTRO (~15s)
"Seven true events. No exaggeration required — history did that part for us.
Subscribe to HistOddities for more of the odd side of history, and if one of these
seven deserves its own full episode, the comments decide which one."

## Production notes
- Runs the same three-path scene taxonomy from `scripts/vox-style-production-plan.md`
  per segment (tagged above): Narrative for staged/invented scenes, Archival for
  events with real surviving photography, Data-Explainer for legal/statistical beats
  — reuse `layered_reveal_clip()` for the latter, same as B1's rebuilt mechanism beat.
- Cillian narration throughout (default voice as of the B1 rebuild).
- Segments 2 and 3 (Molasses, Napoleon) already have produced assets to reuse/adapt
  from the Molasses Flood longform and B1 short — lowest-cost segments to produce.
- Not yet broken into 10s production blocks — this is the script-level document
  (parallel to `molasses-flood-script.md`); a `*-production-blocks.md` breakdown is
  the next step once a specific segment set/order is confirmed.
