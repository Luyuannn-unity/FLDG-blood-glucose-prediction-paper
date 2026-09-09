# iter15 — full reference check and placeholder sweep (2026-09-09)

Author request: fix the ARISES citation to the full author list, check every
reference with agents (exists? cited correctly?), and confirm the paper has no
placeholders left.

## Method

`references.bib` has 65 entries, 58 of them cited. A script paired each entry
with every passage of the paper that cites it (five input files of 13 entries).
Five agents checked each entry against Crossref, OpenAlex, Semantic Scholar,
arXiv, PubMed/Europe PMC, DataCite, ClinicalTrials.gov, JAEB, Kaggle and open
full texts, and judged whether the cited passage is supported. Their reports
are concatenated in `refcheck_2026-09-09_full.md`.

## Outcome

- All 65 entries exist. No fabricated or unreachable reference.
- Every quoted number in `tab:prior`, `tab:oodprior` and the Discussion was
  confirmed against its source, with one exception (Jaloli, below).
- Citation-use verdicts: 54 supported, 4 partly supported (idf2021, farahmand2025glumind,
  liu2021feddg, zhu2026glullm), 1 number wrong (jaloli2023cnnlstm), 7 uncited.

## Bib fixes applied (`revision/references.bib`)

- **zhu2022arises**: author list corrected to Zhu, Uduku, Li, Herrero, Oliver,
  Georgiou (was Zhu, Kuang, Daniels, Herrero, Li, Georgiou); number 1 added;
  "verify at submission" note removed. Confirmed by Crossref and Europe PMC.
- **"and others" entries** now list the first six authors, which is what
  plos2015.bst prints before "et al.": battelino2019tir, rieke2020future,
  bergenstal2021flair, fang2026mthyponet. Full lists where the paper has few
  authors: vaswani2017attention (8), zhou2021informer (7), sheller2020federated (11).
- **Wrong or missing fields**: zhu2023glugan pages 4906--4917 → 5122--5133;
  zhu2024gpformer now the version of record (2025;29(8):5424--5437);
  zhou2022dgsurvey year 2022 → 2023 (print issue of vol 45(4));
  wolff2026metabonet switched from the arXiv preprint to the Journal of Diabetes
  Science and Technology version (doi 10.1177/19322968261441637, online ahead of
  print, preprint id kept in the note); james2025brist1d now lists all five
  DataCite creators; kaggle2024brist1d uses Kaggle's requested five-author
  citation; teo2024federated adds Nan Liu (erratum 10.1016/j.xcrm.2024.101481);
  alsuhaymi2025t1duom accent and middle initial.
- **Added identifiers**: DOI/volume/pages for li2018mldg, liu2021feddg,
  li2021ditto, mcmahan2017fedavg, karimireddy2020scaffold, wu2021autoformer,
  zhou2021informer; issue numbers for martinsson2020 and li2025fedDGsurvey;
  pages and location for pansheriya2026aegis; URLs for marling2020ohio and
  sergazinov2024glucobench.
- Header note about deliberate truncations replaced.

## Paper wording fixes (`revision/glucose_fl_paper_working.tex`, mirrored to v30)

1. **Author summary, 8.4 million.** The IDF Atlas 10th edition gives only an
   under-20 T1D count; the 8.4 million figure is Gregory et al. 2022. Cite now
   reads `\cite{gregory2022t1dindex}` alone. idf2021 is therefore uncited.
2. **Introduction, GluMind.** The preprint shows glucose dynamics differ between
   populations and that fine-tuning across cohorts forgets, but says nothing
   about devices or sites and does not test unseen populations. Sentence now:
   "But glucose dynamics differ between populations~\cite{farahmand2025glumind},
   demographics and devices differ from site to site, and a model can degrade on
   populations it did not see in training."
3. **Discussion, Jaloli & Cescon.** 9.3 mg/dL was their LSTM comparator; their
   own CNN-LSTM is 9.73 ± 1.34 at 30 min (population level). Changed to 9.7.
4. **GluLLM (three places).** (a) Intro: "improves in-cohort accuracy further"
   contradicted our own table (GluLLM 20.6 vs GPFormer 19.2); now "beats a bank
   of deep-learning baselines in-cohort". (b) `tab:oodprior`: the GluLLM paper
   never states the inputs of its Crossformer, TCN and GRU baselines; those
   cells now read "not stated". (c) Footnote: "Those two sources evaluate on the
   same 46-subject hold-out" → each uses a 46-subject hold-out (GluLLM does not
   say it reuses GPFormer's split), plus a sentence on the unstated inputs.

## Left for the author (also in REQUIRED_FROM_YOU.md)

FedDG wording on "adapted to the federated setting" (author chose the bare cite
in Paul 3); AEGIS "on T1D-UOM" (closed access; LOPO, 15 min and mmol/L are
confirmed); seven uncited entries plus idf2021; Darpit/Dave name order;
optional GPFormer three-days-per-subject note.

## Placeholder sweep

No TODO, TBD, XXX, "???", red text, `\todo`, "[insert" or "citation needed" in
rendered text. Two `%` comment notes remain (author block lines 103–107; data
availability lines 708–711); they never render. `zhu2022arises` was the last
bib note asking for verification at submission.

## Cross-checks that passed

`tab:datasets` ages ABC4D 36 (29–46) = GluGAN Table III; ARISES 40 (30–50) =
the ARISES paper. Teo 2024: 612 studies, 5.2 %. Li 2025: 107 studies, 10
real-world. Sun 2025: five cities, three continents, in-silico. Dexcom G7 MARD
8.2/9.1 %, Libre 3 7.8 %. GPFormer: all eight RMSE values, 46-subject hold-out,
MLDG, decoder convention. GluLLM: 20.6/21.1/21.3/22.1, 46 individuals.
GlucoFM-Bench: 16.71 (4.82), 20.81 (4.26), LSTM, by-time, univariate.
FCNN: 20.23 (3.38), 20.25 (2.60), by-time, CGM + carbs + bolus.

## Resolved (2026-09-09, same day)

- **AEGIS on T1D-UOM: confirmed by the author from the full text.** The paper says: "Using the T1D-UOM dataset, which includes continuous glucose, insulin, nutrition, and activity measurements, we engineer physiologically meaningful features and evaluate the system under a leave-one-patient-out protocol to ensure generalizability to unseen individuals." All four claims about AEGIS (T1D-UOM, leave-one-patient-out, 15-min horizon, mmol/L) are now verified. No change to the paper. Item removed from REQUIRED_FROM_YOU.md.
