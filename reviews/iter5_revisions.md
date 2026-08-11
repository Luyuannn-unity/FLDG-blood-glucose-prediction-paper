# Iteration 5 — 2026-08-11 — author decisions applied + Methods gaps closed

Session driver: the author's pre-submission triage. Snapshot: `glucose_fl_paper_v10.tex`.

## Changes to `revision/glucose_fl_paper_working.tex`

1. **Bolus removed entirely** (author decision). Deleted the Methods paragraph
   "Bolus input variant", the Results paragraph "Adding bolus insulin does not
   help…", and `tab:bolus`. Cleaned the now-unmotivated "CGM-only" contrast from
   the Results intro and the captions of `tab:main`, `tab:ood`, `tab:h60`. The
   paper is now 7 tables, CGM-only throughout. Kept the Intro's clinical phrase
   "inform bolus and snack decisions" (about patient decisions, not the variant).

2. **MLDG update spec written into Methods** (was deferred to "released with the
   code"; reviewer 2 called it non-reproducible). Verified in
   `flock_model_gpformer.py` and the training logs
   (`MLDG enabled (second-order/higher) — n_support=1, n_query=1, inner_iters=1,
   trade_off=1.0, inner_lr=same as outer`):
   - each batch grouped by patient; whole patients assigned to meta-train /
     meta-test, ~50/50 by window count, patient-disjoint;
   - fallback to a plain step if <2 eligible patients — never fired
     (0 of 191,100 MLDG steps across 5 seeds, from `mldg_split_usage.csv`);
   - inner update: one differentiable SGD step on the meta-train loss at the
     outer LR (1e-4);
   - outer loss: meta-train loss at original weights + meta-test loss at adapted
     weights, equal weight; second-order term retained (no first-order approx.);
   - outer step by the client's Adam; inner step does not touch Adam state.

3. **MetaboNet restored as data source** (author decision; passage existed in
   v1–v3 and had been cut). HUPA-UCM, T1D-UOM, and ReplaceBG come from MetaboNet's
   harmonised release, which explains the patient counts (22 of 25; 14 of 17) —
   the old "quality filtering" caption note was wrong and is replaced. Also notes
   we re-split by patient rather than adopting MetaboNet's leaky split.
   `\cite{wolff2026metabonet}` now used; entry was already in references.bib.

4. **RMSE@30 justification added** to "Evaluation protocol and metrics": (i) RMSE
   is the square root of the MSE training objective, so it measures what the
   compared training procedures were asked to do; (ii) 30 min is the standard,
   comparable horizon; (iii) one scalar per strategy–cohort pair keeps the many
   comparisons readable.

## Verification done this session

- tab:main federated rows recomputed from `output_arises_bolus/cgm/seed_*/…`:
  MLDG 19.99±0.18, FedAvg 20.09±0.12, FedProx 20.27±0.12 — exact match.
- Loss function confirmed from logs: `Loss: MSE (single-head, c_out=1)` — the
  code's `quantile_loss` attribute is an MSE adapter in all paper runs.
- Overleaf-vs-working: nothing unique remains in `glucose_fl_paper.tex` (last
  content edit 6/29 = ReplaceBG adaptation, superseded by `tab:finetune`).
  Rename/point-main-at-working is safe at submission.
- Structural checks pass: 7/7 table envs balanced, no orphan labels/refs, all
  cite keys present in references.bib.
- Found 7 empty seed_46 output dirs (apfl, decoupled, ditto×3, single_ABC4D,
  single_HUPA-UCM) — the source of tab:main's 4-seed cells; author to copy.

## Addendum (same day): seed_46 outputs synced — all 30-min tables now 5-seed

The author downloaded the complete `seed_46` folder from the remote machine.
Verified before replacing: all 12 arms present; the 5 overlapping arms'
`best_model_local_test_irt.csv` are byte-identical to the local partial copy;
the old partial folder was a strict subset (backed up to the session scratchpad).

Numbers updated in the working draft (v11), all recomputed from CSVs at 5 seeds:

- `tab:main` — Local: 18.86±0.15 / 19.94±0.17 / 22.04±0.22 / 19.80±0.19, avg
  20.16 (was 20.15). APFL: avg 20.35 (was 20.28). APFL-decoupled: avg 20.32
  (was 20.37). Ditto µ=0.01: avg 20.06; µ=0.1: 20.17; µ=1.0: 20.05 (was 20.09,
  now numerically below FedAvg — prose softened to "on par with FedAvg").
  Caption's 4-seed disclosure removed: every cell is 5 seeds.
- `tab:ood` — trained-on-HUPA-UCM: 21.93±0.17 / 27.10±0.24 / 25.81±0.23;
  trained-on-ABC4D: 21.78±0.22 / 26.70±0.28 / 25.35±0.20; Local mean Flair
  26.75→26.76. ARISES/T1D-UOM rows unchanged (already 5-seed).
- Prose: Local held-in average 20.15→20.16 (Results + Discussion); Ditto
  ARISES best 21.98→21.95; evaluation-protocol 4-seed caveat removed.
- Bold markers unchanged (same winners in every column).

Second addendum: the author then also synced the remote logs
(`20260618_122726_cgm_s46_*.log`, 7 files). Provenance check passed — each log's
final held-in rmse_30 equals the synced CSV value, and re-deriving the old table
with mixed 4/5-seed means reproduced 34.26 / 38.29 / 45.45 / 41.90 exactly.
`tab:h60` Local cells updated to full 5-seed: held-in avg 34.29, OOD
ReplaceBG 38.30, BrisT1D 45.46, Flair 41.92 (prose 34.26→34.29). ARISES and
global rows unchanged (already 5-seed). Every number in the paper is now
5-seed and traced to disk. Parser: scratchpad `h60_recompute.py` (mirrors
`build_rmse60_fig.py`). The new outputs also include `best_global_model.pt`
for every arm, so clinical metrics are recomputable by inference later.

## Decisions recorded (see REQUIRED_FROM_YOU.md)

- Persistence / clinical-metrics comparison: **not reported** (author).
- Bolus: **removed** (author).
- Centralised Phase F baseline: re-run is convergence-matched; **include in
  paper?** still open (recommended: include).
