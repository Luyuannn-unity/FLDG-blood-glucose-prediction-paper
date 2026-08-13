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
