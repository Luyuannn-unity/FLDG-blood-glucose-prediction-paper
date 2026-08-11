# Submission TODO — PLOS Digital Health

Consolidated checklist before submission. Sources: author's list (2026-08-11),
REQUIRED_FROM_YOU.md, START_HERE.md, and the PLOS Digital Health submission
guidelines (https://journals.plos.org/digitalhealth/s/submission-guidelines).

## A. Hard blockers (desk-reject or fabrication risk)

- [ ] **Cut the abstract to ≤300 words.** Currently ~420. PLOS limit is 300, no
  citations, no specialist abbreviations.
- [ ] **Cut the author summary to 150–200 words.** Currently ~276. First person,
  non-technical.
- [ ] **Author names, affiliations, corresponding email** — still placeholders
  (`Name1 Surname`). Corresponding author also needs an **ORCID iD** in the
  PLOS submission profile. (REQUIRED_FROM_YOU #6)
- [ ] **Data availability statement.** "Will be released upon publication" is not
  accepted by PLOS. Need: code repo with a DOI (e.g. Zenodo) *before*
  submission, plus per-dataset access route / licence / accession for all 7
  cohorts. (REQUIRED_FROM_YOU #7)
- [ ] **Ethics statement.** Explicit IRB/consent statement for secondary use of
  de-identified public datasets — even "exempt, and why" must be stated.
- [x] ~~Seed 46 outputs for 7 arms~~ **Synced + applied 2026-08-11.** All 30-min
  tables now full 5-seed; tab:main, tab:ood, and prose updated and re-verified
  cell-by-cell from CSVs.
- [x] ~~Remote training logs for those 7 arms~~ **Synced + applied 2026-08-11.**
  tab:h60 Local cells recomputed at 5 seeds (34.29 / 38.30 / 45.46 / 41.92);
  every number in the paper is now full 5-seed and traced to disk.
- [x] ~~MLDG exact update spec in Methods~~ **Done 2026-08-11** — spec verified in
  code + training logs and written into Methods (second-order, patient-disjoint
  split, inner SGD at 1e-4, equal-weight outer loss, Adam untouched).
- [x] ~~Patient-count filtering rule~~ **Done 2026-08-11** — counts are MetaboNet's
  harmonised release (22/25, 14/17); Methods now say so and cite MetaboNet.
- [x] ~~Merge the two tex files~~ **Verified 2026-08-11: no merge needed.** Nothing
  lives only in the Overleaf file (last content edit 6/29 is in working.tex).
  At submission, point Overleaf's main document at the working file / rename.
  Re-check only if new Overleaf commits touch `glucose_fl_paper.tex`.

## B. PLOS submission mechanics (needed at upload time)

- [ ] **Short title** ≤70 characters (title page + submission form). Full title
  (~136 chars) is fine.
- [ ] **Cover letter** — why this fits PLOS Digital Health.
- [ ] **Funding statement** — grant numbers + author initials, or "The author(s)
  received no specific funding for this work." Plus the "funders had no role"
  sentence if applicable.
- [ ] **Competing interests statement.**
- [ ] **Author contributions** — CRediT taxonomy, at least one role per author;
  entered in the submission system.
- [ ] **Suggest ≥4 reviewers** — must avoid recent collaborators and
  institutional colleagues (careful: 4 UK institutions are involved in the
  deployment).
- [ ] **Compile to PDF** — LaTeX submissions go in as PDF. No local toolchain, so
  final compile + visual check happens on Overleaf (table widths, overfull
  boxes, figure placement).
- [ ] **Figure format check** — figures embedded in the manuscript at first
  submission; captions directly after first citation, labelled "Fig 1" style.
  (High-res TIFF/EPS uploads only needed at revision.)
- [ ] **Reporting checklist** — consider TRIPOD+AI (prediction-model studies).
  Not on PLOS's explicit list, but reviewers of a clinical prediction paper
  often expect it; filling it in also catches gaps (e.g. missing-data handling).
- [ ] **Reference format pass** — Vancouver/ICMJE, first six authors then et al.,
  DOIs written in full, journal abbreviations per NCBI.

## C. Editorial passes (author + Claude, together)

- [x] ~~Justify RMSE@30 as the primary metric~~ **Done 2026-08-11** — three-reason
  justification (training objective, comparability, readability) added to the
  evaluation subsection.
- [ ] **Flow pass, section by section** (Abstract → Discussion), author + Claude.
- [ ] **Reference correctness pass** — finish open refcheck items: ARISES full
  author list, ABC4D registry-vs-paper. (REQUIRED_FROM_YOU #8)
- [ ] **GPFormer framing sanity check** — Intro + Methods positioning ("same
  objective, but federated, without pooling"). (REQUIRED_FROM_YOU #4)
- [ ] **Number-consistency pass** — every number in abstract/text matches the
  tables; every table traces to a CSV.
- [ ] **Structural validation** — env balance, every \label has a \ref, every
  \cite key exists in references.bib.

## D. Science decisions

1. [x] **Persistence / clinical-metrics finding: NOT reported** (author decision
   2026-08-11). Rationale recorded in REQUIRED_FROM_YOU.md. Don't re-open.
2. [x] **Centralised pooled baseline: added to the paper 2026-08-11** (Methods
   reference paragraph, rows in tab:main/tab:ood, Results paragraph, Discussion
   sentence; limitation (viii) rewritten). Follow-up: author to sync
   `output_centralized_shuffled/` CSVs so the numbers trace to this disk.
3. [ ] **MLDG significance wording** — numerically best everywhere, not
   significant at 5 seeds. More seeds, or keep the current careful phrasing.
4. [ ] **FL architecture figure** — author, later. Note: this is the *deployment*
   diagram (server + 4 university clients over HTTP), not a transformer figure —
   it depicts the paper's headline "real four-institution federation" claim.
   Claude can draft TikZ if wanted.
5. [x] **Bolus: removed entirely** (author decision 2026-08-11) — variant
   paragraph, Results paragraph, and `tab:bolus` deleted; 7 tables remain.
6. [x] **MetaboNet: cited as the data source** for HUPA-UCM/T1D-UOM/ReplaceBG
   (settles the patient-count discrepancy). Not cited as a comparator.
7. [ ] Include GPFormer's reciprocal zero-shot number on ABC4D?

## E. Optional / nice-to-have

- [ ] Preprint on medRxiv (PLOS supports concurrent submission).
- [ ] Striking image (single panel, 300–600 dpi, no text).
- [ ] Acknowledgments section (no funding info in it — that goes in the form).
- [ ] Check institutional APC agreement (UCL et al. may have a PLOS flat-fee
  deal — affects who is corresponding author).
