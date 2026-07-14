# Area Editor meta-review — Round 2 (v2 revision)

**Manuscript:** *Federated and meta-learned blood-glucose forecasting across sites: a domain-generalisation benchmark and a cross-site deployment prototype*
**Venue:** PLOS Digital Health
**Editor assessment date:** 2026-07-07
**Files assessed:** v2 = `glucose_fl_paper_working.tex`; author change-log = `iter1_revisions.md`; source = `RESULTS_arises_bolus.md`, `FLockit_GPFormer/REPORT.md`; round-1 reviews = `iter1_reviewer{1,2,3}_*.md`

---

## 1. Overall verdict

**Heading toward acceptable on tone and framing, but not yet acceptable — and the revision has introduced one clear factual/contradiction error that must be fixed, plus a structural risk the authors should see.**

The rewrite is, on the whole, an honest and competent response to the round-1 consensus. The over-claiming that all three reviewers objected to has been substantially fixed: "guarantee", "safely", and "never collapsed" are gone; effect sizes are now contextualised against sensor error; the method ranking is downgraded to "within seed variation"; the system is reframed as a two-machine feasibility prototype; the title no longer says "cross-country"; and the privacy claim is softened to "necessary but not sufficient." These are genuine improvements and the paper now reads honestly.

Three things hold it back. **(a)** A revision-introduced error: in softening "FedProx is weakest," the authors wrote that FedProx is "numerically **lowest**" in both Results and Discussion — the exact opposite of Table 2, where FedProx is the worst (highest-RMSE) global strategy. This is a hard contradiction with the paper's own table and must be corrected. **(b)** The reframe around "insurance against the one bad cohort (ARISES)" is the right honest move, but it makes the paper's entire "so what" now rest almost entirely on the single ARISES-collapse number (28.51 ± 6.85) — which is the one number that is untraceable to any provided source file. The revision has thus concentrated more weight on the least verifiable statistic. **(c)** The data/ethics statement, the untraceable main table, and the significance testing are still open, and several of those legitimately need data or author input rather than text.

Recommendation: **one more revision** (major-to-moderate). The text-only fixes are quick; the data-dependent items should be honestly scoped, and the FedProx error fixed before anything else.

---

## 2. Round-1 concerns — status

Status codes: **RESOLVED** / **PARTIAL** / **NOT RESOLVED** / **DEFERRED-TO-DATA** (legitimately needs an experiment or author input the text cannot supply).

