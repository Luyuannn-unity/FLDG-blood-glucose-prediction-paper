# Submission TODO — PLOS Digital Health

Consolidated checklist before submission. Sources: author's list (2026-08-11),
REQUIRED_FROM_YOU.md, START_HERE.md, and the PLOS Digital Health submission
guidelines (https://journals.plos.org/digitalhealth/s/submission-guidelines).
Updated 2026-08-24 after the clean-retrain revision (v30).

## A. Hard blockers (desk-reject or fabrication risk)

- [ ] **Live four-institution rerun of the federated arms, then a final number
  swap.** The current numbers come from the clean rerun on cloud pods. Six
  sentences say the reported numbers came from the live run. (REQUIRED_FROM_YOU
  #13)
- [ ] **Code repository must carry what the paper says it carries.** The Methods
  and the availability statement now promise the cleaning scripts, the split
  manifests, the masked loss, the repaired ABC4D/ARISES timestamps and the
  5-seed configs. The public repo (`fldg-glucose`) still ships the pre-fix
  pipeline and 3-seed configs. (REQUIRED_FROM_YOU #17)
- [ ] **Author block** — names and corresponding email are in (2026-08-18).
  Still open: affiliations for Rui Sun and Taiyu Zhu (`[affiliation to be
  confirmed]`), ORCID for the corresponding author, CRediT roles for all six,
  entered in the submission system. (REQUIRED_FROM_YOU #6)
- [ ] **Decide the single-cohort OOD rows** — keep in `tab:ood`, move to an S1
  Table, or drop. The draft is written for keep. (REQUIRED_FROM_YOU #14)
- [x] ~~Cut the abstract to ≤300 words~~ **Done 2026-08-24: 291 words.** Re-count
  after any edit.
- [x] ~~Cut the author summary to 150–200 words~~ **Done 2026-08-24: 199 words.**
- [x] ~~Data availability statement~~ **Written 2026-08-11:** MetaboNet route for
  the five public cohorts, ABC4D/ARISES on request via the corresponding author,
  code repo live under MIT. Optional: mint a Zenodo DOI at submission.
- [x] ~~Ethics statement~~ **Done 2026-08-11** (UCL IHI LREC, Project ID 1665).
- [x] ~~Seed 46 outputs, remote logs, MLDG update spec, patient-count rule, tex
  merge~~ **All done 2026-08-11** (see iter5–iter9 logs). Superseded anyway by
  the clean retrain of 2026-08-21/22 (seeds 42–46).

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
  boxes, figure placement). `tab:h60` is 9 columns inside `\resizebox`; check
  it is legible.
- [ ] **Figure format check** — figures embedded in the manuscript at first
  submission; captions directly after first citation, labelled "Fig 1" style.
  (High-res TIFF/EPS uploads only needed at revision.)
- [ ] **Reporting checklist** — consider TRIPOD+AI (prediction-model studies).
  Not on PLOS's explicit list, but reviewers of a clinical prediction paper
  often expect it; filling it in also catches gaps (e.g. missing-data handling).
- [ ] **Reference format pass** — Vancouver/ICMJE, first six authors then et al.,
  DOIs written in full, journal abbreviations per NCBI.

## C. Editorial passes (author + Claude, together)

- [x] ~~Justify RMSE@30 as the primary metric~~ **Done 2026-08-11.**
- [ ] **Author read-through of the rewritten sections.** Results, Discussion,
  Abstract, Author summary and Intro contribution 2 were rewritten 2026-08-24
  for the corrected results and the new style rule (simple sentences, no
  semicolons, no em-dash asides). Methods gained a Data quality subsection.
- [ ] **Reference correctness pass** — finish open refcheck items: ARISES full
  author list, ABC4D registry-vs-paper. (REQUIRED_FROM_YOU #8)
- [x] ~~GPFormer framing sanity check~~ **Resolved 2026-08-11:** precursor
  framing removed by author decision.
- [x] ~~Number-consistency pass~~ **Done 2026-08-24** by a 14-agent adversarial
  sweep (numbers vs CSV, claims vs facts, consistency, leftover narrative,
  style, Methods vs pipeline). **Redo after the live rerun.**
- [x] ~~Structural validation~~ **Done 2026-08-24** (`check.py`: env balance,
  labels/refs, cites, style). **Redo after the live rerun.**

## D. Science decisions

1. [x] **Persistence / clinical-metrics finding: NOT reported** (author decision
   2026-08-11). Rationale recorded in REQUIRED_FROM_YOU.md. Don't re-open.
2. [x] **Centralised pooled baseline: in the paper** (2026-08-11). Per-seed
   CSVs on disk and a 60-min row in `tab:h60` since 2026-08-24.
3. [x] **MLDG significance** — resolved by the clean retrain: MLDG beats FedAvg
   at five seeds (p = 0.010 at 30 min, 0.002 at 60 min) and beats local
   training (p = 0.014). Plain FedAvg does not beat local training (p = 0.14).
   The paper says so.
4. [x] **FL architecture figure** — done 2026-08-13 (`fig:system`).
5. [x] **Bolus: removed entirely** (author decision 2026-08-11).
6. [x] **MetaboNet: cited as the data source** for HUPA-UCM/T1D-UOM/ReplaceBG.
   Not cited as a comparator.
7. [x] **GPFormer's reciprocal zero-shot number on ABC4D:** no (author decision
   2026-08-11).
8. [x] **Data-quality fixes go in Methods, not a corrigendum** (author decision
   2026-08-24: the paper is unpublished).

## E. Optional / nice-to-have

- [ ] Preprint on medRxiv (PLOS supports concurrent submission).
- [ ] Striking image (single panel, 300–600 dpi, no text).
- [ ] Acknowledgments section (no funding info in it — that goes in the form).
- [ ] Check institutional APC agreement (UCL et al. may have a PLOS flat-fee
  deal — affects who is corresponding author).
