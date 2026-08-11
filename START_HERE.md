# START HERE — orientation for this paper

Read this first if you're picking up the paper with no prior context.

## What the paper is

**Federated + meta-learned blood-glucose forecasting across sites.** Target venue:
*PLOS Digital Health*. One-line thesis:

> Train a 30-min CGM forecaster across four real T1D cohorts held at four separate
> institutions, without pooling raw data. Federation matches single-cohort training
> in-domain and transfers more reliably out-of-distribution (it avoids the
> catastrophic collapse a single-cohort model can suffer). The headline practical
> result: a new site reaches — and beats — local-only training by finetuning the
> federated model on as little as ~10% of its own patients.

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
| Version snapshots (frozen, read-only) | `revision/glucose_fl_paper_v1..v9.tex` — v9 is newest ≈ working |
| **Original draft — DO NOT EDIT** | `glucose_fl_paper.tex` (the author's Overleaf file; see "Two files" below) |
| Open items the author owes | `reviews/REQUIRED_FROM_YOU.md` ← check this every session |
| Per-iteration change log | `reviews/iter{1,2,3,4}_revisions.md` |
| Reviewer critiques (5) | `reviews/iter1_reviewer*.md`, `reviews/iter2_*.md` |
| Reference verification | `reviews/refcheck_*.md` |
| Older open-questions doc | `reviews/UNSURE.md` (superseded by REQUIRED_FROM_YOU.md for live items) |
| New experiment results not yet fully in the paper | `../NEW_FINDINGS.md` (repo root) |
| Raw experiment outputs (numbers come from here) | `../FLockit_GPFormer/output_arises_bolus/cgm/seed_*/<method>/` |

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
   `FLockit_GPFormer/output_*/` or to a verified citation. If a number can't be
   traced, flag it — don't invent it. (This principle already caught and fixed the
   "untraceable Table 1" scare — the numbers were real, the source just wasn't shared.)

## Facts that are LOCKED IN (verified in code/data — don't re-litigate or contradict)

- **Cohorts.** Clients: HUPA-UCM, ABC4D, ARISES, T1D-UOM. Held-out OOD: ReplaceBG,
  BrisT1D, Flair. All adult T1D. Splits are **by patient** (test patients unseen).
- **Model.** Encoder–decoder transformer, ~4.9M params, seq_len 72 (6h), pred_len 12
  (60min), full attention. It follows **GPFormer** (Zhu et al., IEEE JBHI 2024) but
  uses **full attention, not GPFormer's sparse attention** — so it is Informer-style,
  *not* GPFormer proper. GPFormer must stay cited as the antecedent (it did
  Transformer+MLDG+zero-shot glucose DG first, centrally); our novelty is doing it
  **federated, without pooling, across institutions**.
- **Decoder** = Informer-style warm-up: last `label_len=6` context steps + 12 zeros.
  Not a learned start token.
- **Normalisation** = single global constant **154.04 ± 61.00 mg/dL**, computed on the
  4 training cohorts only. **No OOD leakage** (verified in logs). Shipped with the model.
- **Metric** = RMSE, **point** error at 30 min (also 60 min in `tab:h60`), mg/dL,
  mean±sd over **5 seeds (42,43,44,46,47)**; seed 45 not run.
- **OOD scoring** = each cohort's held-out **test split** (ReplaceBG = 21 patients), so
  zero-shot / from-scratch / finetuned all share one test set per cohort.
- **APFL α is learned, not frozen**: it decays 0.23→0.02–0.08, i.e. APFL chooses to
  deploy a ~95% global model. This is a *finding* (personalisation isn't worth much
  here), not a bug.
- **Deployment** = ran live across the 4 universities. Title says "four-institution
  deployment". Honest caveats: plain HTTP (no encryption/secure-agg/DP), single country.

## Current state of the draft

- **Tables (7):** datasets; held-in RMSE@30 (`tab:main`); OOD@30 across 3 cohorts
  (`tab:ood`); zero-shot vs ReplaceBG-trained baselines (`tab:oodprior`); external
  by-time comparison (`tab:prior`); 60-min (`tab:h60`);
  finetuning across 3 targets (`tab:finetune`). (`tab:bolus` and all bolus content
  removed 2026-08-11 by author decision.)
- **Figures (1):** data-efficiency (`fig:dataeff`). **FL architecture diagram still owed.**
- **Key numbers:** held-in avg ~20 mg/dL (Local 20.16, FedAvg 20.09, MLDG 19.99);
  OOD@30 MLDG 21.34/26.31/25.05 (ReplaceBG/BrisT1D/Flair); single-ARISES collapses
  (28.51±6.85 on ReplaceBG, and on all 3). MLDG numerically best everywhere but
  **not significant at 5 seeds** (paired t ≈ −1.3 @30, −2.1 @60).

## The biggest open threads (see REQUIRED_FROM_YOU.md for the full list)

- **Persistence & clinical metrics (`NEW_FINDINGS.md` Phase D/E): DECIDED 2026-08-11 —
  not reported.** Author's call: the paper's claim is RMSE under federation/transfer;
  models were not optimised for event detection. Don't re-open without the author.
- **Centralised baseline (Phase F) has been re-run convergence-matched** (50k steps,
  5 seeds — see NEW_FINDINGS.md). Result: FL ≈ centralised pooling held-in and OOD.
  Open decision: add it to the paper (recommended — answers "why not just pool?").
- **More seeds** would settle MLDG significance. **FedProx µ is untuned.**
- **Admin blockers for PLOS:** author names/affiliations/email + ORCID, code repo DOI,
  per-dataset licence/accession + IRB statement, cover letter, ≥4 suggested
  reviewers, abstract over the 300-word limit, author summary over 200 words.
  (MLDG update spec and patient-count rule: resolved 2026-08-11, now in Methods.)
  Full checklist: `reviews/SUBMISSION_TODO.md`.

## Next-run reminder for the author

Save **model checkpoints AND per-window predictions** on any future training run.
Clinical metrics (Clarke/Parkes/MARD/event-detection) can't be recomputed from the
aggregate CSVs currently on disk. The 60-min numbers only survived because they were
logged (`rmse_60=` in the training logs).
