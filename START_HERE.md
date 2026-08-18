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
| Version snapshots (frozen, read-only) | `revision/glucose_fl_paper_v1..v16.tex` — v16 is newest ≈ working |
| **Original draft — DO NOT EDIT** | `glucose_fl_paper.tex` (the author's Overleaf file; see "Two files" below) |
| **Submission checklist** | `reviews/SUBMISSION_TODO.md` |
| Open items the author owes | `reviews/REQUIRED_FROM_YOU.md` ← check this every session |
| Per-iteration change log | `reviews/iter{1,2,3,4,5}_revisions.md` |
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
  (60min), **full attention** (Informer-style; GPFormer uses sparse — ours is *not*
  GPFormer proper). **GPFormer framing REMOVED by author decision 2026-08-11**: no
  longer presented as our precursor/starting point. It survives only as (a) an
  unnamed Intro citation for "centralised MLDG glucose DG exists", (b) "as in
  GPFormer" on the decoder time-token convention, (c) a comparator in
  `tab:oodprior`. Don't re-add the precursor narrative.
- **Decoder** = Informer-style warm-up: last `label_len=6` context steps + 12 zeros.
  Not a learned start token.
- **Normalisation** = single global constant **154.04 ± 61.00 mg/dL**, computed on the
  4 training cohorts only. **No OOD leakage** (verified in logs). Shipped with the model.
- **Metric** = RMSE, **point** error at 30 min (also 60 min in `tab:h60`), mg/dL,
  mean±sd over **5 seeds (42,43,44,46,47)**; seed 45 not run. The paper text
  says just "5 random seeds" — author decision 2026-08-13: don't list the IDs
  in the paper (internal docs keep them).
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

- **Tables (7):** datasets; held-in RMSE@30 (`tab:main`, avg column now carries
  per-seed-avg sd); OOD@30 across 3 cohorts (`tab:ood`); 60-min (`tab:h60`, since
  2026-08-12 includes the 5 PFL held-in rows from the training logs, sits right
  after `tab:ood`, and still has NO centralised row — no 60-min centralised data
  exists); zero-shot vs ReplaceBG-trained baselines (`tab:oodprior`); external
  by-time comparison (`tab:prior`); finetuning across 3 targets (`tab:finetune`).
  (`tab:bolus` and all bolus content removed 2026-08-11 by author decision.)
- **Figures (2):** data-efficiency (`fig:dataeff`); FL-system architecture
  (`fig:system`, `revision/figures/fl_system.pdf`, matplotlib source
  `fl_system_fig.py` beside it, added 2026-08-13 — the long-owed diagram).
- **Key numbers:** held-in avg ~20 mg/dL (Local 20.16, FedAvg 20.09, MLDG 19.99,
  Centralised reference 19.90); OOD@30 MLDG 21.34/26.31/25.05 (ReplaceBG/BrisT1D/
  Flair), Centralised 21.52/26.33/24.95; single-ARISES collapses (28.51±6.85 on
  ReplaceBG, and on all 3). MLDG numerically best among the *federated* strategies
  in every comparison the paper reports, but **not significant at 5 seeds**
  (paired t ≈ −1.3 @30, −2.1 @60). The paper says "every *reported* comparison"
  because at 60 min FedAvg edges MLDG on the undisplayed T1D-UOM held-in cell
  (32.18 vs 32.25). FedProx held-in avg is 20.27 since 2026-08-12 (full-precision
  per-seed mean; the old 20.28 was a mean of rounded cells).
  Every number in the paper is full 5-seed and traced to disk (as of 2026-08-11),
  except the centralised row — see open threads.

## The biggest open threads (see REQUIRED_FROM_YOU.md for the full list)

- **Persistence & clinical metrics (`NEW_FINDINGS.md` Phase D/E): DECIDED 2026-08-11 —
  not reported.** Author's call: the paper's claim is RMSE under federation/transfer;
  models were not optimised for event detection. Don't re-open without the author.
  **Extended 2026-08-12:** the Results "Beyond RMSE" TIR/lag paragraph is also
  removed (author decision — the paper's framing is RMSE-only). The paper now
  reports no TIR agreement or forecast-lag numbers anywhere; Methods, Limitation
  (i), and Future work were cleaned to match. The ~20-min forecast-lag caveat is
  gone with it.
- **Centralised (pooled) reference: IN THE PAPER since v13** (Methods baselines,
  rows in tab:main/tab:ood, Results paragraph, limitation (viii) rewritten). Framed
  as "reference", NOT "upper bound" (empirically not strict). ⚠️ Its numbers trace
  to `NEW_FINDINGS.md` per-seed values (recomputed with *sample* sd) — author still
  owes `output_centralized_shuffled/seed_*/best_model_local_test_irt.csv` on disk.
- **More seeds** would settle MLDG significance. **FedProx µ is untuned.**
- **PLANNED NEXT (agreed 2026-08-11): full rewording/flow pass with the author, in
  order Results → Discussion → Methods → Intro → Abstract + Author summary last**
  (abstract cut 420→≤300 words and author summary 276→150–200 happen at the end,
  after content settles). Facts and numbers are final unless the author says
  otherwise — the pass is about prose, not content.
- **Admin blockers for PLOS:** author names/affiliations/email + ORCID, cover
  letter, ≥4 suggested reviewers, abstract over the 300-word limit, author summary
  over 200 words. (Done 2026-08-11: ethics statement — UCL IHI LREC Project ID
  1665; ABC4D/ARISES access route — on request via ken.li@ucl.ac.uk; code repo
  live + MIT; Limitations and Future work merged into one paragraph.)
  (MLDG update spec and patient-count rule: resolved 2026-08-11, now in Methods.)
  Full checklist: `reviews/SUBMISSION_TODO.md`.

## Next-run reminder for the author

Save **model checkpoints AND per-window predictions** on any future training run.
Clinical metrics (Clarke/Parkes/MARD/event-detection) can't be recomputed from the
aggregate CSVs currently on disk. The 60-min numbers only survived because they were
logged (`rmse_60=` in the training logs).
