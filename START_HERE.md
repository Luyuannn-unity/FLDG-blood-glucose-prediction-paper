# START HERE — orientation for this paper

Read this first if you're picking up the paper with no prior context.

## What the paper is

**Federated + meta-learned blood-glucose forecasting across sites.** Target venue:
*PLOS Digital Health*. One-line thesis:

> Train a 30-min CGM forecaster across four real T1D cohorts held at four separate
> institutions, without pooling raw data. Federation beats single-cohort training
> in-domain (MLDG 0.36 mg/dL lower, p = 0.005, 5/5 seeds) and transfers about as
> well as the best single cohort and better than the average one. The privacy
> cost vs pooling is 0.09 mg/dL (not significant; exact tie at 60 min). The
> headline practical result: a new site beats local-only training by finetuning
> the federated model on ~10% of its own patients on the two larger OOD cohorts
> (about 30% on the 15-patient BrisT1D).
>
> **2026-08-24: all numbers come from the clean retrain (see `../CHANGES.md`).
> The old "single-ARISES collapses OOD" story was a timestamp-bug artefact and is
> retired.**

Two contributions: (1) a **by-patient, held-in-vs-OOD benchmark** of federated
strategies (Local, FedAvg, FedProx, MLDG, APFL, Ditto) on one glucose task; (2) the
system was **run for real across four UK universities** (UCL, Manchester, Newcastle,
Oxford), not simulated on one host.

## Where things are

