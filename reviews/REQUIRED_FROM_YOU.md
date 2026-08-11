# Things I need from you — running list

You asked me to track this and chase you. Ticked items are resolved; open items block
specific claims in the paper. Ordered by what would sink the paper first.

---

## 🔴 OPEN — blocks a claim currently in the paper

| # | What I need | Why it matters / what it blocks |
|---|---|---|
| 1 | **Download the remote training LOGS for the 7 recovered seed_46 arms** (`apfl`, `decoupled`, `ditto_mu0.01/0.1/1.0`, `single_ABC4D`, `single_HUPA-UCM`) — the same place the outputs came from | You synced the seed_46 *outputs* (2026-08-11) and all 30-min tables are now full 5-seed and verified. But the 60-min numbers are parsed from training logs (`rmse_60=`), and the local logs for these 7 arms are empty stubs (the real runs happened remotely). Until the logs arrive, `tab:h60`'s Local cells (which need single_HUPA-UCM/ABC4D at 60 min) rest on 4 seeds while the caption says 5. With the logs I'll recompute those cells. |
| 4 | **Sanity-check the GPFormer framing** (Intro para + Methods) | GPFormer (Zhu 2024) already did Transformer+MLDG+zero-shot glucose DG. I reposition us as "same objective, but without pooling, across institutions." If that framing is wrong, a reviewer reads the paper as re-doing GPFormer. |
| 6 | **Author names, affiliations, corresponding email** | Still `Name1 Surname` / `correspondingauthor@institute.edu`. Corresponding author also needs an ORCID iD in the PLOS system. |
| 7 | **Data availability**: code repo DOI/URL, per-dataset access route + licence + accession, IRB/consent statement for secondary use | PLOS will not accept "available from the authors." Desk-reject risk. |
| 8 | **ARISES citation author list** (I added Zhu et al., npj Digit Med 2022, DOI 10.1038/s41746-022-00626-5); and **ABC4D**: registry (NCT02053051) or a journal paper? | I could confirm the DOI/trial but not the full author order. |

## 🟡 OPEN — decisions, not blockers

| # | Decision | My recommendation |
|---|---|---|
| 10 | Include **GPFormer's reciprocal data point** — it scores 22.9 zero-shot on ABC4D, one of *our* training cohorts (we get 19.68 held-in) | Nice symmetry (they transfer into our cohort, we transfer into theirs). Your call. |
| 12 | **Add the centralised-pooling baseline to the paper?** Phase F was re-run convergence-matched (50k steps, 5 seeds; NEW_FINDINGS.md). Story it supports: FL ≈ centralised pooling held-in *and* OOD, so federation costs almost nothing vs pooling — and FL→finetune beats both centralised and from-scratch on every OOD target. | **Include.** Reviewers routinely ask "why not just pool?"; we now have the clean answer and it strengthens, not weakens, the FL story. One table or two sentences + a table would do it. |

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
