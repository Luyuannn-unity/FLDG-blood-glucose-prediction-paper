# Things I need from you — running list

You asked me to track this and chase you. Ticked items are resolved; open items block
specific claims in the paper. Ordered by what would sink the paper first.

---

## 🔴 OPEN — blocks a claim currently in the paper

| # | What I need | Why it matters / what it blocks |
|---|---|---|
| ~~1~~ | ~~seed_46 outputs + logs~~ | **FULLY RESOLVED 2026-08-11.** Outputs and remote logs both synced. Every table (30-min and 60-min) is now full 5-seed, recomputed and verified; log-vs-CSV cross-check confirms the logs belong to the same runs. |
| ~~4~~ | ~~GPFormer framing~~ | **RESOLVED 2026-08-11 (author decision): precursor framing removed entirely.** GPFormer is no longer presented as our starting point. It remains in exactly three roles: (a) an unnamed Intro citation motivating the gap ("centralised MLDG glucose DG exists"); (b) "as in GPFormer" on the decoder time-of-day-token convention (Methods); (c) an external comparator in the comparison subsection and `tab:oodprior` (kept — deleting the best published ReplaceBG row while keeping its sibling rows from the same source would read as hiding the closest competitor). This also closes old item 10 (reciprocal data point: no). |
| 6 | **Author names, affiliations, corresponding email** | Still `Name1 Surname` / `correspondingauthor@institute.edu`. Corresponding author also needs an ORCID iD in the PLOS system. |
| 7 | **Data availability — remaining gaps**: (a) ideally mint a **Zenodo DOI** for the code repo; (b) accession numbers/URLs for the public datasets (MetaboNet, ReplaceBG, BrisT1D, Flair); (c) access route + justification for the proprietary ABC4D and ARISES (PLOS scrutinises "proprietary" — name a data-access contact, not "on request"); (d) IRB/consent statement for secondary use | Code repo LIVE at `github.com/Luyuannn-unity/fldg-glucose` (pushed 2026-08-11, code-only, scanned first) with **MIT license** (copyright line says "The fldg-glucose authors" — swap in real names when de-anonymising). Paper cites the real URL. |
| 8 | **ARISES citation author list** (I added Zhu et al., npj Digit Med 2022, DOI 10.1038/s41746-022-00626-5); and **ABC4D**: registry (NCT02053051) or a journal paper? | I could confirm the DOI/trial but not the full author order. |

## 🟡 OPEN — decisions, not blockers

| # | Decision | My recommendation |
|---|---|---|
| ~~12~~ | ~~Centralised baseline in paper~~ | **DONE 2026-08-11** (author decided include). Methods reference paragraph, rows in tab:main + tab:ood, Results paragraph, Discussion sentence; old limitation (viii) rewritten, future-work clause dropped. Framed as "centralised (pooled) reference", not "upper bound" (empirically it isn't strict). ⚠️ One follow-up: **sync `output_centralized_shuffled/seed_*/best_model_local_test_irt.csv` (5 files) from the remote machine** — the paper's centralised numbers currently trace to the per-seed values in NEW_FINDINGS.md, not to CSVs on this disk. ⚠️ Second follow-up (added 2026-08-12): **no 60-minute centralised numbers exist anywhere** (NEW_FINDINGS Phase F records rmse@30 only). Table `tab:h60` now carries the PFL held-in rows (recovered from `rmse_60=` in the training logs) but has no centralised row. If the centralised run's training logs on the remote machine logged `rmse_60=`, sync them and we can complete the table; otherwise it stays FL+PFL+Local only. |

---

## 📌 DECIDED (author decisions on record — don't re-litigate)

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
  training logs (`flock_model_gpformer.py`; log line "MLDG enabled (second-order/
  higher) — n_support=1, n_query=1, inner_iters=1, trade_off=1.0, inner_lr=same as
  outer"). Batches split patient-disjoint ~50/50 by windows; inner step = one
  differentiable SGD step at 1e-4; outer loss = support loss at original weights +
  query loss at adapted weights (equal weight); second-order term retained; outer
  Adam state untouched by the inner step; fallback to a plain step never fired
  (0 of 191,100 steps). Methods rewritten accordingly — the "released with the
  code" deferral is gone.
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
