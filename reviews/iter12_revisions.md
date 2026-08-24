# Iteration 12 (2026-08-24): corrected results from the clean retrain

Source of every new number: `C:\Users\luyua\Desktop\release_bundle\output_clean_retrain\`
(`final_results_summary.csv`, per-seed CSVs under `pod_results/`). Change summary
from the author: `../../CHANGES.md`. Session facts and decisions:
scratchpad `facts.md` (copied into this log where they matter).

## Why

Three data problems were found and fixed, and the whole experiment matrix was
rerun on seeds 42-46 (old set 42/43/44/46/47):

1. MetaboNet's HUPA-UCM arrives resampled from 15 to 5 min with dropouts bridged
   linearly and no flag (39% of the old test windows had invented data). Fixed by
   rebuilding HUPA-UCM and T1D-UOM with a splice rule (constant-slope or clamped
   runs > 60 min treated as missing, stretches < 280 samples dropped; kept 88% of
   train / 70% of test samples, same patient splits).
2. T1D-UOM's seven 15-min patients were flagged (`cgm_real=0`) but never masked.
   Training loss and validation model selection are now masked to real samples.
   Test metrics are unmasked.
3. ABC4D and ARISES timestamps were off by 1000x, so their time-of-day marks were
   garbage in every old run. Repaired.

The old headline "single-ARISES collapses OOD (28.5 +/- 6.9)" was an artefact of
fix 3. It is retired everywhere.

## What changed in the paper (batches, all exact-match scripts in the session scratchpad)

1. **Tables**: every cell of `tab:datasets` (HUPA-UCM and T1D-UOM rows), `tab:main`,
   `tab:ood`, `tab:finetune`, the Ours rows of `tab:prior` and `tab:oodprior`.
   `tab:h60` rebuilt as a full table (all four held-in cohorts for every strategy,
   OOD columns kept, Centralised row added, single-ARISES row removed, wrapped in
   `\resizebox`). Bold rule: lowest per column excluding centralised, ties both bold.
2. **Methods**: MetaboNet paragraph discloses the interpolated grid. New
   subsection "Data quality" (the three fixes as method, not history). Preprocessing
   paragraph rewritten (global constant for federated and centralised models,
   own-cohort statistics for single-cohort models, author confirmed). Masked MSE.
   Evaluation paragraph states the clean-test reporting standard and the paired
   test's scope. MLDG step count dropped, zero-fallback claim kept. Data
   availability mentions the cleaning scripts.
3. **Results**: held-in paragraph now says federation beats local training
   (MLDG -0.36, p=0.005, 5/5; FedAvg -0.18, p=0.015; FedProx n.s.; gain
   concentrated on HUPA-UCM, tie on ARISES). Collapse paragraph replaced by
   "MLDG best global model, federation beats the average single cohort, held-in
   accuracy does not predict transfer". 60-min paragraph updated. MLDG paragraph
   now reports significance (p=0.010 @30, 0.002 @60, 24 of 24 cells, FedAvg vs
   FedProx not ranked, p=0.06). Ditto: flat mu, personalisation buys nothing.
   Centralised: 0.09 gap n.s., exact tie at 60 min, level OOD, MLDG ahead on
   ReplaceBG at 60 min. Finetune: 0.3-0.5, all 5/5, eight of nine pairs
   significant (FedAvg on Flair p=0.12). Data efficiency: 10% holds on ReplaceBG
   (17 patients) and Flair (10 patients, ceiling, was wrongly 9), BrisT1D pulls
   ahead from about 30% (author decision on wording).
4. **Discussion**: principal findings, the reliability paragraph (now "gains
   in-domain and removes the need to pick a source cohort"), the personalisation
   paragraph (tension is gone), finetuning, meta-learning (strategy choice matters
   as much as federating at 30 min), implications, strengths, positioning (new
   numbers, HUPA-UCM harder-test-set caveat: same models score ~1.4 mg/dL lower on
   the public grid), zero-shot numbers, BrisT1D/Flair, limitations (i, ii, iii, vi,
   vii).
5. **Abstract, Author summary, Intro contribution 2** rewritten for the new story.
   Abstract <= 300 words, summary 197.
6. **Style pass** (author rule 2026-08-24): no semicolons and no em-dash asides in
   prose anywhere in the paper. 58 sentence edits. Numeric ranges written with `--`
   stay.
7. **Figure**: `figures/data_efficiency.pdf/.png` regenerated from the new per-seed
   CSVs by the new `figures/data_efficiency_fig.py`.

Pre-existing errors fixed on the way: "two of which also consume insulin" (only
GluLLM does); the CGM-alone claim was attached to the wrong cohorts (it applies to
ARISES and ABC4D vs Zhu et al.); "24-participant" BrisT1D vs the 15 used;
"all seven cohorts are adult" vs Flair's adolescents; tab:prior sd column now
filled on all four Ours rows.

## Decisions taken by the author this session

- Paper not published or preprinted, so the data fixes are Methods, not a corrigendum.
- The clean rerun was executed on cloud pods, not on the four-site federation. The
  author will rerun live on the four institutions, so every "run live over HTTP
  across four universities" sentence stays as is. Numbers will be swapped once
  more after that run.
- `tab:h60` full table with OOD columns and a Centralised row.
- Single-cohort OOD rows and the Local mean-of-four row: **decision deferred**
  (keep in `tab:ood` / move to S1 Table / drop). Text is written for "keep". The
  sentences that depend on it: Results OOD paragraph from "What the single-cohort
  rows add" to the end, tab:ood caption's single-cohort sentences, Discussion
  "Federation gains in-domain..." paragraph from "The second benefit" onwards,
  Methods line "For OOD we also report the mean over the four single-cohort models",
  Methods "Local-mean" in the OOD-scored list, `tab:h60` Local OOD cells.
- Subset sizes use the ceiling (10% of Flair = 10 patients, 70% of BrisT1D = 11).
- BrisT1D data-efficiency wording: "pulls ahead from about 30%", no caveat.
- Normalisation: federated and centralised use 154.04 +/- 61.00, singles use own
  cohort statistics.

## Still open

- Live four-institution rerun, then a final number swap (mechanical, the scripts
  in the scratchpad show the pattern).
- Single-cohort OOD rows decision (above).
- Confirm the BrisT1D source-study participant count if it is to be mentioned
  (the draft now says "15 patients in the release we use").
