# Iteration 6 — Results rewording pass (2026-08-12)

Prose/flow pass on Results, per the author's instructions. Facts unchanged except
where noted (one rounding fix, one new-data table extension — both traced to disk).

## Styling

- Removed the "honest" hedging tic in all three places: Intro ("evaluate ...
  honestly" → "evaluate ..."), Results ("The honest reading is therefore" → "The
  reading is therefore"), Discussion ("Three caveats keep this honest" → "Three
  caveats apply").

## tab:main (held-in 30-min)

- Caption note now opens "Mean ± standard deviation across 5 random seeds" (seed
  IDs stay in Methods).
- The per-seed-average sd is no longer a caption aside for 3 strategies; it is
  appended to **every** avg cell (`20.09 ± 0.12` etc.), explained together with
  the "avg is the unweighted mean" sentence. Values computed from the per-seed
  CSVs (`output_arises_bolus/cgm/seed_*/<arm>/best_model_local_test_irt.csv`;
  centralised from NEW_FINDINGS Phase F per-seed table), sample sd (ddof=1) —
  verified to be the same convention as every existing cell.
- **FedProx avg corrected 20.28 → 20.27.** The old value was the mean of the
  rounded cells; 20.27 is the full-precision per-seed mean (20.272). No other avg
  changed.
- Dropped from the caption: the PFL-no-OOD explanation (text covers it later) and
  "differences among strategies are within seed variation". Bolding note
  simplified to "lowest value per column excluding the centralised reference".

## Results prose

- ¶1 (federation matches held-in): removed all numbers that sit in tab:main /
  tab:ood; the paragraph now points at the tables. CGM sensor error claim
  replaced: uncited "≈8–15 mg/dL" → "MARD ≈8–9%, roughly 12–14 mg/dL at this
  population's mean glucose" with **two new verified references**
  (`garg2022dexcomg7` Dexcom G7 MARD 8.2%, DOI 10.1089/dia.2022.0011;
  `alva2023libre3` FreeStyle Libre 3 MARD 7.8%, DOI 10.1007/s13300-023-01385-6).
- ¶MLDG: deleted the FedProx-was-weakest / untuned-µ sentence (not the point of
  the paragraph; µ-untuned remains in Limitations). Now carries both horizons'
  stats: gap 0.09 mg/dL at both horizons, OOD gaps 0.02–0.17, paired t ≈ −1.3
  (30 min) and ≈ −2.1 (60 min).
- ¶finetuning: removed the sentence restating tab:finetune's numbers (the
  0.3–0.7 mg/dL range stays); "the two truly held-out cohorts" → "Flair and
  BrisT1D" (ReplaceBG is equally held out).
- Accuracy fix forced by new data: "MLDG numerically lowest in every comparison"
  → "every **reported** comparison" (3 places: Results ¶MLDG, Discussion
  principal findings, Discussion on-meta-learning). Reason: at 60 min FedAvg
  edges MLDG on the undisplayed T1D-UOM held-in cells (32.18 vs 32.25).

## tab:h60 (60-min) — extended and moved

- **Moved** (paragraph + table) from the end of Results to directly after
  tab:ood, so the two horizons sit together before the centralised/MLDG/
  personalised analysis and the adaptation story.
- **Added the five PFL held-in rows** (ARISES + avg columns, OOD dashes),
  recovered from `rmse_60=` lines in `logs_gpformer_arises_bolus` training logs
  with the `build_rmse60_fig.py` parsing logic, extended to 5 seeds and sample
  sd. Extraction reproduced every pre-existing tab:h60 cell exactly before the
  new rows were trusted. New rows: APFL 36.67±0.09 / 34.37±0.22; APFL-decoupled
  36.52±0.26 / 34.34±0.16; Ditto µ=0.01 **36.36±0.16** (new ARISES column bold) /
  34.16±0.15; Ditto µ=0.1 36.64±0.13 / 34.22±0.09; Ditto µ=1.0 36.65±0.22 /
  34.14±0.18.
- avg column now carries per-seed-average sds (Local 34.29±0.14, FedAvg
  34.16±0.08, FedProx 34.31±0.11, MLDG 34.07±0.12), matching tab:main's style.
- Conclusions checked against the new rows and they hold: PFL held-in averages
  straddle FedAvg (34.14–34.37), MLDG's 34.07 is below the whole band, ditto
  µ=0.01 again wins ARISES (as at 30 min). Paragraph rewritten: table numbers
  removed from text, PFL clause added, significance sentence moved to ¶MLDG.
- **Centralised 60-min: does NOT exist on disk or in NEW_FINDINGS** (Phase F is
  30-min only), so no centralised row was added. Logged as a follow-up in
  REQUIRED_FROM_YOU item 12.

## Untouched, pending author

- ¶"Federation costs almost nothing relative to centralised pooling" — author
  asked for a summary of its message before rewording.
- ¶"Beyond RMSE" (TIR/lag) — author asked where the numbers live, what the
  conclusion is, and whether to keep it. Assessment delivered in-session; awaiting
  decision.

## Second batch (same session) — centralised paragraph + full number sweep

- **Centralised-provenance question resolved in-session**: the author asked how
  the paper can claim centralised-vs-FL parity OOD when "I never ran an OOD test
  on CL". Answer: the Phase F centralised run's standard eval pass scored all 7
  datasets (per-seed OOD values are in NEW_FINDINGS Phase F); the author
  confirmed they had forgotten the run. Claim stands; CSV sync still owed
  (item 12).
- **¶"Federation costs almost nothing"** rewritten to carry one message only:
  privacy is nearly free — ~0.1 mg/dL held-in, on par OOD ("indistinguishable" →
  "on par"). All table-restated numbers replaced with table refs. **Moved** from
  after tab:h60 to directly before the "better starting point" paragraph.
- **The transfer-limit point** ("even the pooled model transfers worse than
  from-scratch on the target") moved out of the centralised paragraph and now
  opens the "better starting point" paragraph as its motivation: zero-shot has a
  ceiling → use the transferred model as an initialisation. Also fixed the odd
  "a new site that does contribute data" → "that has local data of its own".
- **Number sweep across all Results paragraphs** (rule: no numbers in text that a
  table already carries; derived gaps/ranges stay):
  - ¶MLDG: personalised-cluster range "(20.1–20.4)" → table ref.
  - ¶personalised: Ditto µ=1.0 "(20.05, on par with FedAvg's 20.09)" and ARISES
    "(21.95)" dropped; wording "best Ditto held-in average, on par with
    FedAvg's".
  - ¶data-efficiency: the three "(21.14 vs 21.38 ...)" RMSE parentheticals
    dropped (from-scratch column is in tab:finetune, 10% values are in the
    figure); patient counts kept.
- New Results order: tab:main → ¶federation-matches + tab:ood → ¶60-min +
  tab:h60 → ¶MLDG → ¶personalised → ¶centralised-cost → ¶starting-point +
  tab:finetune → ¶data-efficiency + fig → ¶beyond-RMSE.
- Snapshot v18.

## Verification

- Env balance (table/tabular/figure/center/document) OK; all \cite keys resolve;
  all tab:/fig: labels referenced.
- Every new number traces: 30-min avg sds to the seed CSVs, 60-min PFL cells to
  the training logs, citations to publisher/PubMed records.
