# Review — Reviewer 1 (clinical diabetes / digital health / medical decision-support)

**Manuscript:** "Federated and meta-learned blood-glucose forecasting across sites: a domain-generalisation benchmark and a cross-country deployment"
**Journal:** PLOS Digital Health

---

## 1. Recommendation

**Major revision.**

The paper addresses a genuinely important and clinically resonant problem: short-horizon CGM forecasters that are accurate on their training cohort but transfer poorly to new populations, together with the regulatory reality that the diverse data which would fix this cannot be pooled. The federated-learning framing is apt, the by-patient (rather than by-time) evaluation protocol is a real methodological strength that most prior work on these cohorts does not attempt, and the head-to-head comparison of FedAvg/FedProx/MLDG/APFL/Ditto with a clean held-in vs. out-of-distribution (OOD) separation is a useful contribution. The from-scratch cross-machine deployment is a nice feasibility demonstration.

However, from a clinical decision-support standpoint the manuscript is not yet publishable in its current form, for three linked reasons. First, the **entire clinical case rests on a single aggregate metric (RMSE@30 in mg/dL)** with no clinical error grid (Clarke/Parkes), no MARD, no hypo-/hyperglycaemia detection performance, and no uncertainty quantification — so the reader cannot tell whether the model is safe where safety matters (the hypoglycaemic range). Notably, essentially every benchmark paper the authors themselves cite (GlucoFM-Bench, Kolev, Manchanda, Tan & McBeth) reports a clinical error grid or MARD; this manuscript is a step behind field norms. Second, the **headline effect sizes are very small relative to CGM sensor noise and seed variance** (a ~2 mg/dL OOD gain, a ~0.4 mg/dL finetuning gain), yet the language ("robustness guarantee", "transferred safely", "never collapsed") is far stronger than n=1 OOD cohort and 4–5 seeds can support. Third, the "deployable by a small clinical consortium" claim is undercut by a **plain-HTTP, no-encryption, no-secure-aggregation, no-differential-privacy** system exchanging model weights over the public internet — which for real PHI is a safety/governance problem, not a selling point. I also found **numerical inconsistencies** between the manuscript and the supplied results files that must be reconciled before the results can be trusted.

None of these is fatal; the study design is sound and the honest by-patient framing is commendable. But the clinical metrics, the hedging, and the data/ethics statement all need substantial work.

---

## 2. Major concerns

### M1. RMSE@30 alone is not a sufficient clinical endpoint — report a clinical error grid, MARD, and hypo/hyperglycaemia detection.

The manuscript motivates the work in explicitly clinical terms — a forecast can "trigger preemptive alerts, inform bolus and snack decisions, and close the loop in automated insulin-delivery systems" (Introduction) — but then evaluates only "root-mean-squared error (RMSE) in mg/dL at the 30-minute and 60-minute horizons" (Evaluation protocol and metrics). Population-averaged RMSE is dominated by the euglycaemic bulk of the data and is close to blind to the clinically decisive tails. A model can post an excellent RMSE while systematically under-predicting rapid drops into hypoglycaemia — the single most dangerous failure mode for the bolus/snack/closed-loop decisions the authors invoke.

This is especially glaring because the authors' own benchmark comparators report exactly the missing metrics: GlucoFM-Bench reports "Clarke/Surveillance Error Grid", Kolev reports "Clarke EG", Manchanda reports "Clarke EG", and Tan & McBeth report "MARD ... and DTS zone-A" (per `paper_summary.txt`). By reporting RMSE only, this paper is less clinically informative than the literature it benchmarks against.

**Requested additions (at least):**
- A **Clarke or Parkes (consensus) error-grid** analysis for the main global models (Local-mean, FedAvg, FedProx, MLDG) held-in and on ReplaceBG, reporting % in zones A+B vs. the clinically dangerous zones C/D/E.
- **Hypoglycaemia and hyperglycaemia event detection** at the 30-min horizon: sensitivity, specificity/false-alarm rate, and detection lead time for crossing <70 mg/dL and >180/>250 mg/dL. This is what determines whether the "preemptive alert" use case actually works.
- **MARD** and, ideally, error stratified by glycaemic range (e.g. <70, 70–180, >180 mg/dL), so the reader can see where the RMSE gain lives.
- The manuscript should then re-examine whether federation's advantage survives on these clinical metrics, or whether it is confined to aggregate RMSE.

### M2. The ~2 mg/dL OOD "improvement" is over-interpreted, and the local baseline it beats is an artefact of averaging in one collapsed model.

The abstract states federation "transferred substantially better out of it" and the Results claim FedAvg/MLDG "improve on the mean single-cohort model (23.54) by more than 2 mg/dL". Two problems.