| What | Path |
|---|---|
| **LIVE draft (edit this)** | `revision/glucose_fl_paper_working.tex` |
| Bibliography (edit this) | `revision/references.bib` |
| Figures | `revision/figures/` (e.g. `data_efficiency.pdf`) |
| Version snapshots (frozen, read-only) | `revision/glucose_fl_paper_v1..v16.tex` — v16 is newest ≈ working |
| **Original draft — DO NOT EDIT** | `glucose_fl_paper.tex` (the author's Overleaf file; see "Two files" below) |
| **Submission checklist** | `reviews/SUBMISSION_TODO.md` |
| Open items the author owes | `reviews/REQUIRED_FROM_YOU.md` ← check this every session |
| Per-iteration change log | `reviews/iter{1,2,3,4,5}_revisions.md` |
| Reviewer critiques (5) | `reviews/iter1_reviewer*.md`, `reviews/iter2_*.md` |
| Reference verification | `reviews/refcheck_*.md` |
| Older open-questions doc | `reviews/UNSURE.md` (superseded by REQUIRED_FROM_YOU.md for live items) |
| Corrected results summary (the numbers come from here) | `../CHANGES.md` (repo root) |
| Raw per-seed outputs of the clean retrain | `C:\Users\luyua\Desktop\release_bundle\output_clean_retrain\` (`final_results_summary.csv`; per-seed under `pod_results/clean_eval` and `pod_results/followup`) |
| STALE, do not use | `../NEW_FINDINGS.md`, `../FLockit_GPFormer/output_arises_bolus/` (pre-fix runs) |

## Two files, one repo — the Overleaf gotcha

The author edits `glucose_fl_paper.tex` in **Overleaf** and pushes; our reviewed work
lives in `revision/glucose_fl_paper_working.tex`. These are **two separate documents**
that have not been merged — `revision/` has the abstract, all the analysis, the moved
comparison section, and every reviewer fix; the Overleaf file is the author's own
running copy. Before editing: `git pull --rebase --autostash origin main`. Expect
Overleaf commits ("Updates from Overleaf") to land between sessions.

**Merge status (verified 2026-08-11):** the Overleaf file's last content edit was
2026-06-29 (the ReplaceBG-adaptation section), and that content is in the working
file (extended to all 3 targets in `tab:finetune`). Nothing lives only in
`glucose_fl_paper.tex`, so at submission the author can simply point Overleaf's main
document at the working file (or rename it) — no line-by-line merge needed. If new
"Updates from Overleaf" commits touch `glucose_fl_paper.tex` after this date,
re-check before renaming.

## Workflow (do this every time)

1. `cd paper && git pull --rebase --autostash origin main`.
2. Edit `revision/glucose_fl_paper_working.tex` (and `references.bib`).
3. **No LaTeX toolchain locally** — validate structurally instead:
   - env balance: `begin{table}`==`end{table}`, same for `tabular`, `figure`, `document`
   - every `\label{tab:/fig:...}` has a `\ref`, and every `\cite{key}` key exists in `references.bib`
4. Snapshot to the next `glucose_fl_paper_vN.tex`, commit, `git push origin main`.
5. Log substantive changes in a new `reviews/iterN_revisions.md`; move resolved
   author-items out of `reviews/REQUIRED_FROM_YOU.md`.
6. **Never fabricate numbers.** Every value in the paper traces to a CSV under
   `release_bundle/output_clean_retrain/` or to a verified citation. If a number can't be
   traced, flag it — don't invent it. (This principle already caught and fixed the
   "untraceable Table 1" scare — the numbers were real, the source just wasn't shared.)

## Facts that are LOCKED IN (verified in code/data — don't re-litigate or contradict)

- **Cohorts.** Clients: HUPA-UCM, ABC4D, ARISES, T1D-UOM. Held-out OOD: ReplaceBG,
  BrisT1D, Flair. All adult T1D. Splits are **by patient** (test patients unseen).
- **Model.** Encoder–decoder transformer, ~4.9M params, seq_len 72 (6h), pred_len 12
  (60min), **full attention** (Informer-style; GPFormer uses sparse — ours is *not*
  GPFormer proper). **GPFormer framing REMOVED by author decision 2026-08-11**: no
  longer presented as our precursor/starting point. It survives only as (a) an
  unnamed Intro citation for "centralised MLDG glucose DG exists", (b) "as in
  GPFormer" on the decoder time-token convention, (c) a comparator in
  `tab:oodprior`. Don't re-add the precursor narrative.
- **Decoder** = Informer-style warm-up: last `label_len=6` context steps + 12 zeros.
  Not a learned start token.
- **Normalisation** = single global constant **154.04 ± 61.00 mg/dL**, computed on the
  4 training cohorts only, used by the federated and centralised models. **No OOD
  leakage** (verified in logs). Single-cohort (local) models use their own cohort's
  mean/sd (author confirmed 2026-08-24). Unchanged after the clean retrain.
- **Metric** = RMSE, **point** error at 30 min (also 60 min in `tab:h60`), mg/dL,
  mean±sd over **5 seeds (42–46)** since the 2026-08-21/22 clean rerun (the old
  set was 42/43/44/46/47). The paper text says just "5 random seeds" — author
  decision 2026-08-13: don't list the IDs in the paper (internal docs keep them).
  Every pairwise comparison uses a two-sided paired t-test across the 5 seeds.
- **Data quality (2026-08-24).** HUPA-UCM and T1D-UOM are cleaned rebuilds
  (constant-slope or clamped runs > 60 min cut, stretches < 280 samples dropped;
  kept 88% train / 70% test samples, same patient splits). Training and validation
  loss masked to real samples; test metrics unmasked. ABC4D/ARISES timestamps
  repaired. Described in the Methods subsection "Data quality". The paper is
  unpublished, so this is Methods, not a corrigendum.
- **Style rule (author, 2026-08-24):** simple, concise sentences. No semicolons
  and no em-dash asides (`---`) in prose. Numeric ranges written `$12$--$14$` stay.
- **Subset sizes use the ceiling:** 10% of Flair = 10 patients (not 9), 10% of
  BrisT1D = 2, 70% of BrisT1D = 11 (do not state that count in the paper).
- **MLDG inner step** = one differentiable step by a `higher`-library copy of
  the client's Adam (inherits moments, lr, weight decay; writes nothing back);
  outer = meta-train + meta-test loss, equal weight, second-order kept.
  In Methods as equations (`eq:mldginner`/`eq:mldgouter`) since 2026-08-13;
  re-verified in `fl_paper_release/transformer/flock_model_transformer.py`
  (`_train_step_mldg_ref`). Not plain SGD — don't regress the wording.
- **OOD scoring** = each cohort's held-out **test split** (ReplaceBG = 21 patients), so
  zero-shot / from-scratch / finetuned all share one test set per cohort.
- **APFL α is learned, not frozen**: it decays 0.23→0.02–0.08, i.e. APFL chooses to
  deploy a ~95% global model. This is a *finding* (personalisation isn't worth much
  here), not a bug.
- **Deployment** = ran live across the 4 universities. Title says "four-institution
  deployment". Caveats: single country; no secure aggregation / DP yet. **Author
  decision 2026-08-11: do NOT emphasise the lack of security** — "plain HTTP /
  no encryption / could be attacked" language was removed everywhere; the only
  remaining mention is one neutral sentence in Limitations (v) framed as the
  next step (add secure aggregation + DP).

## Current state of the draft

- **Tables (7):** datasets (HUPA-UCM/T1D-UOM rows are the cleaned data); held-in
  RMSE@30 (`tab:main`, ties both bold); OOD@30 (`tab:ood`, federated + centralised
  + four single-cohort rows + Local mean-of-four, all with sd); 60-min (`tab:h60`,
  since 2026-08-24 a FULL table: all four held-in cohorts for every strategy, OOD
  columns, Centralised row, wrapped in `\resizebox`); zero-shot vs
  ReplaceBG-trained baselines (`tab:oodprior`); external by-time comparison
  (`tab:prior`, sd on all four Ours rows, harder-HUPA footnote); finetuning
  (`tab:finetune`).
- **Figures (2):** data-efficiency (`fig:dataeff`, regenerated 2026-08-24 by
  `revision/figures/data_efficiency_fig.py` from the clean per-seed CSVs);
  FL-system architecture (`fig:system`).
- **Key numbers (30 min, 5 seeds 42–46; single-cohort arms re-evaluated
  2026-08-24 with the training-time normalisation constant):** held-in avg Local
  20.49, FedAvg 20.43, FedProx 20.58, MLDG 20.25, Centralised 20.16. MLDG − Local
  −0.23 (p = 0.014, 5/5), FedAvg − Local −0.05 (p = 0.14, NOT significant),
  FedProx − Local +0.10 (n.s.), MLDG − FedAvg −0.18 (p = 0.010; −0.21, p = 0.002
  at 60 min), MLDG − Centralised +0.09 (p = 0.32; exact tie at 60 min). Local
  wins ARISES numerically (21.87 vs MLDG 22.06, p = 0.24). MLDG lowest of
  {FedAvg, FedProx, MLDG} in all 16 held-in/OOD cells. OOD@30 MLDG
  21.30/26.25/25.02 (ReplaceBG/BrisT1D/Flair), Centralised 21.41/26.31/25.00,
  Local mean-of-four 21.73/26.56/25.22 (MLDG beats it on all three, p ≤ 0.004;
  FedAvg on ReplaceBG only; FedProx nowhere). Single-ARISES is the best single
  OOD model on BrisT1D/Flair (ties MLDG on BrisT1D, edges it by 0.17 on Flair);
  single-HUPA is the worst, 0.7–0.9 behind MLDG. MLDG beats a single model in 18
  of 24 OOD cells. Finetune beats scratch on all three by 0.49/0.29/0.29 (best
  arm, all 5/5); 10% of patients enough on ReplaceBG (17) and Flair (10); BrisT1D
  pulls ahead from ~30%. HUPA-UCM absolute errors are ~1.4 mg/dL higher on the
  clean test set than the same models score on the public grid.
- **Headline wording (since v30): "the meta-learned federated model beats local
  training; plain averaging matches it."** Do not write "federation beats local"
  without the MLDG qualifier.
- **Two things every number in the paper currently is NOT:** from the live
  four-site run (see open threads), and final for the single-cohort rows.

## The biggest open threads (see REQUIRED_FROM_YOU.md for the full list)

- **Live four-institution rerun (author decision 2026-08-24).** The clean rerun
  was executed on rented cloud pods + the local machine through the sweep driver,
  not through the HTTP server/clients across the four universities. The author
  will rerun live on the four sites. Until then the "run live across four
  universities" sentences stay as they are, and a final number swap follows the
  live run (the `batch*.py` scripts in the session scratchpad show the pattern;
  every number lives in the tables plus a known list of prose spots).
- **Single-cohort OOD rows (deferred).** Keep in `tab:ood` / move to an S1 Table /
  drop. The draft is written for "keep". Sentences that hang on it are listed in
  `reviews/iter12_revisions.md`.
- **Persistence & clinical metrics: DECIDED 2026-08-11, not reported.** Don't
  re-open without the author. RMSE-only framing throughout.
- **Centralised reference:** fully on disk now (`clean_eval/seed_*/centralized/`),
  30 and 60 min, in every table. Framed as "reference", not "upper bound".
- **Statistical framing:** MLDG vs FedAvg and FL vs Local are significant at 5
  seeds; still unsettled are MLDG vs Centralised, MLDG vs FedAvg on Flair @30
  (p = 0.09), FedAvg vs FedProx (p = 0.06), FedProx vs Local @30 (p = 0.77).
  Limitation (iii) says so. FedProx µ is untuned.
- **Admin blockers for PLOS:** author affiliations 2 and 3, ORCID, CRediT, cover
  letter, suggested reviewers. Abstract ≤ 300 words and summary ≤ 200 are now met
  (re-count after any edit). Full checklist: `reviews/SUBMISSION_TODO.md`.

## Next-run reminder for the author

Save **model checkpoints AND per-window predictions** on any future training run.
Clinical metrics (Clarke/Parkes/MARD/event-detection) can't be recomputed from the
aggregate CSVs currently on disk. The 60-min numbers only survived because they were
logged (`rmse_60=` in the training logs).
