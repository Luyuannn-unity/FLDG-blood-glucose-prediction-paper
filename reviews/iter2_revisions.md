# Iteration 2 — how we revised v2 → v3

Round-2 reviews: `iter2_editor_metareview.md` (Area Editor meta-review vs. round 1)
and `iter2_reviewer_fresh.md` (fresh reviewer, cold read). Both said the tone/framing
fixes from round 1 landed, but flagged one hard error, an over-hedge that overshot,
a coherence gap, and some over-softening that buried the contribution.

Tags: **[FIXED in v3]** / **[CAVEATED]** / **[→UNSURE]** (needs author input/data).

## Hard error — sign inversion (editor NEW-1, fresh 2.1) — [FIXED in v3]
- v2 said FedProx was "numerically lowest" (= best) in Results and Discussion; the
  table shows FedProx is the **worst** global strategy (OOD 21.57, held-in avg 20.28).
- Results: now "FedProx was numerically **weakest** of the three global strategies
  here (highest RMSE both held-in and OOD)... single untuned µ, not a tuned ranking."
- Discussion (finetuning): now "FedProx, numerically **weakest** zero-shot here, is
  numerically **best** after finetuning (20.98 mg/dL) --- a reversal..." (the correct,
  and more interesting, reading).

## Over-hedge that overshot (editor NEW-3, fresh) — [FIXED in v3]
- "statistically indistinguishable from one another" asserted a (non-)significance
  result with no test. Replaced everywhere (abstract, Results heading, Discussion)
  with "differ only within seed-to-seed variation," which the data support without a test.

## Coherence gap: MLDG spec vs "released code" (editor NEW-4) — [FIXED in v3]
- v2 deferred the MLDG update to "the released code" while the availability statement
  said code was only "available from the authors."
- Restored a compact inner/outer update description in Methods (inner step on
  meta-train, update by the post-step meta-test-loss gradient; exact inner-lr and
  optimiser-state handling "will be released with the code").
- Changed availability statement to "will be released in a public repository upon
  publication" (consistent). Exact repo DOI + dataset licences/IRB still [→UNSURE #13, #20].

## Residual absolute in Author summary (editor NEW-5) — [FIXED in v3]
- "whereas the federated models did not" → "did not, on the one held-out cohort we tested."

## Over-softening that buried the contribution (fresh §4) — [FIXED in v3]
- Abstract: added an explicit closing statement of the deliverable --- "a clean,
  by-patient, held-in-versus-OOD benchmark across four real T1D cohorts, together
  with a runnable cross-machine federation" --- and noted that almost all prior
  glucose FL is simulated. No longer ends on all-concessions.
- System: stated plainly it is a "working" system / "working artifact, not a
  simulation" (kept the security caveats, but only where they belong).
- Positioning subsection left factual; the "match under a harder split" point is now
  supported by the confident abstract framing. (Could push confidence further; see below.)

## Dangling bolus (fresh 2.4) — [FIXED in v3]
- Added a one-line Results result: adding the log-bolus channel changed RMSE@30 by
  < ~0.05 mg/dL on average (within seed noise, no consistent direction), so it is not
  promoted to a main result. (Consistent with REPORT.md; fewer seeds than main run.)

## Can't separate "federation" from "more diverse data" (fresh 2.2, editor) — [CAVEATED] + [→UNSURE #21]
- Added Limitation (viii): no pooled-central control, so the mechanism is "more diverse
  training data obtained under a privacy constraint," not the averaging algorithm itself.
- Flagged whether a centrally pooled baseline exists to add. [→UNSURE #21]

## Smaller fixes — [FIXED in v3]
- "Local ARISES accurate on its own patients (22.04)" reworded (22.04 is the worst
  held-in cohort; now "on par with federation on its own patients... hardest cohort").
- Held-in "avg" labelled **unweighted** (cohorts differ in size) in the table caption.
- Added a visible note that patient counts are post-filtering subsets (Table 1 caption);
  removed the long internal REVIEW comment (kept a short author NOTE pointing to UNSURE).

## Still open / deferred (acknowledged in-text, logged in UNSURE)
- **Untraceable numbers now more load-bearing** (editor NEW-2): the honest reframe puts
  more weight on the ARISES-collapse figure (28.51±6.85), which is the least traceable
  number. NOT changed (we won't invent data). Escalated in UNSURE #1–#3 — sourcing this
  is now the single highest-priority provenance item.
- Per-single-model OOD numbers in the table (editor punch-list 5): NOT added — I only
  have BOLUS per-single values, not CGM-only, so adding them would mix variants. [→UNSURE]
- Clinical metrics, LOCO, persistence baseline, significance test, data-efficiency
  sweep: legitimately DEFERRED-TO-DATA; acknowledged in Limitations + Future work.
- "meta-learned" in the title vs. MLDG being a neutral result (fresh 2.5): [→UNSURE #22]
  — title wording is the author's call.
