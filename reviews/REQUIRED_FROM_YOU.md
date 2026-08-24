# Things I need from you — running list

You asked me to track this and chase you. Ticked items are resolved; open items block
specific claims in the paper. Ordered by what would sink the paper first.

---

## 🔴 OPEN — added 2026-08-24 (clean-retrain revision)

| # | What I need | Why it matters / what it blocks |
|---|---|---|
| 13 | **Rerun the federated arms live on the four institutions**, then hand over the per-seed CSVs | The clean rerun (2026-08-21/22) ran on cloud pods through the sweep driver. Six sentences say the reported numbers came from the live four-site run (abstract, summary, intro contribution 3, principal findings, implications, strengths). You chose to keep them and rerun live. Until the live numbers exist those sentences are a promise, not a report. After the run: one more number swap (tables + the prose spots listed in `iter12_revisions.md`). |
| 14 | **Decide the single-cohort OOD rows**: keep in `tab:ood` (current), move to an S1 Table, or drop | Gates the last five sentences of the Results OOD paragraph, the single-cohort sentences of the `tab:ood` caption, the second half of the Discussion paragraph "Federation gains in-domain and removes the need to pick a source cohort", and two Methods clauses. My recommendation is S1 Table + one sentence. |
| 16 | **Single-cohort models: train/eval normalisation mismatch (found 2026-08-24 by the verification sweep, confirmed against the CSVs).** Every arm, including the four single-cohort models, was TRAINED with the shared constant 154.04 / 61.00 (`_configs/cgm_s42_single_*.yaml`, training logs). The reporting evaluation (`eval_extended.py`, driven by `run_contaminated_evals.py`, which deliberately matches "the same training-vs-eval stats quirk the old Phase D runs used") recomputes the constants from each arm's training dirs: pooled clean four-cohort stats for federated/centralised arms (152.18 / 61.09, immaterial: training-time and extended evals agree within 0.03) and each single cohort's OWN stats for the single-cohort arms (HUPA-UCM 136.29 / 52.36, ARISES 161.69 / 65.13). For seed 42 the same single-HUPA-UCM model scores 20.44 with the training constants (`cgm/seed_42/single_HUPA-UCM/best_model_local_test_irt.csv`) vs 20.99 reported; single-ARISES 21.71 vs 21.80; ABC4D and T1D-UOM within 0.1. | This inflates the local baseline on HUPA-UCM (and so the FL-vs-local gain, 1.00 on HUPA-UCM, 0.36 on average) and touches every single-cohort row held-in and OOD (tab:main Local row, tab:h60 Local row, tab:ood single-cohort rows and the Local mean, all "ARISES best / HUPA worst" sentences). **Recommended fix:** re-run the extended evaluation of the four single-cohort arms x 5 seeds with the training constants (eval only, no training; checkpoints for seed 42 are local, seeds 43-46 are on the pods), then swap the single-cohort numbers and the paired tests. Until then the Methods carry a `% NOTE (author)` at the normalisation sentence and say only that all models are trained with the shared constant. |
| 15 | **BrisT1D source-study participant count** | Limitation (ii) used to say "24-participant"; the release we use has 15 patients, so it now says "15 patients in the release we use". If you want the source count too, confirm it. |


## 🔴 OPEN — blocks a claim currently in the paper