(a) **Clinical magnitude.** A ~2 mg/dL difference in 30-min RMSE is well within CGM sensor error (Dexcom/Libre MARD ~8–10%, i.e. roughly 8–15 mg/dL at typical glucose levels) and is unlikely to change any clinical decision. The manuscript never contextualises the effect size against sensor noise or a minimal clinically important difference, so "substantially better" is not defensible as written.

(b) **The baseline is inflated by construction.** The 23.54 mg/dL "Local OOD" is the *mean of four single-cohort models*, and the underlying results (`RESULTS_arises_bolus.md`) show three of those four transfer perfectly well to ReplaceBG: single_HUPA-UCM 22.01, single_ABC4D 21.85, single_T1D-UOM2 21.67 — all within ~0.2–0.5 mg/dL of FedAvg (21.43)/MLDG (21.34). Only single_ARISES (the smallest, highest-glucose cohort) collapses. So the honest statement is not "federation beats local by 2 mg/dL" but "**three of four single-cohort models transfer fine; federation is insurance against accidentally deploying the one bad cohort's model.**" That is a narrower, more credible claim and the paper should be reframed around it. As written, presenting the mean-of-four (dragged down by one outlier) as *the* local baseline reads as a stacked comparison.

Please report the per-single-model OOD numbers in the main text/table (not only the mean), and temper the headline accordingly.

### M3. "Robustness guarantee" / "never collapsed" / "transferred safely" — the safety language vastly outruns the evidence (n=1 OOD cohort).

The word "guarantee" appears in the abstract ("a robustness guarantee against distribution shift") and as a Discussion subheading ("Federation as a robustness guarantee, not only an accuracy gain"). The Discussion further asserts "every global model we trained generalised to the unseen cohort, and none collapsed" and the abstract says the models "never collapsed on the unseen cohort." The Author summary claims "every federated model transferred safely."

This is a strong safety claim resting on **a single held-out cohort (ReplaceBG) and 4–5 seeds** — a fact the authors concede in Limitations ("Our strongest claim — robust OOD transfer — rests on a single held-out cohort"). One OOD cohort cannot establish a "guarantee" of anything, and "never" / "safely" are unsupported generalisations. ReplaceBG is moreover a fairly conventional adult US T1D cohort, so the *magnitude* of distribution shift being tested is itself modest — this is not a stress test against, e.g., paediatric, T2D, or a different device generation.

**Requested changes:**
- Remove "guarantee" and "safely" throughout; replace with hedged language ("was associated with more reliable transfer on the one held-out cohort tested").
- Either add **multiple OOD cohorts** (strongly preferred — a leave-one-cohort-out design over the five cohorts would give five OOD tests almost for free and would make the robustness claim genuinely defensible), or explicitly downgrade the claim to a single-cohort observation.
- The word "safe/safely" is a loaded clinical term and should not be used without the error-grid/hypo-detection evidence requested in M1.

### M4. Numerical inconsistencies between the manuscript and the supplied results — the key "collapse" statistic is not reproducible from the data files.

The manuscript's dramatic failure statistic is the ARISES-only model on ReplaceBG: "**28.51 ± 6.85**" (Results and Discussion). I cannot reconcile this with the underlying files:
- `RESULTS_arises_bolus.md` reports single_ARISES OOD = **26.86 ± 3.45** (5 seeds).
- `FLockit_GPFormer/REPORT.md` (3-seed, CGM-only) reports single_ARISES OOD = **31.8 ± 5.95**, and elsewhere "≈29".

Three different values for the single number the paper leans on hardest. The local-baseline OOD mean (manuscript 23.54) likewise cannot be recomputed cleanly from the per-model numbers in the results file (mean of 22.01/21.85/26.86/21.67 ≈ 23.10, not 23.54). Held-in cells also drift (e.g. ABC4D MLDG 19.68 in the manuscript vs 19.76 in `RESULTS_arises_bolus.md`; local ARISES 22.04 vs single_ARISES 21.94).

These are not cosmetic: the "catastrophic collapse" narrative and the "2 mg/dL" gap both depend on which numbers are correct. Please state precisely which run/seeds Table 2 is drawn from, ensure the manuscript, `RESULTS_arises_bolus.md`, and `REPORT.md` agree, and correct any transcription errors. (I note the results file the reviewer was given is headed "ARISES **Bolus**" yet appears to be used as the CGM-only source — clarify which is the CGM-only table of record.)

### M5. The finetuning "recipe" gain is clinically negligible and over-sold.

