# Things I need from you — running list

You asked me to track this and chase you. Ticked items are resolved; open items block
specific claims in the paper. Ordered by what would sink the paper first.

---

## 🔴 OPEN — blocks a claim currently in the paper

| # | What I need | Why it matters / what it blocks |
|---|---|---|
| 1 | **Sync the 5-seed runs** (you said done, not synced) | I'll re-verify every table against the synced data. Until then the tables rest on the current export. |
| 2 | **Exact MLDG update spec** — inner learning rate; whether the 2nd-order term is really computed (`create_graph`); what happens to Adam's moment buffers in the inner step | Methods currently says "the exact inner update… will be released with the code." Reviewer 2 called the current description non-reproducible. This is the one method we name in the title. |
| 4 | **Sanity-check the GPFormer framing** (Intro para + Methods) | GPFormer (Zhu 2024) already did Transformer+MLDG+zero-shot glucose DG. I reposition us as "same objective, but without pooling, across institutions." If that framing is wrong, a reviewer reads the paper as re-doing GPFormer. |
| 5 | **Patient-count filtering rule** — HUPA-UCM 22 (vs 25 published), T1D-UOM 14 (vs 17) | Need the explicit inclusion/exclusion criterion. A silent patient drop reads as bias risk. |
| 6 | **Author names, affiliations, corresponding email** | Still `Name1 Surname` / `correspondingauthor@institute.edu`. |
| 7 | **Data availability**: code repo DOI/URL, per-dataset access route + licence + accession, IRB/consent statement for secondary use | PLOS will not accept "available from the authors." Desk-reject risk. |
| 8 | **ARISES citation author list** (I added Zhu et al., npj Digit Med 2022, DOI 10.1038/s41746-022-00626-5); and **ABC4D**: registry (NCT02053051) or a journal paper? | I could confirm the DOI/trial but not the full author order. |

## 🟡 OPEN — decisions, not blockers

| # | Decision | My recommendation |
|---|---|---|
| 9 | Cite **MetaboNet-Bench**? | Optional. It benchmarks all 3 OOD cohorts but only as a *pooled* 13-dataset aggregate, and its train pool includes HUPA-UCM + T1D-UOM (2 of our training cohorts), so it is **not** an independent comparator. Bib entry is ready. |
| 10 | Include **GPFormer's reciprocal data point** — it scores 22.9 zero-shot on ABC4D, one of *our* training cohorts (we get 19.68 held-in) | Nice symmetry (they transfer into our cohort, we transfer into theirs). Your call. |
| 11 | Keep `tab:bolus`? | Paper now has 7 tables. If you want to cut one, this is the least load-bearing. |

---

## ✅ RESOLVED (answered by you)

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