| # | What I need | Why it matters / what it blocks |
|---|---|---|
| ~~1~~ | ~~seed_46 outputs + logs~~ | **FULLY RESOLVED 2026-08-11.** Outputs and remote logs both synced. Every table (30-min and 60-min) is now full 5-seed, recomputed and verified; log-vs-CSV cross-check confirms the logs belong to the same runs. |
| ~~4~~ | ~~GPFormer framing~~ | **RESOLVED 2026-08-11 (author decision): precursor framing removed entirely.** GPFormer is no longer presented as our starting point. It remains in exactly three roles: (a) an unnamed Intro citation motivating the gap ("centralised MLDG glucose DG exists"); (b) "as in GPFormer" on the decoder time-of-day-token convention (Methods); (c) an external comparator in the comparison subsection and `tab:oodprior` (kept — deleting the best published ReplaceBG row while keeping its sibling rows from the same source would read as hiding the closest competitor). This also closes old item 10 (reciprocal data point: no). |
| 6 | **Author block — remaining gaps**: (a) affiliations for Rui Sun (2) and Taiyu Zhu (3) — currently `[affiliation to be confirmed]`; (b) confirm "Rui Sun" name order (input read "Sun Rui"; PLOS wants First Last); (c) optional department for Manchester; (d) ORCID for the corresponding author (mandatory) + CRediT roles for all six, entered in the PLOS system | **Done 2026-08-11:** six authors inserted — Luyuan Qi¹, Paul Taylor¹, Rui Sun², Taiyu Zhu³, Simon Harper⁴, Kezhi Li¹* (corresponding, ken.li@ucl.ac.uk); ¹ Institute of Health Informatics, UCL; ⁴ University of Manchester. |
| 7 | **Data availability — remaining gaps**: (a) optionally mint a **Zenodo DOI** for the code repo; (b) accession numbers/URLs for the public datasets (MetaboNet, ReplaceBG, BrisT1D, Flair); (c) confirm the consent phrasing in the ethics sentence ("no participants were contacted") matches the LREC application | **Done 2026-08-11:** ethics statement added (UCL Institute of Health Informatics LREC, Project ID 1665, study title quoted); ABC4D/ARISES now "available upon request and approval" via Dr Kezhi Li (ken.li@ucl.ac.uk); code repo live at `github.com/Luyuannn-unity/fldg-glucose`, MIT-licensed, cited in the paper. |
| 8 | **ARISES citation author list** (I added Zhu et al., npj Digit Med 2022, DOI 10.1038/s41746-022-00626-5); and **ABC4D**: registry (NCT02053051) or a journal paper? | I could confirm the DOI/trial but not the full author order. |

## 🟡 OPEN — decisions, not blockers

