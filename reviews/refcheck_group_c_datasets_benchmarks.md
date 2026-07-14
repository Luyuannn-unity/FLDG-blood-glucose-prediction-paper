# Reference Check — Group C: Datasets & External Benchmark Papers

Manuscript: `paper/revision/glucose_fl_paper_working.tex`
Bib: `paper/revision/references.bib`
Authoritative number source (from PDFs): `Benchmark papers/paper_summary.txt`
Checked: 2026-07-07. Verification via arXiv, Crossref, Nature, MDPI (search), ClinicalTrials.gov, IEEE.

## Summary table

| Key | Metadata verdict | Claim/number verdict | Confirmed source | Fix needed |
|-----|------------------|----------------------|------------------|------------|
| hidalgo2024hupaucm | CONFIRMED | n/a (dataset) | DOI 10.1016/j.dib.2024.110559 | none |
| alsuhaymi2025t1duom | CONFIRMED (add issue/pages) | n/a (dataset) | DOI 10.1038/s41597-025-05695-1 | add `number=1`, `pages=1379` |
| wolff2026metabonet | CONFIRMED | n/a (dataset) | arXiv 2601.11505 | none (optional: add note "under review, JDST") |
| aleppo2017replacebg | CONFIRMED | n/a (OOD dataset) | DOI 10.2337/dc16-2482 | none |
| lu2026glucofmbench | PLACEHOLDER → COMPLETABLE | numbers MATCH | arXiv 2606.06881 | fill 5 authors |
| zhu2023fcnn | **DOI WRONG** | numbers MATCH | DOI 10.1109/TBME.2022.3187703 | correct DOI (was .3187033) |
| tan2026uncertainty | PLACEHOLDER → COMPLETABLE | claim (MARD-only) MATCH | arXiv 2603.04955 | fill author names |
| pansheriya2026aegis | PLACEHOLDER → COMPLETABLE | claim (15-min, mmol/L, LOPO) MATCH | DOI 10.1109/CCWC67433.2026.11393699 | fill authors |
| manchanda2025lstm | PLACEHOLDER + **issue# & title wrong** | claim (window-avg RMSE) MATCH | DOI 10.3390/diabetology6100115 | authors, DOI, fix `number` 11→10, title |
| kolev2026benchmark | PLACEHOLDER + **issue# wrong** | claim (synthetic-only) MATCH | DOI 10.3390/app16083928 | authors, DOI, fix `number` 7→8 |
| ABC4D (cohort) | **NO CITATION IN MS** | — | NCT02053051 | add dataset citation |
| ARISES (cohort) | **NO CITATION IN MS** | — | NCT03643692 / npj DM 2022 | add dataset citation |

All four quoted RMSE@30 values in Table `tab:prior` (16.71/4.82, 20.81/4.26, 20.23/3.38, 20.25/2.60) and all four split descriptions **exactly match** `paper_summary.txt`. No number mismatches found.

---

## Detailed notes

### Datasets

**hidalgo2024hupaucm — CONFIRMED.**
"HUPA-UCM diabetes dataset", *Data in Brief* **55**:110559 (2024), DOI 10.1016/j.dib.2024.110559. Authors J.I. Hidalgo, J. Alvarado, M. Botella, A. Aramendi, J.M. Velasco, O. Garnica — match the bib. 25 T1D subjects, FreeStyle Libre 2 + Fitbit Ionic. Also on Mendeley Data (3hbcscwz44) and PMC11214197. No change.

**alsuhaymi2025t1duom (T1D-UOM) — CONFIRMED, incomplete.**
"A longitudinal multimodal dataset of type 1 diabetes", *Scientific Data* **12**(1):1379 (2025), DOI 10.1038/s41597-025-05695-1 (Nature article s41597-025-05695-1; PMC12331950). University of Manchester; Zenodo record 10.5281/zenodo.17361905 (per paper_summary). Bib is missing `number` and `pages`. Add `number={1}`, `pages={1379}`.