| # | Round-1 concern (reviewer) | Status | One-line justification (v2) |
|---|---|---|---|
| C1 | Over-claiming: "guarantee/safely/never collapsed" (R1-M3, R2-M8, R3-M3) | **RESOLVED** | Heading now "Federation buys **more reliable transfer**, not only an accuracy gain"; abstract "transferred **more reliably**"; Discussion explicitly "careful not to over-read one OOD cohort ... as a guarantee." |
| C2 | Reframe OOD benefit as "3/4 singles transfer fine; insurance vs one bad cohort" (R1-M2, R2-M1) | **PARTIAL** | Reframe done ("three of the four ... transferred to within roughly half a mg/dL ... Federation's value here is reduced tail risk, not a large mean gain"). But R1 asked for the **per-single OOD numbers in the table**; v2 gives only the prose "half a mg/dL," not the values (22.01/21.85/21.67) or an OOD SD column. |
| C3 | Method ranking not significant; align across sections (R1-min3, R2-M6, R3-M3) | **RESOLVED (text)** / DEFERRED (test) | Heading now "**statistically indistinguishable from one another**"; "We therefore do not claim MLDG is the best method." Abstract aligned. Actual paired test still not run (DEFERRED). |
| C4 | Untraceable numbers: 28.51±6.85 collapse and 23.54 local-OOD mean in no source (R1-M4, R2-M1, R3-M1/M2) | **NOT RESOLVED** (DEFERRED-TO-DATA) | Both numbers unchanged in v2 (Results + Discussion still quote 28.51±6.85 and 23.54). Known/logged; the CGM-only 5-seed source was never supplied. See NEW-2 — the reframe makes this worse in impact. |
| C5 | Main CGM-only table can't be traced to a source; finetuning numbers are bolus-variant (R3-M1/M6, R2-M1) | **NOT RESOLVED** | Table values (e.g. MLDG ABC4D 19.68 vs bolus 19.76) still differ from the only 5-seed file; finetuning numbers (20.98/21.04/21.04/21.38) still match the **bolus** file exactly while presented in a CGM-only narrative. Variant provenance still unstated. |
| C6 | MLDG under-specified; "reuses Adam state"; meta-split mismatched to evaluated shift (R2-M3) | **PARTIAL** | Mechanism caveat added and correct ("simulates cross-**patient** shift ... not the cross-**cohort** shift measured by the OOD test"). But equations/inner-lr deferred to "the released code" — code not yet released (see NEW-4). |
| C7 | APFL frozen-α; FedProx untuned µ (R2-M2) | **PARTIAL** (DEFERRED-TO-DATA) | Contradictory "α lr 0.1" removed; caveats added ("APFL mixing weight may not have moved far ... read as a lower bound"; FedProx "single untuned µ"). Underlying code fix / re-run still needed. |
| C8 | Privacy/deployment over-framed; "compatible with data-protection regimes" (R1-M7, R2-M8) | **RESOLVED** | Reframed as feasibility prototype; security caveats now in Discussion deployment paragraph; "keeping raw data in-house is a **necessary but not sufficient** condition for compliance." |
| C9 | Data/ethics statement incomplete; "available from the authors" (R1-M8) | **NOT RESOLVED** | Still "Code ... is available from the authors"; author TODO comment still in source (add repo/DOI, licences, FL figure). Not PLOS-compliant. Ethics sentence added ("de-identified secondary ... no new human-subjects data") is a partial improvement. |
| C10 | Patient counts disagree with source papers; state filtering rule (R1-M8, R2-min3, R3-min2) | **NOT RESOLVED** | Table still 22/25/12/14; a REVIEW comment flags the discrepancy but no explicit inclusion/exclusion criterion is stated in the text. |
| C11 | Clinical metrics: error grid, MARD, hypo/hyper detection, uncertainty (R1-M1, R1-M6) | **DEFERRED-TO-DATA** | Honestly acknowledged in Limitations (i) and Future work as "the most important gap for a clinical reading." Legitimately needs experiments. |
| C12 | Leave-one-cohort-out / multiple OOD cohorts (R1-M3, R2-M5) | **DEFERRED-TO-DATA** | Flagged as "the highest-value next experiment" in Limitations (ii). |
| C13 | No persistence / simple baseline (R2-M4) | **DEFERRED-TO-DATA** | Acknowledged in Limitations (iv) and Future work; not added. |
| C14 | Finetuning confounded, within noise, wrong regime (R1-M5, R2-M7) | **RESOLVED (text)** / DEFERRED (data) | Softened to "suggestive"; caveats added (ReplaceBG 166 patients "does not test the data-poor small-clinic regime"; from-scratch used same budget). Data-efficiency sweep deferred. |
| C15 | 60-min horizon promised but absent (R1-min4, R3-min5) | **RESOLVED** | Removed from abstract; Methods honestly states "the model forecasts to 60 minutes, but we defer the longer-horizon analysis to future work." |
| C16 | Global normalisation scope / OOD leakage (R1-min5, R2-min1, R3-min6) | **RESOLVED (asserted)** | Now "computed from the four training cohorts only — the held-out OOD cohort does not contribute to it." (Author flagged [UNSURE #17] to confirm — asserted, not yet verified.) |
| C17 | Bold "Ours" in external table misleading (R1-min7, R3-min3) | **RESOLVED** | `tab:prior` "Ours (MLDG, global)" rows are no longer bolded. |
| C18 | Abstract jargon-dense (R1-min1) | **RESOLVED** | Abstract now leads with the clinical problem; method roster deferred to mid-abstract. |
| C19 | Population scope stated only at end (R1-min9) | **RESOLVED** | Introduction now states "All cohorts are adult T1D populations, so our findings should not be assumed to extend to paediatric or type-2 diabetes." |
| C20 | Skipped seed 45 / irregular seed set; per-cell n (R2-min2, R3-M4) | **PARTIAL** | Disclosed ("42, 43, 44, 46, 47; seed 45 was not run"; 4-seed cells noted). *Why* 45 was skipped still unexplained; still no per-cell n column in the table. |
| C21 | Bolus variant null / preliminary (R1-min8, R2-min6) | **RESOLVED** | Described as "a preliminary sensitivity check ... rather than as a main result"; no bolus numbers promoted to the main text. |
| C22 | Novelty scoped honestly (R2-M9) | **RESOLVED** | Intro frames a "controlled domain-generalisation benchmark" (primary) + "run for real, not only simulated" (secondary); no new-algorithm claim. |

---

## 3. NEW issues introduced by the revision

**NEW-1 (must fix — internal contradiction with Table 2). "FedProx numerically lowest" is sign-inverted.**
In Table 2, FedProx is the **worst** global strategy in both regimes (held-in avg 20.28 vs FedAvg 20.09, MLDG 19.99; OOD 21.57 vs FedAvg 21.43, MLDG 21.34 — higher RMSE is worse). Yet the revision now states, twice, that FedProx is *lowest*:
- Results: *"FedProx was numerically **lowest** here but was run at a single untuned µ, so this is not a tuned ranking."*
- Discussion: *"the three global strategies converge once finetuned (FedProx, numerically **lowest zero-shot here**, is also numerically best after finetuning)."*

This is a botched softening: the change-log says "FedProx is weakest" was softened to "lowest here, untuned" — but in RMSE "lowest" means **best**, i.e. the opposite of "weakest." The Results paragraph now self-contradicts (it says MLDG is numerically lowest OOD *and* FedProx is numerically lowest). The Discussion parenthetical is half-wrong: FedProx is *not* lowest zero-shot (it is highest = 21.57), though it *is* lowest **after** finetuning (20.98). Fix: say FedProx was numerically **highest/weakest** zero-shot (untuned, so not a tuned ranking) but numerically best after finetuning — which is actually a more interesting observation and worth keeping once stated correctly.

**NEW-2 (structural risk the reframe created). The contribution now rests almost entirely on the one untraceable number.**
The honest reframe (C2) narrows the headline from "federation is ~2 mg/dL better" to "federation is insurance against the single cohort (ARISES) that collapses OOD." That is defensible — but it means the paper's entire "so what" now depends on the ARISES-collapse figure (28.51 ± 6.85), which is exactly the value that appears in **no** source file (bolus 26.86 ± 3.45; REPORT 31.8 ± 5.95). Before, the untraceable number was one of several supports; now it is *the* support. This raises, not lowers, the priority of sourcing that number to a named CGM-only 5-seed run. If the true collapse is milder (or the SD smaller), the "reduced tail risk" contribution weakens materially. The editor should require the provenance before acceptance.

**NEW-3 (over-hedge that is itself an unsupported claim). "Statistically indistinguishable" without a test.**
The abstract, the Results heading, and the Discussion now assert the federated strategies are *"statistically indistinguishable from one another,"* while the same paper states *"we ran no significance test."* A (non-)significance claim requires a test in either direction. This is over-hedging that overshoots into a second unsupported statistical statement. Fix: use "differences are within seed-to-seed variation" (which the text also says and which is defensible without a test), or run the paired test and then the phrase is earned.

**NEW-4 (coherence gap created by deferring detail to code that isn't released).**
The revision removed the MLDG update detail from Methods and now says the inner/outer update "is defined in the **released code**." But the Data-and-ethics section still says code is "available from the authors" (no repository/DOI, and the author TODO to add one is still present). So the paper points to a "released" artefact for its central method spec that, per its own availability statement, is not released. Either restore a compact inner/outer update spec (and inner-lr) to the text, or make the release real and cite it — currently the two statements are inconsistent.

**NEW-5 (minor, leftover absolute in the plain-language summary).**
Author summary: *"a model trained on one cohort alone sometimes failed badly on new patients, whereas the federated models **did not**."* This is a residual absolute of the kind the revision otherwise scrubbed; scope it to the one tested cohort ("...did not, on the one held-out cohort we tested") to match the hedging now used in the abstract and Discussion.

**Contradiction sweep (things I checked that are consistent):** abstract OOD range "≈21.3–21.6" matches table global rows; Discussion ARISES held-in 22.04 and Ditto-µ0.01 21.98 match the table; held-in averages (20.15/20.09/20.28/19.99) match; title ("cross-site ... prototype") matches the two-machine feasibility framing in abstract/intro/methods; zero-shot MLDG 21.34 cited in the finetuning paragraph matches the table. No further section-vs-section contradictions found beyond NEW-1.

---

## 4. Prioritised punch-list for the next revision

### A. Text-only fixes (should be done before re-review; fast)
1. **Fix NEW-1:** correct "FedProx numerically lowest" → "numerically highest/weakest (untuned)" in Results; fix the Discussion parenthetical to "numerically weakest zero-shot ... but numerically best after finetuning." (Hard contradiction with Table 2.)
2. **Fix NEW-3:** replace "statistically indistinguishable" with "within seed-to-seed variation" wherever it appears (abstract, Results heading, Discussion), unless a test is added.
3. **Fix NEW-4:** either restore the compact MLDG inner/outer update + inner-lr to Methods, or make "released code" a real, cited repository consistent with the data-availability statement.
4. **Fix NEW-5:** hedge the Author-summary "did not" to the single tested cohort.
5. **C2:** add the per-single-model OOD numbers (22.01 / 21.85 / 21.67 / ARISES) to the table or Results text, since the whole reframe hinges on them.
6. **C9/C10:** replace "available from the authors" with a repository/DOI plan and per-dataset access route/licence; state the explicit patient inclusion/exclusion criterion that produces 22/25/12/14 and reconcile with the source papers.
7. **C20:** add per-cell n to Table 2 and one line explaining why seed 45 was skipped.

### B. Provenance / bookkeeping (needs author's run artefacts, not new experiments)
8. **C4/C5 (highest priority given NEW-2):** name the exact CGM-only 5-seed run behind Table 2, supply per-seed CSVs, and reconcile the ARISES-collapse figure (28.51 ± 6.85) and local-OOD mean (23.54) to that run — or correct them. Confirm the finetuning numbers are CGM-only, not the bolus variant, or relabel them.
9. **C7:** verify in code whether APFL's α actually updated; if frozen, re-run or keep the "lower bound" caveat and say so explicitly.

### C. Needs new experiments / data (legitimately deferrable, but scope honestly)
10. **C11:** clinical metrics — Clarke/Parkes error grid, MARD, hypo/hyper event detection, predictive uncertainty. (The single most important gap for a clinical venue; currently a Limitation.)
11. **C12:** leave-one-cohort-out for ≥1 additional OOD estimate — directly de-risks the central claim now that it rests on one cohort (NEW-2).
12. **C13:** add a persistence + one simple learned baseline to every cell.
13. **C14:** finetuning data-efficiency sweep on a subsampled new site, with significance tests.
14. **C3:** paired significance test across the shared seeds (resolves NEW-3 properly).