The Discussion presents finetuning as resolving the generalisation/personalisation tension "in favour of the foundation-then-adapt recipe," concluding a new centre gets "a personalised model that no single-cohort training could match." The actual numbers: finetuned 20.98–21.04 vs. from-scratch 21.38 vs. zero-shot MLDG 21.34 mg/dL. The finetuning-vs-scratch gap is **~0.4 mg/dL** and the finetuning-vs-zero-shot gap is **~0.3 mg/dL** — both far below CGM sensor error and only a few times the seed sd (0.04–0.09). This does not support a strong "two-stage protocol" recommendation.

Moreover the finetuning was done on **ReplaceBG's own 166 training patients** (per `REPORT.md`), which is a *large* cohort — not representative of the "small clinical consortium / new centre with one cohort" the paper targets. A clinically meaningful finetuning experiment would show a **data-efficiency curve** (RMSE vs. number of local patients / weeks of data), so a new clinic can see how much local data it needs. As written, the recipe's clinical plausibility is asserted, not demonstrated. Please add the data-efficiency analysis and temper the language.

### M6. No uncertainty quantification — a real gap for a decision-support tool.

The model is trained with MSE loss and emits a single point forecast ("predicts a single CGM channel ... trained with mean-squared-error (MSE) loss"). For the clinical use cases the paper claims (alerts, bolus decisions, closed loop), the clinician/algorithm needs to know *when to trust the prediction* — calibrated predictive uncertainty is arguably as important as the point estimate, and two of the authors' own comparators (Zhu et al.'s evidential FCNN; Tan & McBeth) are built entirely around this. Please either add predictive-uncertainty estimation and report calibration, or explicitly acknowledge in Limitations that the absence of uncertainty output limits clinical deployability. This should not be silently omitted from a decision-support paper.

### M7. The "deployable" security/privacy framing is clinically and legally under-considered.

The paper repeatedly frames the system as ready for a clinical consortium ("deployable by a small clinical consortium without dedicated infrastructure"; "compatible with data-protection regimes"). But the system communicates "over plain HTTP" and the authors concede "we do not add secure aggregation or differential privacy, and a determined adversary could in principle attack the exchanged updates." Model weights/updates are known to be vulnerable to inversion/membership-inference; transmitting them in clear text over the public internet between health institutions is not a configuration a real consortium's information-governance office would approve. GDPR/HIPAA compliance is asserted ("compatible with data-protection regimes that would otherwise forbid pooling") but not established — no DPIA, no encryption, no access control.

Please (a) stop presenting the current prototype as deployment-ready for PHI; reframe it as a *feasibility/architecture* demonstration; (b) move the security limitations out of a single Limitations sentence and into the Discussion where the deployment claims are made; and (c) soften "compatible with data-protection regimes" to a statement that the *no-raw-data-movement property is a necessary but not sufficient* step toward compliance.

### M8. Data-availability and ethics statement is incomplete and internally flagged as unfinished.

The "Data and ethics" section states "Code for the federated system and the analysis is available from the authors," and an author comment in the source ("add a public repository/DOI link and confirm each dataset's access route and licence before submission") confirms it is unfinished. PLOS journals require a compliant data-availability statement and generally do not accept "available from the authors." Specific gaps:
- No repository/DOI for code; no per-dataset access route, licence, or accession (Zenodo/NCT) for the five cohorts.
- ABC4D and ARISES are described as "publicly available" but are Imperial clinical-trial datasets (NCT02053051, NCT03643692); the access/licence route must be stated explicitly.
- The **patient counts do not match the source papers** — an author comment in the source notes HUPA-UCM 22 here vs 25 in Hidalgo et al., and T1D-UOM 14 here vs 17 (21 enrolled, 4 withdrew) in Alsuhaymi et al. The `REPORT.md` split (18/2/2 for HUPA-UCM = 22; 10/2/2 for T1D-UOM = 14) confirms a filtered subset was used but the **filtering/exclusion criterion is never stated**. Exclusions matter clinically (were low-wear-time or poor-quality traces dropped? that biases performance upward). State the exact inclusion/exclusion rule and reconcile the counts.
- No statement on IRB/ethics approval or consent provenance for the secondary use (even if "de-identified secondary data", PLOS expects an explicit statement).

---

## 3. Minor concerns

1. **Abstract is jargon-dense for a clinical/digital-health readership.** It front-loads "FedAvg, FedProx, meta-learning for domain generalisation (MLDG), and two personalised-FL methods (APFL, Ditto) ... second-order meta-gradient." A PLOS Digital Health clinical reader will not parse this. Lead with the clinical problem and finding; defer the method roster. The Author summary is much better calibrated — bring some of that plain-language framing into the abstract.

