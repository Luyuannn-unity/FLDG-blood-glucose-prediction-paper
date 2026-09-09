# iter14 — Clarke error grid added (2026-09-09)

Author request (2026-09-09): "make it a small section in the result section of
the paper, saying it's better in Clarke error grid too. Might need to change
some wordings of only reporting RMSE, and remove the limitation of not having
this grid." This reopens the 2026-08-11 decision for the Clarke grid only.
Persistence, MARD, Parkes and event detection stay unreported.

## Source of every number

`C:\Users\luyua\Desktop\release_bundle\output_clean_retrain\predictions\analysis\clarke\`
(`clarke_summary.csv` for the table, `contrasts.csv` for every p-value and
seed count), produced by `release_bundle/clarke_analysis.py` from the
per-window prediction dumps of the clean-retrain checkpoints
(`predictions/<arm>/seed_<S>/<cohort>.npz`, built 2026-09-04). Copies of the
summary sit in the project root as `clarke_error_grid.{md,csv}`.

Conventions, all matching the RMSE tables:
- 30-minute point forecast (column 5 of the 12-step output), every test window,
  unmasked (the paper's test convention). A real-samples-only variant gives the
  same ordering and the same significant contrasts (T1D-UOM drops about 3 points
  in zone A for every arm). It is in the CSVs under `filt = real`, not in the paper.
- Local = own-cohort single model held-in, mean of the four singles OOD. avg =
  unweighted mean of the four held-in cohorts, sd of the per-seed average.
- Paired two-sided t-test over seeds 42–46, same as every other contrast.
- Zone rules: Clarke et al. 1987, reference implementation (zone A tested first).
  The older `release_bundle/extended_metrics.py::clarke_zones` is NOT standard
  (D overwrites A for true <= 70) and was not used.
- The dumps use the pinned normalisation (154.04 / 61.00) for every arm. The
  paper's federated RMSEs were computed with recomputed stats (mean 152.18), so
  the dumped federated RMSEs differ from the tables by at most 0.02 mg/dL. Zone
  shares are unaffected at the two decimals reported.

## Edits to `revision/glucose_fl_paper_working.tex` (mirrored to v30)

1. **Abstract.** One sentence after "plain federated averaging only matched it.":
   "The ordering held on the Clarke error grid." Word count re-checked (see below).
2. **Methods, evaluation paragraph.** "single primary metric" → "primary
   metric". New sentences after the 60-minute sentence describe the Clarke grid
   (zone A, zones D and E, same test windows as the RMSE, `\cite{clarke1987}`,
   `Table~\ref{tab:clarke}`). The paired t-test sentence now reads "per-seed
   RMSE, or per-seed zone share".
3. **Results.** New paragraph "The ordering holds on the Clarke error grid."
   and new `tab:clarke` (zone A block and zones D+E block, five arms, held-in +
   OOD, `\resizebox` like `tab:h60`), inserted between `tab:h60` and the "MLDG
   has the lowest error in every comparison" paragraph. Bold = best per column
   within each block excluding Centralised (Local wins the HUPA-UCM D+E cell).
4. **Discussion, principal findings.** One sentence: "The same ordering held on
   the Clarke error grid, where MLDG also had the fewest clinically dangerous
   forecasts of the federated strategies."
5. **Limitation (i).** Rewritten: RMSE stays primary, the grid confirms the
   ordering, the models were not trained for it, 1–5 % of forecasts still land
   in the dangerous zones, MARD and event detection remain future work. The
   sentence "Whether federation's small advantage survives on such metrics is
   untested" is gone.
6. **`references.bib`.** New entry `clarke1987` (Clarke, Cox, Gonder-Frederick,
   Carter, Pohl. Diabetes Care 1987;10(5):622–628, doi 10.2337/diacare.10.5.622)
   in the "Clinical / diabetes background" group.

## Headline numbers now in the paper (30 min, all windows, 5 seeds)

| | Local | FedAvg | FedProx | MLDG | Centralised |
|---|---|---|---|---|---|
| zone A, held-in avg | 83.80 | 84.20 | 83.85 | 84.71 | 85.46 |
| zones D+E, held-in avg | 3.57 | 3.44 | 3.64 | 3.08 | 2.91 |

MLDG − Local zone A: +0.92 (p = 0.058, 4/5) held-in; ReplaceBG +0.88
(p = 0.019), BrisT1D +0.41 (p = 0.013), Flair +0.31 (p = 0.043), all 5/5.
FedAvg − Local +0.40 (p = 0.35), FedProx − Local +0.06 (p = 0.81).
MLDG − Local D+E: −0.49 (p = 0.028) held-in; ABC4D/ARISES/T1D-UOM p ≤ 0.009,
OOD p ≤ 0.024, all 5/5; HUPA-UCM +0.55 (p = 0.073, Local better).
MLDG − Centralised zone A −0.74 (p = 0.014); D+E p ≥ 0.25 everywhere.
Ditto μ=0.1 zone A held-in 84.48 (+0.68 vs Local, p = 0.037).
60 min: MLDG − Local zone A +0.79 (p = 0.015, 5/5); MLDG has the lowest D+E of
all arms incl. Centralised on ABC4D, T1D-UOM, ReplaceBG, BrisT1D, Flair.

## Trackers

`START_HERE.md` (tables 7 → 8, clinical-metrics item rewritten, next-run
reminder updated), `reviews/REQUIRED_FROM_YOU.md`, `reviews/SUBMISSION_TODO.md`
(D.1) updated. `reviews/UNSURE.md` untouched.
