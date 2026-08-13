# Iteration 8 — Methods styling pass, part 1: redundancy cuts (2026-08-13)

Scope: **Materials and methods only** (prose; tables untouched), plus two
Discussion follow-up edits from the concurrent Discussion session (see Notes).
Facts and numbers unchanged — deletions only, with minimal splices.

## What changed

Per the author's instruction ("remove redundant sentences ... without losing
any information"), 12 restatements were deleted. Each states something the
section already says elsewhere:

1. Datasets: "Every window in the validation and test sets therefore comes
   from a patient never seen during training, and" (the author's own example;
   consequence of the by-patient split stated in the same sentence).
2. Preprocessing: "rather than using per-client statistics" (excluded by
   "a single *global* mean ... shared across all clients").
3. Forecasting model: "The full 12-step horizon is produced in one forward
   pass." (restates "single-shot rather than autoregressive").
4. Forecasting model: "The same architecture is used for every client and
   every federated strategy, so all comparisons differ only in how the model
   is trained, not in capacity." (duplicate of "Holding this architecture
   fixed..." in the same subsection).
5. FL system: "rather than simulated on one host" (the paragraph's closing
   "shared-memory shortcut" sentence carries the same contrast).
6. FL system: "each training only on its own cohort" (protocol paragraph
   above: clients "train locally on their own cohort").
7. Centralised reference: "--- it requires moving raw records across
   institutions ---" (same as "as if their raw data could be pooled at one
   site" two sentences earlier).
8. MLDG: "MLDG and FedProx alter only client-side training; the server still
   FedAvg-aggregates." (duplicate of the FL-system subsection).
9. Evaluation: ", which contributed no training data" ("never-seen cohorts",
   same sentence).
10. Evaluation: ", which is what makes our numbers comparable with prior
    work" (re-derives "most widely reported in this literature").
11. OOD test sets: "No patient from any held-out cohort contributes to
    federated training, so" (premise stated twice before; kept "Every OOD
    test patient is unseen in the strong sense...").
12. Evaluation: "; every configuration is complete over all five seeds"
    (the preceding sentence lists all five seeds).

~120 words cut from Methods.

## Verification

Found by a 14-agent workflow (3 finder lenses -> merge/dedup -> one
adversarial verifier per cut, checking information loss, grammar of the
splice, and structural role). All 12 confirmed safe; 24 raw candidates were
merged to 12. Structure checks pass after editing: envs balanced
(table/tabular/figure/document), cite count unchanged (72), no dangling refs.

## Notes

- This commit also carries two small Discussion edits made by the concurrent
  Discussion session after its 7e0d2cb commit: the paragraph title
  "Implications for a clinical consortium" -> "Implications for a small group
  of clinics", and a new hedged closing passage on federated pretraining of
  glucose foundation models (cites the existing `lu2026glucofmbench` key;
  explicitly states no scaling experiment was run).
- Still owed for the Methods rework (next parts): method citations in
  "Federated strategies and baselines" (mcmahan2017fedavg, li2020fedprox,
  li2018mldg, deng2020apfl, li2021ditto — currently Intro-only), then the
  wording/flow pass.
- Snapshot: `revision/glucose_fl_paper_v21.tex`.

---

# Part 2 — author-directed Methods changes (2026-08-13, same day)

Per the author's instructions. Note: some of these edits rode into the
concurrent session's commit 5a0ccec (whose message covers only the
tab:finetune column reorder); this log is the record for all of them.

1. **Datasets**: the three held-out cohorts are no longer "never seen during
   training / used only as OOD test cohorts" — they are later finetuned on.
   New text names both roles (zero-shot OOD test; finetuning target adapted on
   training patients, evaluated on held-out test patients). Table note now
   says "excluded from *federated* training"; Evaluation regimes now says
   "the three held-out cohorts"; the OOD-test-sets claim ("unseen cohort and
   unseen individual") is now scoped to the zero-shot evaluation.
2. **FL system figure added** (`fig:system`; `figures/fl_system.pdf`/`.png`,
   matplotlib source `figures/fl_system_fig.py`): server + 4 clients with
   patient counts, numbered round steps (broadcast / local train / return /
   FedAvg), public-internet HTTP band, no-raw-data-movement footer.
   Referenced from the FL-system subsection; closes the long-owed
   FL-architecture-figure item (tex author-NOTE updated).
3. **Strategy citations at point of definition**: FedAvg (mcmahan2017fedavg),
   FedProx (li2020fedprox), MLDG (li2018mldg), APFL (deng2020apfl), Ditto
   (li2021ditto). Previously Intro-only.
4. **FedProx**: dropped "did not sweep µ / indicative rather than tuned"
   (author instruction). Methods now just states µ=0.05; the untuned-µ caveat
   stays in Limitations (iv).
5. **MLDG rewritten with equations** (`eq:mldginner`, `eq:mldgouter`)
   replacing the verbose mechanics. The Adam-with-history inner step was
   re-verified in code (fl_paper_release/transformer/flock_model_transformer.py,
   `_train_step_mldg_ref`): one differentiable step by a `higher` copy of the
   client's Adam (inherits moments, lr 1e-4, weight decay; no write-back);
   outer = meta-train + meta-test loss at equal weight (mldg_trade_off=1.0);
   second-order retained; real-Adam outer step; patient-disjoint split with
   never-fired fallback. All six claims VERIFIED with file:line evidence.
6. **Seeds**: paper no longer lists seed IDs — "5 random seeds" only (author
   instruction; internal docs keep the IDs). "Across the common seeds" →
   "across seeds".
7. **Removed** the "We emphasise that these standard deviations…" passage to
   the end of the paragraph (author instruction). The seed-sd caveat and
   clinical-metrics pointer survive in Limitations (i)/(iii).
8. **New Methods paragraph "Finetuning on held-out cohorts"** (the protocol
   was previously only implied by Results): three arms (zero-shot /
   from-scratch / finetuned) on the same held-out test patients; finetuning =
   all parameters, 10 epochs, lr 1e-4, val-best selection (traced to
   NEW_FINDINGS Phases B/C/G/H and `finetune_ood()` in the release code);
   data-efficiency = random 10–70% of training patients per seed, val/test
   unchanged.
9. **Implementation details corrected**: "one local epoch per communication
   round" → "one pass over the local training set, capped at 500 gradient
   steps" (traced to `proposer_max_steps_per_epoch: 500` in
   config_mldg_seed42.yaml and NEW_FINDINGS Phase B; the 191,100 MLDG-step
   total is consistent with the cap, not with full epochs). Also added
   gradient-norm clipping at 1.0 (verified universal: main step, MLDG paths,
   PFL trainers).
10. **Results honesty fix that follows from 8/9**: "identical training
    budget" claim removed (the finetuned arm trains for *fewer* steps than
    from-scratch — ≤5,000 vs ≤12,500 — so the old wording was wrong, though
    conservative). Now: both arms see identical target data, gain attributed
    to initialisation. tab:finetune note likewise now says the finetuned rows
    differ in starting weights, not in data seen.

Structure checks: envs balanced (figure=2, equation=2), fig:system 1 ref,
fig:dataeff 3 refs, eq labels ref'd via \eqref, all 5 new cite keys in
references.bib (82 \cite total). Snapshot: v24.