2. **"Clinically actionable 30-minute horizon" is asserted, not shown.** The paper never demonstrates a clinical action (alarm, dose change) benefiting from the forecast. Either cite evidence that 30-min forecasts change decisions/outcomes, or soften to "commonly used warning horizon."

3. **MLDG's superiority is within seed noise.** MLDG over FedAvg is ~0.09–0.14 mg/dL held-in and ~0.1 mg/dL OOD (results file), smaller than the per-cell sd. The Discussion partly concedes this ("the effect is real but modest") but the Results heading "MLDG is the strongest global strategy" and the abstract ("MLDG was the strongest deployable global strategy") overstate it. Add the significance testing the Limitations admit is missing, or downgrade "strongest" to "numerically best, within seed variation."

4. **60-minute horizon is promised but absent** ("We report the 30-minute horizon here and leave the 60-minute horizon to a fuller analysis"; a TODO remains in the source). The Methods say the model forecasts 60 min. A single-horizon paper is acceptable, but the 60-min claim in Methods/abstract should be removed if not reported, and the longer horizon is where clinical decisions actually get harder — its omission weakens the clinical case.

5. **Global normalisation constant.** CGM is normalised with a single global mean/sd (154.04 ± 61.00 mg/dL). For a genuinely new OOD site this statistic is unknown at deployment; clarify whether it is a fixed constant shipped with the model (fine) or leaks any OOD information, and confirm ReplaceBG statistics did not inform it.

6. **ReplaceBG dwarfs the training cohorts** (984,447 OOD test windows vs 126k–562k train). Note this asymmetry; OOD RMSE is effectively a ReplaceBG-population average and may not reflect a small clinic.

7. **Table 3 (external comparison) is appropriately hedged** ("Numbers are indicative, not head-to-head") — good. But bolding "Ours" in that table visually implies winning despite the caveat; consider un-bolding to avoid the impression of a head-to-head victory the text disclaims.

8. **Bolus variant** is correctly relegated to preliminary, but note the underlying signal (≈0.05 mg/dL, within seed sd per `REPORT.md`) is essentially null; consider dropping it from the main text or clearly labelling it null rather than "a small, consistent benefit."

9. **Population scope.** All five cohorts are adult T1D; the Limitations note this. Given the clinical framing, state up front (Introduction) that findings do not extend to paediatric or T2D populations, rather than only at the end.

---

## 4. Concrete, actionable suggestions

1. **Add a clinical-metrics table** (Clarke/Parkes zone %, MARD, hypo/hyper detection sensitivity/false-alarm/lead-time) alongside RMSE, held-in and OOD, for the four deployable global models. This single addition would do the most to make the paper clinically credible and would bring it in line with the comparator literature.

2. **Convert the single-OOD-cohort design into leave-one-cohort-out** across all five cohorts. This turns the central robustness claim from anecdote (n=1) into evidence (n=5) at modest compute cost and directly addresses M3.

3. **Report per-single-model OOD numbers in the main table** and reframe the benefit as "insurance against a bad-cohort model" rather than a 2 mg/dL average gain (M2).

4. **Add a finetuning data-efficiency curve** (RMSE vs. #local patients / weeks) so a new clinic can size the local-data requirement; this replaces the clinically negligible 0.4 mg/dL headline with an actually useful deployment guide (M5).

5. **Reconcile all numbers** across the manuscript, `RESULTS_arises_bolus.md`, and `REPORT.md`; state the exact seed set and run behind Table 2; fix the ARISES-collapse statistic (M4).

6. **Rewrite the safety language**: drop "guarantee", "safely", "never collapsed"; contextualise every effect size against CGM sensor error and seed sd; add the significance tests the Limitations already flag as missing.

7. **Reframe the system contribution** as a feasibility/architecture prototype, add a short "path to secure deployment" paragraph (TLS, secure aggregation, DP, governance), and stop implying regulatory compliance is already achieved (M7).

8. **Complete the data/ethics statement** to PLOS standards: code DOI, per-dataset accession/licence/access route, the patient-count reconciliation with an explicit inclusion/exclusion criterion, and an ethics/consent-provenance statement (M8).

9. **Add the promised FL-architecture figure** (an author TODO in the source) — a schematic of server/clients/OOD-test flow would greatly help the clinical reader.

10. **Consider adding predictive uncertainty**, or at minimum a Limitations paragraph explaining why a point-forecast-only model is a partial decision-support tool (M6).

---

*Overall: a well-motivated, honestly-designed study with a valuable by-patient protocol, held back for a clinical venue by single-metric evaluation, effect sizes that are small relative to noise but described in strong safety language, an incomplete ethics/data statement, and reproducibility gaps between the manuscript and its own results files. These are addressable in a major revision.*
