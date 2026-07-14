# Iteration 4 — your six requests + the OOD-baseline literature search (v6 → v7)

## 1. Decoder description — CORRECTED (you were right, my draft was wrong)
Checked `data_utils_gpformer.py:176-187`. The decoder is **not** fed a learned start
token (that claim came from `REPORT.md`, which is inaccurate). It gets an
**Informer-style warm-up**: the **last `label_len = 6` CGM samples (30 min) of the
context**, concatenated with **12 zeros** as horizon placeholders. Decoder time-marks
cover all 18 positions, so the decoder sees the *calendar time* of the steps it must
predict but none of their glucose. Methods now states this and cites Informer.
(Minor correction to your recollection: it's the **last** 6 context steps, not the first.)

## 2. Four-institution deployment — ADDED, and the paper's claim UPGRADED
Added UCL / Manchester / Newcastle / Oxford to the FL system section. You confirmed the
runs genuinely executed there, so I upgraded the claim everywhere it was understating
itself: abstract, author summary, intro, discussion and **title** previously said "two
physically separate machines" / "prototype". Now: **"a four-institution deployment"**.
Remaining hedges are correctly scoped to *security* (plain HTTP, no secure aggregation)
and *cross-border jurisdiction*, not to scale. This is a materially stronger contribution
than the draft was claiming — arguably the first federated glucose-forecasting results
reported from a genuinely multi-institution run.

## 3. Tables — 5-seed variance added; ReplaceBG removed from held-in table
- `tab:main` is now **held-in only**, every cell `mean ± sd` over the 5 seeds.
- `tab:ood` now lists **all four single-cohort models individually** (reviewers had asked
  for this): three transfer fine (21.6-21.9 on ReplaceBG); only ARISES collapses
  (28.51 ± 6.85), and it does so on all three OOD cohorts.
- One number changed: Local-OOD mean on ReplaceBG was `23.54`; computed exactly from the
  four single models it is **23.45**. Now that all four are shown, it's verifiable.

## 4. Bolus table — ADDED (`tab:bolus`)
Δ = bolus − CGM. Federated: **+0.06 / +0.08 / +0.06** held-in (FedAvg/FedProx/MLDG) and
≤ +0.23 OOD — i.e. noise, slightly negative. Single-ARISES: **−1.65 / −0.44 / −1.18** on
the three OOD cohorts, with seed-sd roughly halved. Synthesis kept: bolus only rescues the
failure mode that federation already prevents, so it is redundant once federated.

## 5. **GPFormer is the direct antecedent — and it was uncited. FIXED.** ⚠️ IMPORTANT
The literature search surfaced **Zhu et al., IEEE JBHI 2024 (DOI 10.1109/JBHI.2024.3428921)**:
a Transformer using **MLDG for zero-shot glucose domain generalisation**, **CGM-only**,
developed on **REPLACE-BG**. It is called **GPFormer** — the same name as our codebase
(`FLockit_GPFormer`), i.e. **our forecaster is that architecture**.

The draft presented "MLDG for glucose forecasting" as if novel. That is not defensible and
a knowledgeable reviewer would have caught it. Fixed by:
- Citing GPFormer as **the architecture** in Methods ("we adopt its architecture unchanged").
- Adding a paragraph to the Introduction that credits GPFormer + GluLLM as prior
  *centralised* MLDG-for-glucose work, and repositions our contribution as: **what happens
  when that objective must be optimised without pooling**, across institutions that cannot
  exchange raw records. That contribution (federated, multi-cohort, head-to-head strategy
  benchmark, real 4-site deployment) survives intact — but it must be stated this way.

## 6. Zero-shot vs published baselines — STRONG result on ReplaceBG (`tab:oodprior`)
Two studies report RMSE@30 on ReplaceBG under **our exact protocol** (by-patient hold-out,
5-min grid, point error at 30 min). Our **zero-shot** MLDG lands *inside the pack of models
trained on the cohort*:

| model | trained on ReplaceBG | RMSE@30 |
|---|---|---|
| GPFormer | yes | 19.2 |
| GluLLM (＋insulin＋EHR) | yes | 20.6 |
| Crossformer | yes | 21.1 |
| N-BEATS | yes | 21.2 |
| TCN | yes | 21.3 |
| **Ours — MLDG (federated)** | **no** | **21.34** |
| Bi-LSTM | yes | 21.7 |
| GRU | yes | 22.1 |
| ARIMA / SVR | yes | 28.1 / 37.4 |

We beat several in-distribution deep baselines while never seeing the cohort and never
pooling data. The 2.1 mg/dL gap to GPFormer is the price of that constraint, and is smaller
than the spread among the in-distribution baselines.

**BrisT1D and Flair: no comparable published baseline exists** (BrisT1D's Kaggle task is a
60-min horizon in mmol/L; other BrisT1D papers report normalised-scale RMSE; Flair has zero
published forecasting baselines). Reported as **novel zero-shot reference points, not wins**.
Flagged that **Flair is a closed-loop (AID) cohort**, whose suppressed variability makes
forecasting easier — stated before a reviewer can.

Numbers deliberately NOT cited (untraceable to any primary source): a "15.16 mg/dL
meta-transfer" REPLACE-BG figure and an "8.5-9.8 mg/dL BrisT1D" figure. Also excluded
Jaloli & Cescon's 9.28 mg/dL (15-min grid + leaky rolling split) except as an example of
protocol heterogeneity.

Full evidence: `refcheck_ood_cohort_baselines.md`.