**wolff2026metabonet — CONFIRMED.**
"MetaboNet: The Largest Publicly Available Consolidated Dataset for Type 1 Diabetes Management", arXiv **2601.11505** (submitted 2026-01-19). Authors Miriam K. Wolff, Peter Calhoun, Eleonora Maria Aiello, Yao Qin, Sam F. Royston — match the bib exactly. Submitted to JDST. arXiv ID and authors all correct. No change required.

**aleppo2017replacebg — CONFIRMED.**
"REPLACE-BG …", *Diabetes Care* **40**(4):538–545 (2017), DOI 10.2337/dc16-2482 (Crossref-verified). Title, authors, volume/issue/pages all correct. No change.

### External benchmark papers

**lu2026glucofmbench — arXiv ID CONFIRMED; author list COMPLETABLE.**
arXiv 2606.06881 (submitted 2026-06-05) is genuinely "GlucoFM-Bench: Benchmarking Time-Series Foundation Models for Blood Glucose Forecasting."
Full authors: **Baiying Lu, Zhaohui Liang, Ryan Pontius, Shengpu Tang, Temiloluwa Prioleau** (Dartmouth/Emory). Bib currently `author = {Lu, and others}` — replace with the full list.
Number check: quoted HUPA-UCM 16.71 (4.82) and T1D-UOM 20.81 (4.26), both LSTM full-shot, by-time, sd across patients — MATCH paper_summary lines 18-19, 62-69. Correct.
(Note: distinct from arXiv 2605.30865 "GlucoFM: A Dual-Stream Foundation Model" and 2606.18640 "MetaboNet-Bench" — do not confuse.)

**zhu2023fcnn — METADATA MOSTLY OK but DOI IS WRONG.**
Correct DOI is **10.1109/TBME.2022.3187703** (Crossref-verified: title, authors Taiyu Zhu / Kezhi Li / Pau Herrero / Pantelis Georgiou, *IEEE TBME* 70(1):193–204, 2023 all match). The bib DOI `10.1109/TBME.2022.3187033` returns 404 on Crossref — a transposed-digit typo (`033` vs `703`). **Fix the DOI.**
Number check: ARISES 20.23 (3.38), ABC4D 20.25 (2.60), FCNN, by-time (64/16/20), sd across patients — MATCH paper_summary lines 20-21, 102-106. Correct.

**tan2026uncertainty — arXiv ID CONFIRMED; authors COMPLETABLE.**
arXiv 2603.04955 (v2) "Uncertainty quantification in neural network-based glucose prediction for diabetes." Authors: **Hai Siong Tan** (Gryphon Center for A.I. & Theoretical Sciences, Singapore) and **Rafe McBeth** (Univ. of Pennsylvania, Perelman School of Medicine). Bib `author = {Tan, and McBeth, }` — fill initials/names.
Claim check: manuscript says "MARD only" — MATCHES paper_summary line 24, 224 (no RMSE reported; MARD + DTS zone-A only). Correct.

**pansheriya2026aegis — DOI CONFIRMED; authors COMPLETABLE.**
DOI 10.1109/CCWC67433.2026.11393699 (Crossref-verified). "AEGIS: AI-Driven Glucose Prediction and Personalized Insulin Dosing", 2026 IEEE 16th CCWC. Authors: **Yash Kishorbhai Pansheriya** and **Marjan Asadinia** (California State University, Northridge). Bib `author = {Pansheriya, and Asadinia, }` — fill given names.
Claim check: manuscript says AEGIS is by-patient LOPO, 15-min horizon, mmol/L, not comparable at 30 min — MATCHES paper_summary lines 25, 251-266 (best XGBoost 15-min RMSE 0.517 mmol/L; 30+ min abandoned). Correct.

**manchanda2025lstm — PLACEHOLDER; issue number AND title wrong.**
Crossref-verified: DOI **10.3390/diabetology6100115**, *Diabetology* **6**(10):115 (2025). Authors: **Esha Manchanda, Jialiu Zeng, Chih Hung Lo** (Syracuse University). Issues to fix:
- Bib `number = {11}` is WRONG → should be **10**.
- Bib title "Personalized {LSTM} Models for Blood Glucose Prediction …" is not the published title → actual title is "Data-Efficiency with Comparable Accuracy: **Personalized LSTM Neural Network Training** for Blood Glucose Prediction in Type 1 Diabetes Management".
- Add authors and DOI.
Claim check: manuscript says "window-averaged RMSE" (non-comparable) — MATCHES paper_summary lines 23, 182-196 (reported 20.50±5.66 / 22.52±6.38 are 0–60 min window averages, not a 30-min-point RMSE). Correct.

