# Reference Check — Group A (Clinical / Diabetes background + Glucose-prediction models + Transformers)

Manuscript: `paper/revision/glucose_fl_paper_working.tex`
Bib: `paper/revision/references.bib`
Checked: 2026-07-07 against Crossref / arXiv / DBLP / publisher pages / Google Scholar.

## Summary table

| Key | Cited claim (paraphrase) | Metadata | Claim-support | Source URL | Fix |
|---|---|---|---|---|---|
| idf2021 | T1D ~8.4M worldwide, incidence rising | CORRECT | SUPPORTS | https://diabetesatlas.org | none |
| gregory2022t1dindex | 8.4M people with T1D worldwide (2021) | CORRECT | SUPPORTS | https://doi.org/10.1016/S2213-8587(22)00218-2 | none |
| battelino2019tir | International consensus targets for time-in-range | CORRECT | SUPPORTS | https://doi.org/10.2337/dci19-0028 | none |
| vettoretti2020advanced | AI + CGM decision support / insulin-delivery | CORRECT | SUPPORTS | https://doi.org/10.3390/s20143870 | none |
| bekiari2018ap | Artificial pancreas / closed-loop efficacy | CORRECT | SUPPORTS | https://doi.org/10.1136/bmj.k1310 | none |
| martinsson2020 | RNN + variance estimation baselines | CORRECT | SUPPORTS | https://doi.org/10.1007/s41666-019-00059-y | none |
| marling2020ohio | Standardized datasets/challenges (OhioT1DM) | CORRECT | SUPPORTS | https://ceur-ws.org/Vol-2675/paper11.pdf | none |
| sergazinov2023gluformer | Personalized, uncertainty-aware transformer, SOTA | CORRECT (minor: pages) | SUPPORTS | https://doi.org/10.1109/ICASSP49357.2023.10096419 | verify `pages` |
| sergazinov2024glucobench | Transformer forecasters reporting SOTA | CORRECT | PARTIAL | https://arxiv.org/abs/2410.05780 | see note (benchmark, not a forecaster) |
| ghimire2024generalize | Cross-cohort transfer is an open question | CORRECT | SUPPORTS | https://doi.org/10.1371/journal.pone.0310801 | none |
| farahmand2025glumind | Model degrades on unseen populations | CORRECT | SUPPORTS | https://arxiv.org/abs/2509.18457 | none |
| vaswani2017attention | The transformer | CORRECT (truncated authors) | SUPPORTS | https://arxiv.org/abs/1706.03762 | expand authors at submission |
| zhou2021informer | Long-horizon time-series transformer variant | CORRECT (truncated authors) | SUPPORTS | https://ojs.aaai.org/index.php/AAAI/article/view/17325 | expand authors; optional add DOI 10.1609/aaai.v35i12.17325 |
| wu2021autoformer | Long-horizon time-series transformer variant | CORRECT | SUPPORTS | https://arxiv.org/abs/2106.13008 | none |

No WRONG-field metadata errors of substance. One PARTIAL (over-stretch) and two minor field notes below. Nothing left UNVERIFIED.

---

## Detailed notes