| # | Decision | My recommendation |
|---|---|---|
| ~~12~~ | ~~Centralised baseline in paper~~ | **CLOSED 2026-08-24:** the clean retrain put the centralised per-seed CSVs on disk (`release_bundle/output_clean_retrain/pod_results/clean_eval/seed_*/centralized/extended_metrics.csv`) at 30 and 60 min, and `tab:h60` now carries a Centralised row. Earlier history: **DONE 2026-08-11** (author decided include). Methods reference paragraph, rows in tab:main + tab:ood, Results paragraph, Discussion sentence; old limitation (viii) rewritten, future-work clause dropped. Framed as "centralised (pooled) reference", not "upper bound" (empirically it isn't strict). ⚠️ One follow-up: **sync `output_centralized_shuffled/seed_*/best_model_local_test_irt.csv` (5 files) from the remote machine** — the paper's centralised numbers currently trace to the per-seed values in NEW_FINDINGS.md, not to CSVs on this disk. ⚠️ Second follow-up (added 2026-08-12): **no 60-minute centralised numbers exist anywhere** (NEW_FINDINGS Phase F records rmse@30 only). Table `tab:h60` now carries the PFL held-in rows (recovered from `rmse_60=` in the training logs) but has no centralised row. If the centralised run's training logs on the remote machine logged `rmse_60=`, sync them and we can complete the table; otherwise it stays FL+PFL+Local only. |

---

## 📌 DECIDED (author decisions on record — don't re-litigate)

- **2026-08-24, clean-retrain revision.** (a) Paper is unpublished, so the three
  data fixes are a Methods subsection ("Data quality"), not a corrigendum. (b) The
  "single-ARISES collapses OOD" result is retired (timestamp-bug artefact). (c)
  `tab:h60` is a full table with OOD columns and a Centralised row. (d) Local
  models normalise with their own cohort statistics; federated and centralised use
  154.04 ± 61.00. (e) MLDG step count dropped, zero-fallback claim kept. (f) Subset
  sizes use the ceiling: 10% of Flair = 10 patients. (g) BrisT1D data-efficiency
  wording: "pulls ahead from about 30%", no seed-noise caveat. (h) Style: simple
  sentences, no semicolons, no em-dash asides, paper-wide.

- **Persistence / clinical-metrics comparison (NEW_FINDINGS Phase D/E) will NOT be
  reported** (decided 2026-08-11). Rationale: the paper's claim is about RMSE under
  federation and transfer; the models were optimised for RMSE, not event detection,
  and reporting a metric family we did not optimise for would import a problem that
  is not the paper's focus. The Methods now justify RMSE@30 as the single primary
  metric (training objective + comparability + readability), and the Limitations
  already state that error-grid/MARD/event detection are not included.
- **Bolus is out** (decided 2026-08-11). The bolus input variant, its Results
  paragraph, and `tab:bolus` are removed from the working draft; the paper is now
  7 tables, CGM-only throughout. The only remaining "bolus" is the Intro's clinical
  phrase "inform bolus and snack decisions", which is about patient decisions.

## ✅ RESOLVED (answered by you)

- **MLDG update spec** (was item 2) — resolved from you + verified in code and the
  run configs (`gpformer_arises_bolus_alt.sh` generator sets
  `mldg_first_order=False`, `mldg_inner_reuse_outer_opt=True` → the
  `_train_step_mldg_ref` path). Batches split patient-disjoint ~50/50 by windows;
  **inner step = one differentiable step by a `higher` copy of the outer Adam**
  (reads its moment history and LR 1e-4, writes nothing back) — *not* plain SGD;
  the author's memory caught an earlier wrong "SGD inner step" wording, fixed
  2026-08-11. Outer loss = support loss at original weights + query loss at
  adapted weights (equal weight); second-order term retained; fallback to a plain
  step never fired (0 of 191,100 steps). Release code + configs ship the same
  variant.
- **Patient counts** (was item 5) — resolved: HUPA-UCM (22) and T1D-UOM (14) are the
  counts carried in MetaboNet's harmonised release, not our filtering. The Methods
  now say so and cite MetaboNet (which also settles old item 9 — it is cited as the
  data source, not as a comparator benchmark).
- **Loss function** — verified in logs: `Loss: MSE (single-head, c_out=1)`. The
  `quantile_loss` attribute in the code is a naming shim (MSELossAdapter when
  `proposer_loss_type='mse'`, which is what all paper runs used). Methods' "trained
  with MSE" claim is correct.

- **Normalisation constant is clean — NO OOD LEAK.** Confirmed by you and verified in the
  logs: `mean=154.04, std=61.00` is the *only* normalisation value used anywhere in the run
  backing the paper (`logs_gpformer_arises_bolus`, 1861 occurrences, no others). It is
  computed on the four training cohorts, and the held-out cohorts are scored under that same
  shipped constant — which is also the deployment-realistic setting. The Methods claim
  ("no OOD information enters preprocessing") is accurate as written.
  *(Red herring for the record: `mean=159.9, std=61.2` appears in `logs_gpformer_v1`, an
  obsolete April run — it is a descriptive log of BrisT1D's raw statistics at
  window-extraction time, not a normalisation being applied.)*
  ▸ Minor residual: I could not confirm which constant the **ReplaceBG-from-scratch** arm
  used. If it used ReplaceBG's own statistics, that would *advantage* the from-scratch
  baseline — making our finetuning win conservative rather than inflated. Worth a one-line
  check when you sync, but it cannot hurt the claim.

- **All OOD scoring is on held-out test patients only** (ReplaceBG = 21-patient split) — so zero-shot, from-scratch and finetuned arms share an identical per-cohort test set. Methods, tab:ood and tab:oodprior all now say this consistently. (Corrected an earlier draft error that claimed BrisT1D/Flair were scored on all patients.)
- **RMSE@30 is a point forecast**, not a window average. This is what makes the GPFormer/GluLLM comparison valid; stated in the table caption.
- **We use full attention, not GPFormer's sparse attention** — verified in code. Methods/Intro/comparison corrected; the gap to GPFormer now explicitly attributed to architecture *and* training regime.
- **APFL α is not frozen** — I checked `apfl_alpha_log.csv`: α decays 0.23 → 0.02–0.08 in every seed. Better than a "failure mode": APFL *learns* to deploy ~95% global model. Now a Results finding, and it supplies the missing explanation for the personalised-FL family.
- **Decoder** = Informer-style warm-up (last 6 context steps + 12 zeros), not a start token.
- **Deployment** = 4 real institutions (UCL/Manchester/Newcastle/Oxford). Claim upgraded throughout.
- **60-min horizon** = recovered from training logs (`rmse_60=`); no retrain was needed.

---

## ⚠️ Trap to avoid on the next run

**If you finetune on BrisT1D / Flair, you must recompute their zero-shot OOD numbers on the
reduced test split.** They are currently 100% test. The moment you carve out a finetuning
train split, the zero-shot / from-scratch / finetuned arms are no longer on the same test
set — which is precisely why ReplaceBG uses a 21-patient test split. Their OOD numbers will
shift slightly.

**Also: save checkpoints AND per-window predictions on the next run.** Clinical metrics
(Clarke/Parkes grid, MARD, hypo/hyper detection) cannot be computed from what is currently
on disk — only aggregate CSVs were kept. The 60-min numbers survived only by luck, because
someone logged them.