**kolev2026benchmark — PLACEHOLDER; issue number wrong.**
Crossref-verified: DOI **10.3390/app16083928**, *Applied Sciences* **16**(8):3928 (2026). Authors: **Mikhail Kolev, Irina Naskinova, Mariyan Milev, Stanislava Stoilova, Iveta Nikolova** (Univ. of Warmia and Mazury, Poland; Sofia University, Bulgaria). Issues to fix:
- Bib `number = {7}` is WRONG → should be **8**.
- Add authors and DOI.
Claim check: manuscript says "synthetic data only" — MATCHES paper_summary lines 22, 27, 127-132 (all experiments on Bergman-model synthetic data due to HUPA-UCM HTTP-403; no real-data result; no per-dataset breakdown). Correct.

### ABC4D and ARISES cohort citations — MISSING (author note confirmed)

In the manuscript, `hidalgo2024hupaucm` (HUPA-UCM), `alsuhaymi2025t1duom` (T1D-UOM), `aleppo2017replacebg` (ReplaceBG) and `wolff2026metabonet` (MetaboNet) are cited (lines 291-298, 484-486), but **ABC4D and ARISES are named without any `\cite`** (lines 292-293, 313, 486). They lack dedicated dataset citations. Proposed additions below.

- **ABC4D** ≈ trial **NCT02053051** ("Advanced Bolus Calculator for Type 1 Diabetes (ABC4D)", Imperial College London; case-based-reasoning bolus advisor). Registry entry is a citable dataset source. (Originating-paper alternatives if a journal ref is preferred: Reddy et al., *Diabetes Technol. Ther.* 2016 pilot, or Reddy/Herrero et al. 2023 randomized crossover — not independently verified here for the exact n=25 phase-4 cohort used by Zhu et al., so registry is the safe citation.)
- **ARISES** ≈ trial **NCT03643692** ("Adaptive, Real-time, Intelligent System to Enhance Self-care", Imperial College London; 6-week study, 12 T1D adults). The originating dataset/methods paper is **Zhu et al., "Enhancing self-management in type 1 diabetes with wearables and deep learning", *npj Digital Medicine* 5:78 (2022), DOI 10.1038/s41746-022-00626-5** — a stronger academic citation than the registry alone.

---

## Proposed new / corrected BibTeX

