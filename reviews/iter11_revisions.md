# Iteration 11 — Introduction distillation (2026-08-13)

Scope: **Introduction only**, second round of the intro rework, responding to
the author's notes on iteration 10. No numbers changed anywhere.

## The author's notes, and what was done

1. **"A third family aligns client representations... we leave it to future
   work" — out of scope.** Sentence removed. ⚠️ This orphans four citations
   that appeared nowhere else in the paper: `li2021moon`, `fedcl2023`,
   `flda2023`, `fedadv2022`. They remain in `references.bib` (harmless,
   BibTeX prints only cited entries) but are no longer cited. Flagged to the
   author.
2. **Contribution 1 too methodological.** Cut from ~150 to ~85 words: dropped
   the strategy list (now "the six strategies above", pointing at the ¶6
   list), the "30 minutes is the alert horizon" aside, the "two choices make
   this a stricter test" framing, the by-time-split contrast, and the
   adult-T1D caveat sentence (covered by limitation (vii), line ~1245, and
   the datasets paragraph, line ~1220).
3. **Contribution 2:** "which is what turns the benchmark into usable
   deployment advice" → "providing a practical strategy for onboarding new
   sites" (author's wording). Also cut "reach, and exceed, local-only
   performance without a large local data-collection effort".
4. **Contribution 3:** the "What we do *not* claim..." disclaimer (no
   encryption / secure aggregation / DP, single country) removed from the
   intro. Still fully covered in Methods (~line 453) and Discussion
   (limitation (vi), ~lines 1241–1244), so the paper's honesty about this is
   intact — locked facts respected.
5. **¶2 ending** replaced with the author's sentence: "Robust generalisation
   therefore requires methods that can exploit diversity across available
   cohorts while remaining effective on populations not observed during
   training." ("little reason to generalise" gone.)
6. **Global 20–25% cut.** Achieved 27%: **1537 → 1118 words.** Per-paragraph
   distillation, dropping detail that Methods/Discussion explain:
   - ¶1: "microvascular and cardiovascular" → "long-term complications";
     CGM/TIR sentence compressed.
   - ¶2: model-history clause chain compressed; all nine citations kept.
   - ¶3: "needed corpus vs available silos" sentence cut (opener already
     says it); "let alone across borders" cut; "proximal regularisation /
     control-variate variance reduction" → "variants such as FedProx and
     SCAFFOLD".
   - ¶4: "differences widen across countries" cut; DG definition folded
     into the parenthetical (`zhou2022dgsurvey` moved onto it).
   - ¶5: "with insulin and electronic-health-record inputs" cut; "across
     several institutions that each hold a different cohort..." cut
     (implied by "without pooling").
   - ¶6: per-method motivation clauses cut (`chen2018fedmeta` and
     `fallah2020perfedavg` merged into one bracket).
   - ¶7: the restatement parenthetical after "Closing this gap" cut.
   - ¶8: "from the UVA/Padova simulator" cut; the "running a federation for
     real requires..." sentence halved.
   - ¶13: "four real institutions" → "real institutions"; light trim.

## Validation

- Intro word count 1537 → 1118 (−27%).
- All remaining `\cite` keys resolve; env balance OK; no labels/refs
  touched.
- Locked facts respected: GPFormer still an unnamed citation
  (`zhu2024gpformer`), `sun2025multicontinental` still cited, honest
  deployment caveats still in Methods + Discussion.

Snapshot: `revision/glucose_fl_paper_v26.tex`.