### idf2021 & gregory2022t1dindex
**Sentence (l.157–158):** "Type 1 diabetes (T1D) affects an estimated 8.4 million people worldwide and its incidence is rising in many regions~\cite{idf2021,gregory2022t1dindex}."
- **gregory2022**: Confirmed — Lancet Diabetes & Endocrinology 10(10):741–760, 2022, DOI 10.1016/S2213-8587(22)00218-2. The study explicitly reports ~8.4M people with T1D worldwide in 2021 and projects a 60–107% rise by 2040. Authors, volume, issue, pages, DOI all match. SUPPORTS the "8.4 million" and "rising" claims directly.
- **idf2021**: IDF Diabetes Atlas 10th ed. (2021), International Diabetes Federation, Brussels — a standard reference work; url resolves. Standard corporate-author @misc entry. Reasonable support for the "rising incidence worldwide" framing (though the precise 8.4M figure is gregory2022's). CORRECT/SUPPORTS.

### battelino2019tir
**Sentence (l.164–165):** "...time in range, for which international consensus targets have been defined~\cite{battelino2019tir}."
- Confirmed exactly: Diabetes Care 42(8):1593–1603, 2019, DOI 10.2337/dci19-0028. This is the ATTD International Consensus on Time in Range defining clinical CGM targets. Metadata CORRECT; claim SUPPORTS precisely.

### vettoretti2020advanced & bekiari2018ap
**Sentence (l.166–169):** "...can trigger preemptive alerts, inform bolus and snack decisions, and close the loop in automated insulin-delivery systems~\cite{vettoretti2020advanced,bekiari2018ap}."
- **vettoretti2020**: Sensors 20(14):3870, 2020, DOI 10.3390/s20143870. Review of AI + CGM for advanced diabetes management (glucose prediction, bolus calculators, decision support). CORRECT/SUPPORTS.
- **bekiari2018**: BMJ 361:k1310, 2018, DOI 10.1136/bmj.k1310. Systematic review/meta-analysis of artificial-pancreas (closed-loop) treatment in outpatient T1D. CORRECT/SUPPORTS the "close the loop in automated insulin-delivery systems" clause.

### martinsson2020
**Sentence (l.171–174):** "Recurrent architectures with predictive variance estimation established strong baselines on benchmark cohorts~\cite{martinsson2020}."
- J. Healthcare Informatics Research 4:1–18, 2020, DOI 10.1007/s41666-019-00059-y. Authors Martinsson, Schliep, Eliasson, Mogren confirmed. Paper is RNN/LSTM with predictive variance estimation, benchmarked on OhioT1DM. Metadata CORRECT; claim SUPPORTS exactly.

### marling2020ohio
**Sentence (l.174–175):** "...standardised datasets and challenges shaped much of the early evaluation~\cite{marling2020ohio}."
- CEUR-WS Vol-2675, KDH@ECAI 2020, pages 71–74. Confirmed (paper11.pdf). The OhioT1DM dataset paper, tied to the BGLP Challenge. Metadata CORRECT; claim SUPPORTS ("standardised datasets and challenges").

### vaswani2017attention
**Sentence (l.175–177):** "The transformer~\cite{vaswani2017attention}..."
- "Attention Is All You Need," NeurIPS 2017 (arXiv 1706.03762). Canonical. Metadata CORRECT. Author list is deliberately truncated with "and others" (flagged in bib header) — expand to full 8-author list at submission. Claim SUPPORTS.

### zhou2021informer & wu2021autoformer
**Sentence (l.176–177):** "...its long-horizon time-series variants~\cite{zhou2021informer,wu2021autoformer}..."
- **zhou2021informer**: AAAI 2021, pp. 11106–11115, DOI 10.1609/aaai.v35i12.17325 (DBLP: conf/aaai/ZhouZPZLXZ21). Long-sequence time-series forecasting transformer. Metadata CORRECT (authors truncated "and others" — expand; optionally add the AAAI DOI). SUPPORTS.
- **wu2021autoformer**: NeurIPS 2021 (arXiv 2106.13008). Authors Wu, Xu, Wang, Long confirmed. Long-term series forecasting transformer. Metadata CORRECT; SUPPORTS.

### sergazinov2023gluformer
**Sentence (l.178–179):** "...personalised, uncertainty-aware transformer forecasters reporting state-of-the-art accuracy~\cite{sergazinov2023gluformer,sergazinov2024glucobench}."
- Confirmed published at IEEE ICASSP 2023 (DBLP; proceedings, Rhodes, Greece). DOI 10.1109/ICASSP49357.2023.10096419 resolves to IEEE Xplore doc 10096419. Authors Sergazinov, Armandpour, Gaynanova confirmed. This is a personalized transformer with uncertainty quantification reporting SOTA — SUPPORTS the claim directly.
- **Minor field note:** bib lists `pages = {1--5}`; the printed ICASSP proceedings pagination is a single page number (one source cites p. 1201). The "1–5" is likely the 5-page manuscript's own pagination. Verify/normalize the `pages` field against IEEE Xplore before submission. Not a substantive error.

### sergazinov2024glucobench
Same sentence as above.
- Confirmed: ICLR 2024 (arXiv 2410.05780). Authors Sergazinov, Chun, Rogovchenko, Fernandes, Kasman, Gaynanova all confirmed. Metadata CORRECT.
- **Claim-support: PARTIAL / mild over-stretch.** GlucoBench is a *curated dataset collection + benchmark* paper (its two tasks are predictive accuracy and uncertainty quantification), not itself a "personalised, uncertainty-aware transformer forecaster reporting state-of-the-art accuracy." The Gluformer citation fully carries that claim; GlucoBench supports the surrounding evidence base (benchmarks, uncertainty evaluation) but is not a forecasting model reporting SOTA. Consider rephrasing so GlucoBench is cited as the benchmark rather than as one of the "forecasters," or move it to a benchmark-context sentence.

### ghimire2024generalize
**Sentence (l.180–181):** "...how well they transfer across cohorts is an open question~\cite{ghimire2024generalize}."
- PLOS ONE 19(9):e0310801, 2024, DOI 10.1371/journal.pone.0310801. Authors Ghimire, Celik, Gerdes, Omlin confirmed. Paper explicitly studies how well deep glucose models generalize across different datasets. Metadata CORRECT; claim SUPPORTS precisely.

### farahmand2025glumind
**Sentence (l.182–183):** "...a model can degrade on populations it did not see in training~\cite{farahmand2025glumind}."
- GluMind, arXiv 2509.18457 (2025). Full author list matches. Paper targets robust cross-population glucose forecasting and mitigates catastrophic forgetting — i.e., it is motivated by exactly the degradation-on-unseen-populations problem. Metadata CORRECT (preprint); claim SUPPORTS.