```bibtex
% ---- CORRECTED: T1D-UOM (add issue + pages) ----
@article{alsuhaymi2025t1duom,
  title   = {A longitudinal multimodal dataset of type 1 diabetes},
  author  = {Alsuhaymi, Ashwaq and Bilal, Ahmad and Gasca Garcia, Daniel and
             Kongdee, Rujiravee and Lubasinski, Nicole and Thabit, Hood and
             Nutter, Paul and Harper, Simon},
  journal = {Scientific Data},
  volume  = {12},
  number  = {1},
  pages   = {1379},
  year    = {2025},
  doi     = {10.1038/s41597-025-05695-1}
}

% ---- COMPLETED: GlucoFM-Bench (full author list) ----
@misc{lu2026glucofmbench,
  title        = {{GlucoFM-Bench}: Benchmarking Time-Series Foundation Models for
                  Blood Glucose Forecasting},
  author       = {Lu, Baiying and Liang, Zhaohui and Pontius, Ryan and
                  Tang, Shengpu and Prioleau, Temiloluwa},
  year         = {2026},
  eprint       = {2606.06881},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG}
}

% ---- CORRECTED: Zhu et al. FCNN (DOI .3187033 -> .3187703) ----
@article{zhu2023fcnn,
  title   = {Personalized Blood Glucose Prediction for Type 1 Diabetes Using
             Evidential Deep Learning and Meta-Learning},
  author  = {Zhu, Taiyu and Li, Kezhi and Herrero, Pau and Georgiou, Pantelis},
  journal = {IEEE Transactions on Biomedical Engineering},
  volume  = {70},
  number  = {1},
  pages   = {193--204},
  year    = {2023},
  doi     = {10.1109/TBME.2022.3187703}
}

% ---- COMPLETED: Tan & McBeth (author names) ----
@misc{tan2026uncertainty,
  title        = {Uncertainty quantification in neural network-based glucose
                  prediction for diabetes},
  author       = {Tan, Hai Siong and McBeth, Rafe},
  year         = {2026},
  eprint       = {2603.04955},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG}
}

% ---- COMPLETED: AEGIS (author given names) ----
@inproceedings{pansheriya2026aegis,
  title     = {{AEGIS}: {AI}-Driven Glucose Prediction and Personalized Insulin Dosing},
  author    = {Pansheriya, Yash Kishorbhai and Asadinia, Marjan},
  booktitle = {2026 IEEE 16th Annual Computing and Communication Workshop and
               Conference (CCWC)},
  year      = {2026},
  doi       = {10.1109/CCWC67433.2026.11393699}
}

% ---- COMPLETED + CORRECTED: Manchanda (authors, DOI, title, number 11->10) ----
@article{manchanda2025lstm,
  title   = {Data-Efficiency with Comparable Accuracy: Personalized {LSTM} Neural
             Network Training for Blood Glucose Prediction in Type 1 Diabetes
             Management},
  author  = {Manchanda, Esha and Zeng, Jialiu and Lo, Chih Hung},
  journal = {Diabetology},
  volume  = {6},
  number  = {10},
  pages   = {115},
  year    = {2025},
  doi     = {10.3390/diabetology6100115}
}

% ---- COMPLETED + CORRECTED: Kolev (authors, DOI, number 7->8) ----
@article{kolev2026benchmark,
  title   = {A Comprehensive Benchmark of Machine Learning Methods for Blood
             Glucose Prediction in Type 1 Diabetes: A Multi-Dataset Evaluation},
  author  = {Kolev, Mikhail and Naskinova, Irina and Milev, Mariyan and
             Stoilova, Stanislava and Nikolova, Iveta},
  journal = {Applied Sciences},
  volume  = {16},
  number  = {8},
  pages   = {3928},
  year    = {2026},
  doi     = {10.3390/app16083928}
}

% ---- NEW: ABC4D cohort (trial registry) ----
@misc{abc4d_nct,
  title        = {Advanced Bolus Calculator for Type 1 Diabetes ({ABC4D})},
  author       = {{Imperial College London}},
  howpublished = {ClinicalTrials.gov identifier NCT02053051},
  year         = {2014},
  url          = {https://clinicaltrials.gov/study/NCT02053051}
}

% ---- NEW: ARISES cohort (originating paper preferred) ----
@article{zhu2022arises,
  title   = {Enhancing self-management in type 1 diabetes with wearables and
             deep learning},
  author  = {Zhu, Taiyu and Kuang, Lei and Daniels, John and Herrero, Pau and
             Li, Kezhi and Georgiou, Pantelis},
  journal = {npj Digital Medicine},
  volume  = {5},
  pages   = {78},
  year    = {2022},
  doi     = {10.1038/s41746-022-00626-5},
  note    = {ARISES cohort; trial NCT03643692. Verify full author list at submission.}
}
```

## UNVERIFIED / caveats
- **ABC4D originating journal paper**: The exact paper for the n=25 "Phase-4" ABC4D cohort used by Zhu et al. was not pinned to a single DOI here; the NCT02053051 registry is proposed as the safe citation. If a journal citation is required, confirm the specific Reddy et al. ABC4D trial paper before use — UNVERIFIED which one matches n=25.
- **zhu2022arises author list**: proposed from typical ARISES authorship; the full/exact author order was not line-by-line confirmed against the npj DM record — verify at submission (DOI 10.1038/s41746-022-00626-5 and NCT03643692 are confirmed).
- MDPI pages (Kolev, Manchanda) block direct fetch (HTTP 403); their metadata above was confirmed via the **Crossref API**, not the publisher HTML.
