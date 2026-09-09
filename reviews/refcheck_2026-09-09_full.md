# Full reference check, 2026-09-09

Five agents (one per group of 13 entries) checked every entry of `revision/references.bib` for existence, metadata, and whether the citing passage is supported by the source. Inputs were built by a script that paired each entry with every passage citing it. Nothing here was edited by the agents; fixes were applied afterwards (see `iter15_revisions.md`).

# Reference check, group 1

Checked 2026-09-09 against Crossref, PubMed, Semantic Scholar, OpenAlex, arXiv, CEUR-WS, ICLR/NeurIPS proceedings and NCBI Bookshelf. No file under the paper directory was touched.

## Summary table

| key | exists | metadata issues | citation use | action needed |
|---|---|---|---|---|
| idf2021 | EXISTS | none (10th edn, 2021, IDF, Brussels confirmed) | PARTLY SUPPORTED: Atlas 10th edn gives 1.2 million under-20s with T1D and no all-ages figure; 8.4 million is not in it | drop idf2021 from the "8.4 million" sentence (gregory2022t1dindex alone carries the number), or cite it only for general T1D burden |
| gregory2022t1dindex | EXISTS | group author "International Diabetes Federation Diabetes Atlas Type 1 Diabetes in Adults Special Interest Group" omitted (sits between Donaghue and Magliano in PubMed); Crossref expands it to 24 names | SUPPORTED: "about 8.4 (95% UI 8.1-8.8) million individuals worldwide with type 1 diabetes" in 2021 | optional: add the group author |
| battelino2019tir | EXISTS | "and others" hides 39 of 42 authors | SUPPORTED | none (see full first-six list below) |
| vettoretti2020advanced | EXISTS | none | SUPPORTED | none |
| bekiari2018ap | EXISTS | none | PARTLY SUPPORTED: shows closed-loop AID works (40 RCTs, 1027 participants); says nothing about forecasting | none required; the forecasting clause rests on vettoretti2020advanced |
| clarke1987 | EXISTS | none | SUPPORTED (zone A = within 20% of reference, or both <70 mg/dL) | none |
| martinsson2020 | EXISTS | missing number = {1}; online Dec 2019, issue Mar 2020 | SUPPORTED | add number = {1} |
| marling2020ohio | EXISTS | none; no URL | SUPPORTED | add url = {https://ceur-ws.org/Vol-2675/paper11.pdf} |
| sergazinov2023gluformer | EXISTS | none | SUPPORTED | none (optionally note arXiv:2209.04526) |
| sergazinov2024glucobench | EXISTS | no URL/arXiv id | SUPPORTED | add url = {https://openreview.net/forum?id=cUSNs8nGaV} (arXiv:2410.05780) |
| ghimire2024generalize | EXISTS | none | SUPPORTED | none |
| farahmand2025glumind | EXISTS | none (arXiv id and 12 authors match) | PARTLY SUPPORTED: shows glucose dynamics differ across populations and catastrophic forgetting when fine-tuned across cohorts; does not test unseen populations, does not mention devices or sites, and is a T2D/healthy cohort | reword: cite it for "glucose dynamics differ between populations"; support "degrades on populations not seen in training" with a different source (e.g. ghimire2024generalize or the manuscript's own OOD results) |
| vaswani2017attention | EXISTS | "and others" hides 5 of 8 authors; no volume | SUPPORTED | give all 8 authors; add volume = {30} |

## Per-entry notes

### idf2021
- Found: International Diabetes Federation. IDF Diabetes Atlas, 10th edition. Brussels: IDF, 2021. Full text on NCBI Bookshelf (https://www.ncbi.nlm.nih.gov/books/NBK581934/); IDF page https://idf.org/news-and-resources/resources/idf-diabetes-atlas-2021/. Edition, year, publisher and city all confirmed.
- Discrepancies: none. (diabetesatlas.org returned HTTP 403, so the URL could not be checked live; it is the IDF's official Atlas domain.)
- Full author list: n/a (corporate author).
- Cited for: "T1D affects an estimated 8.4 million people worldwide [idf2021, gregory2022t1dindex]".
- Verdict on use: PARTLY SUPPORTED. The 10th edition's "Global picture" and "Summary" chapters say "In total, 1,211,900 children and adolescents younger than 20 years are estimated to have type 1 diabetes globally" and give no all-ages T1D estimate. The figure 8.4 million does not appear. The 8.4 million comes from Gregory et al. 2022 (the T1D Index), which is the second citation in the same bracket, so the sentence is still backed. Note: IDF later published "Type 1 diabetes estimates in children and adults" (IDF Diabetes Atlas Reports, 2022) which, per a search snippet, states 8.75 million (95% UI 8.4-9.1) people with T1D in 2022; I could not open that PDF (403), and its number differs from 8.4 million, so it is not a drop-in replacement.

### gregory2022t1dindex
- Found: Gregory GA, Robinson TIG, Linklater SE, Wang F, Colagiuri S, de Beaufort C, Donaghue KC, International Diabetes Federation Diabetes Atlas Type 1 Diabetes in Adults Special Interest Group, Magliano DJ, Maniam J, Orchard TJ, Rai P, Ogle GD. "Global incidence, prevalence, and mortality of type 1 diabetes in 2021 with projection to 2040: a modelling study." Lancet Diabetes Endocrinol. 2022;10(10):741-760. doi:10.1016/S2213-8587(22)00218-2. PMID 36113507.
- Discrepancies: the bib lists the 12 named individuals correctly but omits the collective group author. Crossref expands the group into 24 individual names (adds Harding, Wander, Zhang, Li, Karuranga, Chen, Sun, Xie, Oram, Zhou, Jenkins, Ma). Title, journal, volume, issue, pages, year, DOI all match.
- Full author list: n/a (bib has no "and others").
- Cited for: T1D affects an estimated 8.4 million people worldwide.
- Verdict on use: SUPPORTED. Abstract (via Semantic Scholar): "In 2021, there were about 8.4 (95% uncertainty interval 8.1-8.8) million individuals worldwide with type 1 diabetes."

### battelino2019tir
- Found: Battelino T, Danne T, Bergenstal RM, et al. "Clinical Targets for Continuous Glucose Monitoring Data Interpretation: Recommendations From the International Consensus on Time in Range." Diabetes Care. 2019;42(8):1593-1603. doi:10.2337/dci19-0028. Crossref lists 42 authors.
- Discrepancies: none.
- Full author list: 42 authors, so first six: Tadej Battelino, Thomas Danne, Richard M. Bergenstal, Stephanie A. Amiel, Roy Beck, Torben Biester. Last author: Moshe Phillip.
- Cited for: CGM "underpins consensus glycaemic targets such as time in range".
- Verdict on use: SUPPORTED. This is the international consensus document that set the time-in-range targets from CGM data.

### vettoretti2020advanced
- Found: Vettoretti M, Cappon G, Facchinetti A, Sparacino G. "Advanced Diabetes Management Using Artificial Intelligence and Continuous Glucose Monitoring Sensors." Sensors. 2020;20(14):3870. doi:10.3390/s20143870. PMID 32664432, PMC7412387.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: a reliable 30-60 min forecast "can trigger preemptive alerts, inform bolus and snack decisions, and close the loop in automated insulin-delivery systems".
- Verdict on use: SUPPORTED. Abstract: CGM sensors "provide in real-time, every 1-5 min, the current blood glucose concentration and its rate-of-change, two key pieces of information for improving the determination of exogenous insulin administration and the prediction of forthcoming adverse events, such as hypo-/hyper-glycemia"; the review covers "personalized insulin bolus calculation, adaptive tuning of bolus calculator parameters and glucose prediction" for T1D decision support.

### bekiari2018ap
- Found: Bekiari E, Kitsios K, Thabit H, Tauschmann M, Athanasiadou E, Karagiannis T, Haidich AB, Hovorka R, Tsapas A. "Artificial pancreas treatment for outpatients with type 1 diabetes: systematic review and meta-analysis." BMJ. 2018;361:k1310. doi:10.1136/bmj.k1310. PMID 29669716, PMC5902803.
- Discrepancies: none (PubMed confirms volume 361).
- Full author list: n/a.
- Cited for: same sentence as vettoretti2020advanced, chiefly "close the loop in automated insulin-delivery systems".
- Verdict on use: PARTLY SUPPORTED. It pools "40 studies (1027 participants with data for 44 comparisons)" and finds time in the near-normoglycaemic range "was significantly higher" with artificial pancreas systems. That backs the clinical value of closed-loop AID, but the paper does not discuss glucose forecasting or prediction horizons. As a paired citation it is reasonable; on its own it would not support the forecasting claim.

### clarke1987
- Found: Clarke WL, Cox D, Gonder-Frederick LA, Carter W, Pohl SL. "Evaluating Clinical Accuracy of Systems for Self-Monitoring of Blood Glucose." Diabetes Care. 1987;10(5):622-628. doi:10.2337/diacare.10.5.622. PMID 3677983.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: the Clarke error grid; zone A = forecasts within 20% of reference, or below 70 mg/dL when reference is also below 70 mg/dL.
- Verdict on use: SUPPORTED. The abstract describes the error grid analysis that "takes into account 1) the absolute value of the system-generated glucose value, 2) the absolute value of the reference blood glucose value, 3) the relative difference between these two values, and 4) the clinical significance of this difference." The full text is paywalled so I could not read the zone table directly; the zone A rule quoted by the manuscript (within 20%, or both in the hypoglycaemic range <70 mg/dL) is the standard definition attributed to this paper in secondary sources (Wikipedia, Profil error-grid explainer, common EGA implementations).

### martinsson2020
- Found: Martinsson J, Schliep A, Eliasson B, Mogren O. "Blood Glucose Prediction with Variance Estimation Using Recurrent Neural Networks." J Healthc Inform Res. 2020;4(1):1-18. Published online 1 Dec 2019. doi:10.1007/s41666-019-00059-y. PMID 35415439, PMC8982803.
- Discrepancies: bib lacks number = {1}. Year 2020 matches the issue date (Crossref/Semantic Scholar show 2019 for online-first).
- Full author list: n/a.
- Cited for: forecasting progressed "through recurrent networks".
- Verdict on use: SUPPORTED. Abstract: "an approach for predicting blood glucose levels for diabetics up to 1 h into the future ... based on recurrent neural networks trained in an end-to-end fashion ... comparable to the state of the art on the Ohio T1DM dataset."

### marling2020ohio
- Found: Marling C, Bunescu R. "The OhioT1DM Dataset for Blood Glucose Level Prediction: Update 2020." In: Bach K, Bunescu R, Marling C, Wiratunga N (eds). Knowledge Discovery in Healthcare Data 2020, 5th Int. Workshop (KDH 2020) co-located with ECAI 2020, Santiago de Compostela, 29-30 Aug 2020. CEUR Workshop Proceedings vol. 2675, pp. 71-74. https://ceur-ws.org/Vol-2675/paper11.pdf
- Discrepancies: none. A URL would help readers.
- Full author list: n/a.
- Cited for: "evaluated on standardised datasets and challenges".
- Verdict on use: SUPPORTED. From the paper (read in full): the dataset "was developed to promote and facilitate research in blood glucose level prediction", "contains eight weeks' worth of continuous glucose monitoring, insulin, physiological sensor, and self-reported life-event data for each of 12 people with type 1 diabetes", and "was first released in 2018 for the first Blood Glucose Level Prediction (BGLP) Challenge"; "a CGM blood glucose level every 5 minutes" from Medtronic Enlite sensors.

### sergazinov2023gluformer
- Found: Sergazinov R, Armandpour M, Gaynanova I. "Gluformer: Transformer-Based Personalized Glucose Forecasting with Uncertainty Quantification." ICASSP 2023 - IEEE Int. Conf. on Acoustics, Speech and Signal Processing, 2023, pp. 1-5. doi:10.1109/ICASSP49357.2023.10096419. arXiv:2209.04526.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: "transformer forecasters reporting state-of-the-art accuracy on glucose".
- Verdict on use: SUPPORTED. Abstract: "Deep learning models achieve state-of-the art results in predicting blood glucose trajectories" and "We empirically demonstrate the superiority of our method over existing state-of-the-art techniques both in terms of accuracy and uncertainty on the synthetic and benchmark glucose data sets", using "the Transformer architecture".

### sergazinov2024glucobench
- Found: Sergazinov R, Chun E, Rogovchenko V, Fernandes N, Kasman N, Gaynanova I. "GlucoBench: Curated List of Continuous Glucose Monitoring Datasets with Prediction Benchmarks." ICLR 2024 (proceedings: https://proceedings.iclr.cc/paper_files/paper/2024/hash/4c12e97f2e05304a451e18c9c945036f-Abstract-Conference.html; OpenReview id cUSNs8nGaV; arXiv:2410.05780).
- Discrepancies: none in the fields given; no URL or arXiv id. Author "Nathaniel J. Fernandes" appears as "Nathaniel Fernandes" in the proceedings (harmless).
- Full author list: n/a.
- Cited for: "curated benchmarks standardising their evaluation".
- Verdict on use: SUPPORTED. Abstract: most methods are "evaluated on small, private datasets, impeding reproducibility"; GlucoBench offers "a consolidated repository of curated publicly available CGM datasets", "a standardized task list", and "a set of benchmark models with established baseline performance".

### ghimire2024generalize
- Found: Ghimire S, Celik T, Gerdes M, Omlin CW. "Deep learning for blood glucose level prediction: How well do models generalize across different data sets?" PLOS ONE. 2024;19(9):e0310801. doi:10.1371/journal.pone.0310801.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: "How well they transfer to cohorts they never saw is the open question".
- Verdict on use: SUPPORTED. The paper trains FFNN, CNN, LSTM, TCN and SAN on four datasets (OhioT1DM 12 patients, DCLP3 112, DCLP5 101 children, RT 451) and "the model initially trained on one dataset underwent evaluation using the test set of other datasets". One caveat: its own conclusion is that "all the models performed statistically consistently across datasets proving their generalizable capability", so it poses the question rather than reporting failure; the manuscript's phrasing ("open question") is fair to that.

### farahmand2025glumind
- Found: Farahmand E, Azghan RR, Taheri Chatrudi N, Ansu-Baidoo VY, Kim E, Gudur GK, Malu M, Krueger O, Thomaz E, Pedrielli G, Turaga P, Ghasemzadeh H. "GluMind: Multimodal Parallel Attention and Knowledge Retention for Robust Cross-Population Blood Glucose Forecasting." arXiv:2509.18457v1, 22 Sep 2025. https://arxiv.org/abs/2509.18457
- Discrepancies: none. All 12 authors and the arXiv id match.
- Full author list: n/a.
- Cited for: "glucose dynamics, demographics, and devices differ from site to site, and a model can degrade on populations it did not see in training".
- Verdict on use: PARTLY SUPPORTED. The paper says "a person's blood glucose response to lifestyle factors highly depends on the person's insulin resistance status, resulting in significantly different glucose levels among healthy individuals, people with prediabetes, and patients with diabetes", and shows that a baseline "suffers from the catastrophic forgetting issue" when "fine-tuned sequentially" across AI-READI cohorts (323 healthy, 207 pre-T2DM, 258 T2DM oral, 108 T2DM insulin; 896 participants, three US sites). It does not evaluate a model on an unseen population without fine-tuning, does not discuss device or site differences, and the cohorts are healthy/T2D rather than T1D. So it backs "dynamics differ across populations" and "performance drops when moving between cohorts", but not "devices differ from site to site" or degradation on never-seen populations as such.

### vaswani2017attention
- Found: Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser L, Polosukhin I. "Attention Is All You Need." Advances in Neural Information Processing Systems 30 (NIPS 2017). https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html; arXiv:1706.03762.
- Discrepancies: no volume (30); "NeurIPS" is the current name, the 2017 proceedings say "NIPS 2017" (acceptable). "and others" is not needed for an 8-author paper.
- Full author list: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin (8 authors).
- Cited for: forecasting progressed "to the transformer".
- Verdict on use: SUPPORTED. This is the paper that introduced the Transformer.


---

# Reference check, group 2

Checked 2026-09-09. Sources used: Crossref API, arXiv abstract pages, ar5iv full text, OpenAlex API, PMLR proceedings pages, Semantic Scholar (one hit before rate-limit), WebSearch. DBLP was blocked (403 Anubis) and Semantic Scholar returned 429 for most calls, so venue data came from arXiv "comments", PMLR pages and OpenAlex instead.

## Summary table

| key | exists | metadata issues | citation use | action needed |
|---|---|---|---|---|
| zhou2021informer | EXISTS | "and others" hides 4 of 7 authors; volume/issue/pages missing | SUPPORTED | fill full author list (7 authors); add volume 35, number 12, pages 11106--11115 |
| wu2021autoformer | EXISTS | no volume/pages/URL (NeurIPS has no DOI) | SUPPORTED | optional: add volume 34, pages 22419--22430 |
| mcmahan2017fedavg | EXISTS | no volume/pages | SUPPORTED | optional: add PMLR 54, pages 1273--1282 |
| li2020fedprox | EXISTS | none material | SUPPORTED | none |
| karimireddy2020scaffold | EXISTS | no volume/pages | SUPPORTED | optional: add PMLR 119, pages 5132--5143 |
| rieke2020future | EXISTS | "and others" (17 authors) | SUPPORTED | none (list first 6 + et al. per PLOS style) |
| sheller2020federated | EXISTS | "and others" hides 8 of 11 authors | SUPPORTED | fill full author list (11 authors) |
| kaissis2020secure | EXISTS | none (Rueckert vs Rückert spelling only) | SUPPORTED | none |
| li2018mldg | EXISTS | DOI missing; volume/pages missing | SUPPORTED | add DOI 10.1609/aaai.v32i1.11596, volume 32, pages 3490--3497 |
| liu2021feddg | EXISTS | DOI/pages missing | PARTLY SUPPORTED | add DOI 10.1109/CVPR46437.2021.00107; reword "adapted to the federated setting~\cite{liu2021feddg}" (see notes) |
| deng2020apfl | EXISTS | none; arXiv-only is correct | SUPPORTED | none |
| li2021ditto | EXISTS | no volume/pages | SUPPORTED | optional: add PMLR 139, pages 6357--6368; consider noting Ditto's symbol is lambda, not mu |
| li2021moon | EXISTS | DOI/pages missing | uncited | cite it or delete the entry |

## Per-entry notes

### zhou2021informer
- Found: "Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting". Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, Wancai Zhang. Proceedings of the AAAI Conference on Artificial Intelligence 35(12):11106--11115, 2021. DOI 10.1609/aaai.v35i12.17325 (Crossref). arXiv:2012.07436, comment "AAAI2021".
- Discrepancies: author list truncated with "and others" although only 7 authors; volume, number and pages absent. Title, venue, year, DOI correct.
- Full author list: Zhou, Haoyi; Zhang, Shanghang; Peng, Jieqi; Zhang, Shuai; Li, Jianxin; Xiong, Hui; Zhang, Wancai (7).
- Cited for: (1) a time-series variant of the transformer; (2) the forecaster is an "Informer-style" encoder--decoder Transformer with full attention; (3) single-shot decoding with a start-token warm-up plus zero placeholders and time marks for all decoder positions.
- Verdict on use: SUPPORTED. The Informer paper defines the decoder input as X_de = Concat(X_token, X_0), where the start token is "a L_token long sequence in the input sequence, such as an earlier slice before the output sequence", X_0 is a zero placeholder that "contains target sequence's time stamp", and "our proposed decoder predicts outputs by one forward procedure rather than the time consuming 'dynamic decoding'". This matches passage 3 exactly. Passage 2 is honest that the manuscript uses dense attention, so it does not claim Informer's ProbSparse mechanism; "Informer-style" refers to the seq2seq layout. Passage 1 is trivially supported.

### wu2021autoformer
- Found: "Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting". Haixu Wu, Jiehui Xu, Jianmin Wang, Mingsheng Long. Advances in Neural Information Processing Systems 34, pp. 22419--22430, 2021. arXiv:2106.13008 (v5, Jan 2022). Proceedings PDF: https://proceedings.neurips.cc/paper_files/paper/2021/file/bcc0d400288793e8bdcd7c19a8ac0c2b-Paper.pdf (URL and page range came via WebSearch, not a direct fetch of the proceedings page; OpenAlex only indexes the arXiv version, DOI 10.48550/arxiv.2106.13008).
- Discrepancies: none in the fields present. No volume/pages; NeurIPS papers have no Crossref DOI, so nothing is "missing" there.
- Full author list: n/a (all four already listed).
- Cited for: a time-series variant of the transformer.
- Verdict on use: SUPPORTED. Abstract: "Going beyond Transformers, we design Autoformer as a novel decomposition architecture with an Auto-Correlation mechanism ... In long-term forecasting, Autoformer yields state-of-the-art accuracy". It is a transformer-derived forecaster, which is all the sentence claims.

### mcmahan2017fedavg
- Found: "Communication-Efficient Learning of Deep Networks from Decentralized Data". Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, Blaise Agüera y Arcas. Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (AISTATS), PMLR 54:1273--1282, 2017. https://proceedings.mlr.press/v54/mcmahan17a.html . arXiv:1602.05629.
- Discrepancies: none. Volume/pages absent (optional).
- Full author list: n/a.
- Cited for: (1) FL lets sites train locally and exchange only model updates so no raw record leaves the institution; (2) "FedAvg" baseline is standard federated averaging.
- Verdict on use: SUPPORTED. Abstract: "We advocate an alternative that leaves the training data distributed on the mobile devices, and learns a shared model by aggregating locally-computed updates ... We present a practical method ... based on iterative model averaging". The paper is framed around mobile devices, not hospitals, but the mechanism the manuscript describes is exactly FedAvg. Passage 2 is the canonical attribution.

### li2020fedprox
- Found: "Federated Optimization in Heterogeneous Networks". Tian Li, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, Ameet Talwalkar, Virginia Smith. Proceedings of Machine Learning and Systems (MLSys) 2020, Austin TX, March 2020. arXiv:1812.06127 (v5, comment "MLSys 2020"). DBLP record conf/mlsys/LiSZSTS20 (seen via search result; DBLP itself blocked).
- Discrepancies: none. Pages not verified, so none suggested.
- Full author list: n/a.
- Cited for: (1) a variant motivated by FedAvg degrading under heterogeneity; (2) FedProx adds a proximal term (mu/2)||w - w_global||^2 to each client objective to limit client drift; manuscript uses mu = 0.05.
- Verdict on use: SUPPORTED. Full text Eq. (2): "min_w h_k(w; w^t) = F_k(w) + mu/2 ||w - w^t||^2", and "It addresses the issue of statistical heterogeneity by restricting the local updates to be closer to the initial (global) model". The abstract reports FedProx is "significantly more stable and accurate ... relative to FedAvg" in heterogeneous settings. The paper tuned mu in {0.001, 0.01, 0.1, 1}; 0.05 is the manuscript's own choice and is not attributed to the source, so no problem.

### karimireddy2020scaffold
- Found: "SCAFFOLD: Stochastic Controlled Averaging for Federated Learning". Sai Praneeth Karimireddy, Satyen Kale, Mehryar Mohri, Sashank Reddi, Sebastian Stich, Ananda Theertha Suresh. Proceedings of the 37th International Conference on Machine Learning (ICML), PMLR 119:5132--5143, 2020. https://proceedings.mlr.press/v119/karimireddy20a.html . arXiv:1910.06378.
- Discrepancies: none. Volume/pages absent (optional).
- Full author list: n/a.
- Cited for: a variant motivated by FedAvg degrading when client distributions diverge.
- Verdict on use: SUPPORTED. Abstract: "Federated Averaging (FedAvg) suffers from 'client-drift' when the data is heterogeneous (non-iid), resulting in unstable and slow convergence. ... SCAFFOLD ... uses control variates (variance reduction) to correct for the 'client-drift'".

### rieke2020future
- Found: "The future of digital health with federated learning". npj Digital Medicine 3(1):119, 2020. DOI 10.1038/s41746-020-00323-1 (Crossref). 17 authors.
- Discrepancies: none. "and others" is acceptable for 17 authors.
- Full author list: more than 15 authors. First six: Rieke, Nicola; Hancox, Jonny; Li, Wenqi; Milletarì, Fausto; Roth, Holger R.; Albarqouni, Shadi. Total 17 (remaining: Bakas, Galtier, Landman, Maier-Hein, Ourselin, Sheller, Summers, Trask, Xu, Baust, Cardoso).
- Cited for: FL as a design widely adopted in medical machine learning.
- Verdict on use: SUPPORTED. It is a perspective on FL for healthcare: data "remains underutilized due to data silos and privacy restrictions" and FL lets organisations "collaborate on model development while keeping sensitive patient information secure". Appropriate as a general medical-FL reference.

### sheller2020federated
- Found: "Federated learning in medicine: facilitating multi-institutional collaborations without sharing patient data". Scientific Reports 10(1):12598, 2020. DOI 10.1038/s41598-020-69250-1 (Crossref). 11 authors.
- Discrepancies: "and others" hides 8 of 11 authors.
- Full author list: Sheller, Micah J.; Edwards, Brandon; Reina, G. Anthony; Martin, Jason; Pati, Sarthak; Kotrotsou, Aikaterini; Milchenko, Mikhail; Xu, Weilin; Marcus, Daniel; Colen, Rivka R.; Bakas, Spyridon (11).
- Cited for: FL as a design widely adopted in medical machine learning.
- Verdict on use: SUPPORTED. Abstract: "federated learning among 10 institutions results in models reaching 99% of the model quality achieved with centralized data", trained without sharing patient data. Direct empirical support for the claim.

### kaissis2020secure
- Found: "Secure, privacy-preserving and federated machine learning in medical imaging". Georgios A. Kaissis, Marcus R. Makowski, Daniel Rückert, Rickmer F. Braren. Nature Machine Intelligence 2(6):305--311, 2020. DOI 10.1038/s42256-020-0186-1 (Crossref, OpenAlex).
- Discrepancies: none material. Crossref/OpenAlex spell the third author "Rückert"; the bib has "Rueckert" (the author's own usual English spelling). Either is fine.
- Full author list: n/a.
- Cited for: FL as a design widely adopted in medical machine learning.
- Verdict on use: SUPPORTED. Abstract (OpenAlex): "we present an overview of current and next-generation methods for federated, secure and privacy-preserving artificial intelligence with a focus on imaging applications". A perspective, not evidence of adoption, but fine grouped with rieke2020future and sheller2020federated.

### li2018mldg
- Found: "Learning to Generalize: Meta-Learning for Domain Generalization". Da Li, Yongxin Yang, Yi-Zhe Song, Timothy M. Hospedales. Proceedings of the AAAI Conference on Artificial Intelligence 32(1), 2018, pp. 3490--3497 (pages from Semantic Scholar). DOI 10.1609/aaai.v32i1.11596 (Crossref). arXiv:1710.03463.
- Discrepancies: DOI missing; volume/pages missing. Title, authors, venue, year correct.
- Full author list: n/a.
- Cited for: (1) MLDG simulates train/test domain shift within each update so the model learns to generalise; (2) the manuscript's MLDG variant splits each batch by patient into meta-train and meta-test halves.
- Verdict on use: SUPPORTED. Abstract: "Our algorithm simulates train/test domain shift during training by synthesizing virtual testing domains within each mini-batch. The meta-optimization objective requires that steps to improve training domain performance should also improve testing domain performance." Full text: "at each learning iteration we split the original S source domains into S-V meta-train domains and V meta-test domains", objective argmin F(Theta) + beta G(Theta - alpha F'(Theta)). MLDG splits by domain; the manuscript treats patients as domains, which is a faithful analogue. "rather than memorise" is the manuscript's gloss, not a quote.

### liu2021feddg
- Found: "FedDG: Federated Domain Generalization on Medical Image Segmentation via Episodic Learning in Continuous Frequency Space". Quande Liu, Cheng Chen, Jing Qin, Qi Dou, Pheng-Ann Heng. 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 1013--1023. DOI 10.1109/CVPR46437.2021.00107 (OpenAlex). arXiv:2103.06030, "Accepted to CVPR 2021".
- Discrepancies: DOI and pages missing. Otherwise correct.
- Full author list: n/a.
- Cited for: MLDG "adapted to the federated setting".
- Verdict on use: PARTLY SUPPORTED. FedDG does cite MLDG (its ref [24]: "Meta-learning based methods [8, 24] need to use multi-source data of different distributions to construct virtual training and virtual testing domains within each minibatch") and does set up "the local training as an episodic meta-learning scheme, which learns generalizable model parameters by simulating train/test domain shift explicitly". So it is a genuine precedent for episodic meta-learning DG inside FL. But its adaptation is not the manuscript's: in FedDG "we consider the raw input x as meta-train and its counterparts t generated from frequency space as meta-test", with the transformed data produced by exchanging amplitude spectra between clients ("continuous frequency space interpolation"). The manuscript instead splits a batch by patient. As written, "adapted to the federated setting~\cite{liu2021feddg}" reads as though the patient-split scheme comes from FedDG. Suggest: "following the episodic-learning idea of FedDG~\cite{liu2021feddg}, but splitting each client batch by patient rather than using frequency-space augmentation".

### deng2020apfl
- Found: "Adaptive Personalized Federated Learning". Yuyang Deng, Mohammad Mahdi Kamani, Mehrdad Mahdavi. arXiv:2003.13461, v1 30 Mar 2020, v3 6 Nov 2020. No journal-ref on arXiv; OpenAlex and WebSearch found no peer-reviewed version.
- Discrepancies: none. Citing it as an arXiv preprint is correct.
- Full author list: n/a.
- Cited for: (1) APFL learns an adaptive mixture of the global and a local model; (2) per-client mixture alpha v_i + (1-alpha) w with adaptively updated alpha, initial 0.25.
- Verdict on use: SUPPORTED. Full text: personalized model "h_alpha_i = alpha_i h_loc,i + (1 - alpha_i) h-bar" and Algorithm 1 ("Local Descent APFL") keeps "v-bar_i = alpha_i v_i + (1 - alpha_i) w_i", so alpha weights the personal model and (1-alpha) the global one, matching the manuscript's formula. Section 4.2 "Adaptive alpha update": "we can infer it empirically during optimization". alpha is per client. The initial value 0.25 and the "decoupled APFL variant" are the manuscript's own choices and are not attributed to the paper. (I could not extract the exact alpha gradient equation from ar5iv, but the adaptive update is confirmed by the section title and text.)

### li2021ditto
- Found: "Ditto: Fair and Robust Federated Learning Through Personalization". Tian Li, Shengyuan Hu, Ahmad Beirami, Virginia Smith. Proceedings of the 38th International Conference on Machine Learning (ICML), PMLR 139:6357--6368, 2021. https://proceedings.mlr.press/v139/li21h.html . arXiv:2012.04221, "Accepted by ICML 2021".
- Discrepancies: none. Volume/pages absent (optional).
- Full author list: n/a.
- Cited for: (1) Ditto regularises each client's personal model toward the global one; (2) personal model pulled toward the global one by a proximal term, mu in {0.01, 0.1, 1.0}.
- Verdict on use: SUPPORTED. Full text objective: "h_k(v_k; w*) := F_k(v_k) + lambda/2 ||v_k - w*||^2", and "the hyperparameter lambda controls the interpolation between local and global models". This is exactly what the manuscript says. Minor: Ditto calls the strength lambda; the manuscript writes mu (same symbol as FedProx). Not wrong, but a reader may think they share a hyperparameter; consider "lambda" or a note.

### li2021moon
- Found: "Model-Contrastive Federated Learning". Qinbin Li, Bingsheng He, Dawn Song. 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pp. 10708--10717. DOI 10.1109/CVPR46437.2021.01057 (OpenAlex). arXiv:2103.16257, "Accepted by CVPR 2021".
- Discrepancies: DOI and pages missing; otherwise correct.
- Full author list: n/a.
- Cited for: nothing. The entry is cited nowhere in the paper.
- Verdict on use: n/a (uncited). Either cite it where heterogeneity-handling FL variants are listed (next to FedProx and SCAFFOLD) or delete the entry so the bibliography has no orphans.


---

# Reference check, group 3

Checked 2026-09-09 against Crossref, OpenAlex, arXiv API, PubMed/Europe PMC, DataCite, the NeurIPS proceedings site, ar5iv, data.bris and the arXiv HTML of the MetaboNet paper. Semantic Scholar (429) and DBLP (bot wall) were unreachable; nothing depended on them.

## Summary table

| key | exists | metadata issues | citation use | action needed |
|---|---|---|---|---|
| fallah2020perfedavg | EXISTS | none wrong; could add volume 33, pages 3557--3568, arXiv:2002.07948 | SUPPORTED | none (optional: add pages/URL) |
| chen2018fedmeta | EXISTS | none | SUPPORTED | none |
| li2025fedDGsurvey | EXISTS | missing number={4} | SUPPORTED | add number={4} |
| fedcl2023 | EXISTS | none | uncited | cite it or delete the entry |
| flda2023 | EXISTS | journal is "Reliability Engineering & System Safety" (ampersand) | uncited | cite it or delete the entry |
| fedadv2022 | EXISTS | none | uncited | cite it or delete the entry |
| zhou2022dgsurvey | EXISTS | vol 45(4) pp 4396--4415 is the April 2023 print issue; year=2022 is the online date | SUPPORTED | set year={2023} (or keep 2022 and drop volume/number/pages) |
| hidalgo2024hupaucm | EXISTS | none | SUPPORTED | none |
| alsuhaymi2025t1duom | EXISTS | "Gasca García" (accent) and "Nutter, Paul W." per publisher; trivial | SUPPORTED | none (optional: fix accent, add middle initial) |
| wolff2026metabonet | EXISTS | now published in J Diabetes Sci Technol (online 26 Apr 2026, DOI 10.1177/19322968261441637); bib cites the arXiv preprint only | SUPPORTED | update to journal version or add its DOI; journal title spells "Data Set" |
| aleppo2017replacebg | EXISTS | collective author "REPLACE-BG Study Group" omitted; trivial | SUPPORTED | none (optional: add "and {the REPLACE-BG Study Group}") |
| james2025brist1d | EXISTS | author list wrong: DataCite lists 5 creators, bib lists only James | SUPPORTED | fix author list |
| james2025brist1dpaper | EXISTS | none (arXiv v1 only; no journal version found) | uncited | cite it (natural companion to james2025brist1d) or delete |

## Per-entry notes

### fallah2020perfedavg
- Found: "Personalized Federated Learning with Theoretical Guarantees: A Model-Agnostic Meta-Learning Approach", Alireza Fallah, Aryan Mokhtari, Asuman Ozdaglar. Advances in Neural Information Processing Systems 33 (NeurIPS 2020), pp. 3557--3568. No DOI. https://proceedings.neurips.cc/paper/2020/hash/24389bfe4fe2eba8bf9aa9203a44cdad-Abstract.html ; arXiv:2002.07948 (arXiv title is the shorter "Personalized Federated Learning: A Meta-Learning Approach", v4 23 Oct 2020, comment "To appear in ... NeurIPS 2020"). OpenAlex W3099314130.
- Discrepancies: none. Optional: add volume={33}, pages={3557--3568}, url.
- Full author list: n/a (3 authors, all listed).
- Cited for: "Meta-learning approaches adapt the model-agnostic meta-learning objective to federation".
- Verdict on use: SUPPORTED — abstract: "We show this problem can be studied within the Model-Agnostic Meta-Learning (MAML) framework. Inspired by this connection, we study a personalized variant of the well-known Federated Averaging algorithm".

### chen2018fedmeta
- Found: "Federated Meta-Learning with Fast Convergence and Efficient Communication", Fei Chen, Mi Luo, Zhenhua Dong, Zhenguo Li, Xiuqiang He. arXiv:1802.07876, v1 22 Feb 2018, v2 14 Dec 2019. No journal-ref or DOI on arXiv; no published venue found.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: same sentence as above (meta-learning approaches adapt the MAML objective to federation).
- Verdict on use: SUPPORTED — Introduction (ar5iv full text): "We integrate gradient based meta-learning algorithms MAML and Meta-SGD into the framework for illustration." Abstract: "a parameterized algorithm (or meta-learner) is shared, instead of a global model in previous approaches."

### li2025fedDGsurvey
- Found: "Federated Domain Generalization: A Survey", Ying Li, Xingwei Wang, Rongfei Zeng, Praveen Kumar Donta, Ilir Murturi, Min Huang, Schahram Dustdar. Proceedings of the IEEE 113(4):370--410, 2025 (Crossref: print April 2025, online 20 Aug 2025). DOI 10.1109/JPROC.2025.3596173. arXiv:2306.01334 (v2 1 Mar 2024). OpenAlex W4413360092.
- Discrepancies: bib has no number field; issue is 4. Everything else matches.
- Full author list: n/a (7 authors, all listed).
- Cited for: "Bringing domain generalisation into federation is an active area".
- Verdict on use: SUPPORTED — abstract: "there has been a surge of interest in federated domain generalization (FDG) in recent years ... This paper presents the first survey of recent advances in this area." Note: the survey's own taxonomy is "federated domain alignment, data manipulation, learning strategies, and aggregation optimization"; the manuscript's "two of its method families" (meta-learning, personalisation) is the manuscript's own grouping, not the survey's. The citation sits on "active area", so this is fine as written.

### fedcl2023
- Found: "FedCL: Federated contrastive learning for multi-center medical image classification", Zhenbing Liu, Fengfeng Wu, Yumeng Wang, Mengyu Yang, Xipeng Pan. Pattern Recognition 143:109739, Nov 2023. DOI 10.1016/j.patcog.2023.109739 (Crossref).
- Discrepancies: none.
- Full author list: n/a.
- Cited for: nothing; uncited in the paper.
- Verdict on use: n/a (uncited). Cite it or delete the entry.

### flda2023
- Found: "Federated multi-source domain adversarial adaptation framework for machinery fault diagnosis with data privacy", Ke Zhao, Junchen Hu, Haidong Shao, Jiabei Hu. Reliability Engineering & System Safety 236:109246, Aug 2023. DOI 10.1016/j.ress.2023.109246 (Crossref).
- Discrepancies: journal name uses "&" not "and" (cosmetic).
- Full author list: n/a.
- Cited for: nothing; uncited in the paper.
- Verdict on use: n/a (uncited). Cite it or delete the entry.

### fedadv2022
- Found: "Federated adversarial domain generalization network: A novel machinery fault diagnosis method with data privacy", Rui Wang, Weiguo Huang, Mingkuan Shi, Jun Wang, Changqing Shen, Zhongkui Zhu. Knowledge-Based Systems 256:109880, Nov 2022. DOI 10.1016/j.knosys.2022.109880 (Crossref).
- Discrepancies: none.
- Full author list: n/a.
- Cited for: nothing; uncited in the paper.
- Verdict on use: n/a (uncited). Cite it or delete the entry.

### zhou2022dgsurvey
- Found: "Domain Generalization: A Survey", Kaiyang Zhou, Ziwei Liu, Yu Qiao, Tao Xiang, Chen Change Loy. IEEE Trans. Pattern Anal. Mach. Intell. 45(4):4396--4415, April 2023 (PubMed 35914036: pubdate 2023 Apr; early access online 4 Aug 2022). DOI 10.1109/TPAMI.2022.3195549. arXiv:2103.02503 (v7 12 Aug 2022).
- Discrepancies: bib mixes the 2022 early-access year with the 2023 print volume/issue/pages. Either year={2023}, or year={2022} without volume/number/pages. Author list, title, DOI all match.
- Full author list: n/a.
- Cited for: definition of domain generalisation, "generalise to patients, and even whole cohorts, it never trained on (domain generalisation)".
- Verdict on use: SUPPORTED — abstract: "Domain generalization (DG) aims to achieve OOD generalization by using only source data for model learning."

### hidalgo2024hupaucm
- Found: "HUPA-UCM diabetes dataset", J. Ignacio Hidalgo, Jorge Alvarado, Marta Botella, Aranzazu Aramendi, J. Manuel Velasco, Oscar Garnica. Data in Brief 55:110559, 2024 (online 27 May 2024, CC BY-NC-ND 4.0). DOI 10.1016/j.dib.2024.110559. PMID 38948410, PMC11214197.
- Discrepancies: none.
- Full author list: n/a (6 authors, all listed).
- Cited for: one of four T1D CGM federated-client datasets, distinct study/population/device; publicly available through MetaboNet.
- Verdict on use: SUPPORTED — abstract: "acquired from 25 people with type 1 diabetes mellitus (T1DM). CGM data was acquired by FreeStyle Libre 2 CGMs, and Fitbit Ionic smartwatches were used ... for at least 14 days." MetaboNet lists HUPA-UCM in its fully public subset (22 subjects after MetaboNet's overlap filter, "FreeStyle Libre 2: 100%"). Facts for cross-checking elsewhere in the manuscript: 25 participants in the source, 22 in MetaboNet; FreeStyle Libre 2; Spain (UCM/HUPA); at least 14 days per person.

### alsuhaymi2025t1duom
- Found: "A longitudinal multimodal dataset of type 1 diabetes", Ashwaq Alsuhaymi, Ahmad Bilal, Daniel Gasca García, Rujiravee Kongdee, Nicole Lubasinski, Hood Thabit, Paul W. Nutter, Simon Harper. Scientific Data 12(1):1379, 7 Aug 2025. DOI 10.1038/s41597-025-05695-1. PMID 40775218, PMC12331950. Data: Zenodo 10.5281/zenodo.15806142, CC BY 4.0.
- Discrepancies: trivial. Publisher spells "Gasca García" and "Paul W. Nutter"; bib has "Gasca Garcia" and "Nutter, Paul". Volume/issue/article number/year/DOI match.
- Full author list: n/a (8 authors, all listed).
- Cited for: one of four T1D CGM federated-client datasets; publicly available through MetaboNet.
- Verdict on use: SUPPORTED — abstract: "longitudinal (3-month) real-world data collected from 17 PwT1D participants" with "blood glucose levels; basal and bolus insulin dosages; nutritional intake ...". MetaboNet lists T1D-UOM in its public subset (14 subjects, 0.1 patient-years of overlapping CGM+insulin). Facts for cross-checking elsewhere: 17 participants (14 in MetaboNet), University of Manchester, 12-week study, data collected 1 Oct 2023 to 3 Sep 2024, CGM via LibreView / Dexcom Clarity / Medtronic CareLink exports (mixed sensors), pumps Tandem t:slim X2, MiniMed 780G, Omnipod 5 plus MDI users, Garmin Forerunner 45 wearable.

### wolff2026metabonet
- Found: arXiv:2601.11505, "MetaboNet: The Largest Publicly Available Consolidated Dataset for Type 1 Diabetes Management", Miriam K. Wolff, Peter Calhoun, Eleonora Maria Aiello, Yao Qin, Sam F. Royston; v1 16 Jan 2026, v2 22 Apr 2026, cs.LG, comment "submitted to JDST". Now published: Journal of Diabetes Science and Technology, online 26 Apr 2026, DOI 10.1177/19322968261441637, PMID 42035352, title in journal "...Consolidated Data Set..."; no volume/issue/pages assigned yet (PubMed "as supplied by publisher").
- Discrepancies: bib is the arXiv preprint only. The journal version exists; add its DOI or switch to @article with journal={Journal of Diabetes Science and Technology}, year={2026}, doi={10.1177/19322968261441637}, note={Online ahead of print}. Author list and eprint id are correct.
- Full author list: n/a (5 authors, all listed).
- Cited for: (1) "recently released resource that consolidates public T1D datasets into a single harmonised schema on a common 5-minute grid"; (2) HUPA-UCM, T1D-UOM, ReplaceBG, BrisT1D and Flair "are publicly available through the MetaboNet consolidation".
- Verdict on use: SUPPORTED — full text (arXiv v2): "resampling the datasets into a tabular format, with a homogeneous 5-minute time grid, and standardizing units and feature names"; abstract: "Multiple publicly available T1D datasets were consolidated into a unified resource ... distributed as a fully public subset available for immediate download at https://metabo-net.org/". The public subset table lists all five: Flair (113 subjects, Guardian 3), ReplaceBG (208, Dexcom G4), BrisT1D (19, mixed devices, 52.6% G6), HUPA-UCM (22, FreeStyle Libre 2), T1D-UOM (14). MetaboNet total: 3135 subjects, 1228 patient-years.

### aleppo2017replacebg
- Found: "REPLACE-BG: A Randomized Trial Comparing Continuous Glucose Monitoring With and Without Routine Blood Glucose Monitoring in Adults With Well-Controlled Type 1 Diabetes", Grazia Aleppo, Katrina J. Ruedy, Tonya D. Riddlesworth, Davida F. Kruger, Anne L. Peters, Irl Hirsch, Richard M. Bergenstal, Elena Toschi, Andrew J. Ahmann, Viral N. Shah, Michael R. Rickels, Bruce W. Bode, Athena Philis-Tsimikas, Rodica Pop-Busui, Henry Rodriguez, Emily Eyth, Anuj Bhargava, Craig Kollman, Roy W. Beck, and the REPLACE-BG Study Group. Diabetes Care 40(4):538--545, April 2017 (online 16 Feb 2017). DOI 10.2337/dc16-2482. PMID 28209654, PMC5864100.
- Discrepancies: the collective author "REPLACE-BG Study Group" is omitted; the 19 named authors match exactly. Trivial.
- Full author list: n/a (19 named authors, all listed).
- Cited for: ReplaceBG as a held-out T1D CGM cohort; publicly available through MetaboNet.
- Verdict on use: SUPPORTED — abstract: 226 adults aged 18+ (mean 44 +/- 14) with T1D for at least 1 year, insulin pump users, HbA1c at or below 9.0%, randomised 2:1 to CGM-only (149) vs CGM+BGM (77) for 26 weeks. MetaboNet public subset: "ReplaceBG: 208 subjects; Dexcom G4: 100%; 6-month". Facts for cross-checking elsewhere: 226 enrolled in the trial vs 208 in MetaboNet; Dexcom G4 Platinum; adults; US multicentre trial, published 2017.

### james2025brist1d
- Found (DataCite + data.bris page): "BrisT1D-Open Dataset", creators Sam Gordon James, Miranda Armstrong, Aisling O'Kane, Harry Emerson, Zahraa Abdallah (all University of Bristol). Publisher University of Bristol, published 29 April 2025, CC BY 4.0. DOI 10.5523/bris.33z5jc8fa6tob21ptrugzqog08, https://data.bris.ac.uk/data/dataset/33z5jc8fa6tob21ptrugzqog08/ . (Crossref returns 404 for this DOI because it is DataCite-registered; that is expected.)
- Discrepancies: author field lists only James; the DOI record has five creators. Fix to "James, Sam Gordon and Armstrong, Miranda and O'Kane, Aisling and Emerson, Harry and Abdallah, Zahraa". Title, year, publisher, DOI correct.
- Full author list: Sam Gordon James, Miranda Armstrong, Aisling O'Kane, Harry Emerson, Zahraa Abdallah (5).
- Cited for: BrisT1D as a held-out T1D CGM cohort; publicly available through MetaboNet.
- Verdict on use: SUPPORTED — record description: "a longitudinal study in which 24 young adults with Type 1 Diabetes (T1D) in the UK were given smartwatches ... During the six-month study, participants donated the data collected by their T1D devices and smartwatches". MetaboNet public subset: "BrisT1D: 19 subjects, real-world observational, mixed devices, 52.6% used G6". Facts for cross-checking elsewhere: 24 participants in the source, 19 in MetaboNet; UK young adults; six months; mixed CGM devices.

### james2025brist1dpaper
- Found: arXiv:2507.17757, "BrisT1D Dataset: Young Adults with Type 1 Diabetes in the UK using Smartwatches", Sam Gordon James, Miranda Elaine Glynis Armstrong, Aisling Ann O'Kane, Harry Emerson, Zahraa S. Abdallah. v1 submitted 7 May 2025 (only version), cs.HC (cs.LG secondary), "13 pages, 14 figures", CC BY 4.0. No journal-ref or DOI beyond 10.48550/arXiv.2507.17757; searches for a GigaScience / Scientific Data / Data in Brief version found nothing (the GigaScience giaf134 hit is an unrelated paper).
- Discrepancies: none.
- Full author list: n/a (5 authors, all listed).
- Cited for: nothing; uncited in the paper.
- Verdict on use: n/a (uncited). It is the natural companion to james2025brist1d; either cite it next to the dataset DOI or delete the entry.


---

# Reference check, group 4

Checked 2026-09-09. Sources used: Crossref, OpenAlex, Semantic Scholar, PubMed e-utilities, Europe PMC full-text XML, arXiv API and PDFs, ClinicalTrials.gov API v2, the JAEB dataset page, the Kaggle competition overview (via a text-render proxy), and the author-accepted PDFs of GPFormer, GluGAN and FCNN on UCL Discovery. Publisher pages for SAGE, Springer, MDPI and Nature blocked direct fetches; the Jaloli full text was reached through a text-render proxy of the SAGE page.

## Summary table

| key | exists | metadata issues | citation use | action needed |
|---|---|---|---|---|
| kaggle2024brist1d | EXISTS | Author given as "University of Bristol"; Kaggle's own requested citation names five people (James, Armstrong, O'Kane, Emerson, Abdallah). Ran 18 Sep–29 Nov 2024. | SUPPORTED (60-min horizon and RMSE confirmed on the Kaggle overview; mmol/L confirmed via the dataset paper the competition data was reformatted from) | optional: use Kaggle's citation authors; add access date |
| bergenstal2021flair | EXISTS | 22 authors; bib lists 3 + "and others". PLOS style lists the first six then et al. | SUPPORTED | list first six authors |
| zhu2024gpformer | EXISTS | Version of record is 2025;29(8):5424–5437 (early access 16 Jul 2024). Bib has year 2024 and no volume/issue/pages. | SUPPORTED: all eight quoted RMSE values, the 46-subject hold-out, MLDG, zero-shot transfer, and the decoder design confirmed. One protocol caveat (only the first 3 days of each subject's data were used). | add volume 29, number 8, pages 5424--5437; set year 2025 |
| zhu2026glullm | EXISTS | none (journal styles itself eBioMedicine) | PARTLY SUPPORTED: 20.6/21.1/21.3/22.1 and the 46-individual test set confirmed. Source never states the baselines' inputs, never says its split is the same as GPFormer's, and its 20.6 is worse than GPFormer's 19.2, so "improves in-cohort accuracy further" is not supported by the numbers. | reword three claims (see notes) |
| jeffries2026metabonetbench | EXISTS | arXiv prints "Miriam Wolff" (no "K."); current version v2, 25 Jun 2026 | uncited | cite or drop |
| jaloli2023cnnlstm | EXISTS | none | PARTLY SUPPORTED: 15-minute grid and rolling by-patient split that re-admits test patients confirmed verbatim. "9.3 mg/dL" matches the paper's LSTM comparator (9.28 ± 1.31), not its own CNN-LSTM (9.73 ± 1.34); patient-wise value is 14.04 ± 4.47. | change 9.3 to 9.7 (or "9.3–9.7") |
| fang2026mthyponet | EXISTS | 15 authors; bib has three initial-only names + "and others" | uncited | cite or drop; if kept, list first six with full names |
| jaeb_flair | EXISTS | none material (no year field; bib title uses "---" where the page uses "-") | SUPPORTED | none (optionally add year) |
| abc4d_nct | EXISTS | none (bib uses the brief title; official title is "Clinical Assessment of an Advanced Bolus Calculator for Type 1 Diabetes (ABC4D)") | SUPPORTED | none |
| zhu2023glugan | EXISTS | pages wrong: bib 4906--4917, every record says 5122--5133 | SUPPORTED (Table III gives median (IQR) age for ABC4D and ARISES) | fix pages to 5122--5133 |
| zhu2022arises | EXISTS | none; corrected author list confirmed | SUPPORTED | none |
| lu2026glucofmbench | EXISTS | none | SUPPORTED: 16.71 (4.82), 20.81 (4.26), LSTM, by-time split, univariate CGM, SD over participants, LSTM strongest under full-shot all confirmed | none |
| zhu2023fcnn | EXISTS | none | SUPPORTED: 20.23 (3.38) ARISES, 20.25 (2.60) ABC4D, by-time 80/20 split, CGM + carbohydrate + bolus insulin all confirmed | none |

## Per-entry notes

### kaggle2024brist1d
- Found: "BrisT1D Blood Glucose Prediction Competition", Kaggle community competition, https://www.kaggle.com/competitions/brist1d. Opened 18 Sep 2024 17:00 UTC, final deadline 29 Nov 2024 23:55 UTC. Kaggle's requested citation: "Sam Gordon James, Miranda Elaine Glynis Armstrong, Aisling Ann O'Kane, Harry Emerson, and Zahraa S. Abdallah. BrisT1D Blood Glucose Prediction Competition. https://kaggle.com/competitions/brist1d, 2024. Kaggle." The BrisT1D dataset paper (arXiv:2507.17757, p. 10) says the dataset "was reformatted and used to challenge participants to predict blood glucose an hour in the future using the past six hours of device data" and its reference 29 cites the competition with the same five authors.
- Discrepancies: author field "University of Bristol" is an organisation stand-in; Kaggle asks for the five named authors. Year 2024 is right. No access date.
- Full author list: n/a (bib has no "and others"), but see the five names above.
- Cited for: BrisT1D competition targets a 60-minute horizon in mmol/L, so it is not comparable to the manuscript's 30-minute mg/dL numbers.
- Numbers checked: 60-minute horizon: confirmed ("forecast blood glucose levels one hour ahead using the previous six hours"; "RMSE between the predicted blood glucose levels an hour into the future and the actual values"). mmol/L: the Kaggle data page would not render (JS only, three attempts); confirmed indirectly from the dataset paper, Table 6, where the processed-state "bg" column is in mmol/L and the competition data is a reformatting of that processed state.
- Verdict on use: SUPPORTED. The claim is exactly what the competition does.

### bergenstal2021flair
- Found: Bergenstal RM et al., "A comparison of two hybrid closed-loop systems in adolescents and young adults with type 1 diabetes (FLAIR): a multicentre, randomised, crossover trial", The Lancet 2021;397(10270):208–219, doi 10.1016/S0140-6736(20)32514-9, PMID 33453783 (Crossref and PubMed agree).
- Discrepancies: none in title, journal, volume, issue, pages, year, DOI.
- Full author list: 22 authors. First six exactly: Richard M Bergenstal, Revital Nimri, Roy W Beck, Amy Criego, Lori Laffel, Desmond Schatz. (Then Battelino, Danne, Weinzimer, Sibayan, Johnson, Bailey, Calhoun, Carlson, Isganaitis, Bello, Albanese-O'Neill, Dovc, Biester, Weyman, Hood, Phillip.)
- Cited for: Flair is a hybrid closed-loop (automated insulin delivery) cohort.
- Numbers checked: none quoted. Trial facts: 113 participants aged 14–29, MiniMed 670G vs an advanced hybrid closed-loop system, two 12-week crossover periods (PubMed abstract).
- Verdict on use: SUPPORTED. Title and abstract confirm both arms are hybrid closed-loop. The follow-on statement that automated delivery suppresses glycaemic variability is the manuscript's own reasoning, not attributed to this trial, so nothing more is needed.

### zhu2024gpformer
- Found: Zhu T, Afentakis I, Li K, Armiger R, Hill N, Oliver N, Georgiou P, "Multi-Horizon Glucose Prediction Across Populations With Deep Domain Generalization", IEEE J Biomed Health Inform 2025;29(8):5424–5437, doi 10.1109/JBHI.2024.3428921, PMID 39012743, early access 16 Jul 2024. Author-accepted PDF at https://discovery.ucl.ac.uk/id/eprint/10197097/.
- Discrepancies: bib year 2024 with no volume/issue/pages; the version of record is 2025, vol. 29, no. 8, pp. 5424–5437 (Crossref, PubMed, OpenAlex agree). Author list matches (PubMed spells the fifth author "Neil E Hill").
- Full author list: n/a.
- Cited for: (1) a Transformer trained with MLDG on one large cohort transfers zero-shot to external cohorts; (2) decoder input convention (label_len warm-up + zero placeholders, time-of-day marks supplied for all decoder positions); (3) ReplaceBG RMSE at 30 and 60 min for GPFormer, N-BEATS, Bi-LSTM, ARIMA, SVR; (4) 46-subject hold-out, 5-min grid, point error at the horizon.
- Numbers checked against Table II ("Regression metrics for evaluating the glucose prediction performance"), REPLACE rows:
  - RMSE@30: GPFormer 19.2 confirmed; N-BEATS 21.2 confirmed; Bi-LSTM 21.7 confirmed; ARIMA 28.1 confirmed; SVR 37.4 confirmed.
  - RMSE@60: GPFormer 32.3 confirmed; N-BEATS 34.1 confirmed; Bi-LSTM 34.7 confirmed.
  - 46-subject hold-out: confirmed ("a hold-out testing set consisting of 46 T1D subjects", split "on individual basis", stratified by age and gender).
  - Point error at the horizon on a 5-min grid: confirmed ("i represents the ith timestep in the prediction horizon, such as i = t+6 for a 30-minute prediction horizon"; 24 steps to 2 h).
  - MLDG and zero-shot: confirmed ("we applied meta-learning for domain generalization (MLDG)"; external datasets ABC4D, OhioT1DM, GVAS used as hold-out test sets).
  - Decoder: confirmed. Decoder input is the last L' = 6 steps plus zeros for the future ("future glucose levels are represented via zeros"), with timestamps for all positions (Fig. 1b "Future timestamps"; Table IV decoder output [:, 30, 5] = label length 6 + prediction length 24). Sparse MHSA "inspired by Informer".
  - Inputs "CGM": confirmed as CGM plus sine/cosine time-of-day; "we did not use meal and insulin bolus data as model input".
- Verdict on use: SUPPORTED. Two caveats for the comparison table note: (a) GPFormer kept "only the initial three days of data" per REPLACE-BG subject (Section II-A), so its 46-subject hold-out is 3 days per subject, not the full record; the manuscript's note that all rows share the same protocol could mention this. (b) The note's sentence "Note that GPFormer additionally uses sp..." is cut off in the extract, so I could not check its ending; the source's extras are sparse attention, a quantile loss, and time-of-day marks.

### zhu2026glullm
- Found: Zhu T, Howson J, Nevado-Holgado A, "Empowering digital health management with on-device large language models for glucose prediction: a model development and validation study", eBioMedicine 2026;129:106343, doi 10.1016/j.ebiom.2026.106343, PMID 42349253, PMCID PMC13320499 (open access; full text read from Europe PMC XML).
- Discrepancies: none (three authors, volume, article number, year, DOI all match).
- Full author list: n/a.
- Cited for: (1) a language-model backbone improves in-cohort accuracy further; (2) ReplaceBG RMSE@30 for GluLLM, Crossformer, TCN, GRU with inputs "CGM + insulin + EHR"; (3) same 46-subject hold-out as GPFormer; (4) point error at 30 min on a 5-min grid.
- Numbers checked against Table 2 ("Regression metrics for glucose prediction (mean ± SD) on the held-out REPLACE-BG test set and external Móstoles cohort at 30-min and 60-min horizons"), 30-min RMSE:
  - GluLLM 20.6: confirmed (20.6 ± 3.5). Crossformer 21.1: confirmed (21.1 ± 3.6). TCN 21.3: confirmed (21.3 ± 3.7). GRU 22.1: confirmed (22.1 ± 3.7). (NBeats is 21.4 ± 3.7 there.)
  - 46-subject test set: confirmed ("a development set comprising 180 individuals and a hold-out testing set of 46 individuals", participant-disjoint).
  - 5-min grid: confirmed (L = 72, tau = 12 for 6 h context and 1 h horizon; CGM every 5 min).
  - Point error at 30 min: consistent but not stated in so many words. Table 2 reports metrics "at 30- and 60-min prediction horizons, following standard evaluation settings"; the sequence-level "global RMSE ... comparing predicted sequences with actual CGM sequences" is a separate figure (Fig. 2). Formulas are in the supplement, which I could not reach.
  - Inputs "CGM + insulin + EHR" for GluLLM: confirmed in substance (CGM in date-time form, "when available, combined with insulin bolus information", EHR prompt with age, sex, BMI, HbA1c).
  - Inputs "CGM + insulin + EHR" for Crossformer, TCN, GRU: NOT CHECKABLE. The paper does not say what the 15 deep-learning baselines received; it only says a model-agnostic meta-learning framework was applied to the non-LLM models.
  - "Same 46-subject hold-out" as GPFormer: NOT SUPPORTED as written. Both papers use a 180/46 split, but GluLLM does not cite GPFormer or say it reuses that split.
- Verdict on use: PARTLY SUPPORTED. Three rewordings: (1) "Those two sources evaluate on the same 46-subject hold-out" -> "each evaluates on a 46-subject hold-out"; (2) label the Crossformer/TCN/GRU inputs as "as in GluLLM (not stated)" or drop the input column for those rows; (3) "a language-model backbone improves in-cohort accuracy further" is true relative to GluLLM's own baselines ("outperformed 15 state-of-the-art deep learning models") but the manuscript's own table shows GPFormer at 19.2 below GluLLM at 20.6, so "further" (beyond GPFormer) is contradicted; say instead that it outperforms a bank of deep-learning baselines in-cohort.

### jeffries2026metabonetbench
- Found: Jeffries N, Wolff M, Royston S, Healey E, Mayer C, Klonoff D, Snyder M, Wang T, "MetaboNet-Bench: A Multi-modal Benchmark for Glucose Forecasting in Type 1 Diabetes", arXiv:2606.18640, v1 17 Jun 2026, v2 25 Jun 2026, cs.LG and q-bio.QM. https://arxiv.org/abs/2606.18640
- Discrepancies: arXiv prints "Miriam Wolff"; bib has "Wolff, Miriam K." (harmless if that is her full name elsewhere). Title, other seven authors, eprint number and year match.
- Full author list: n/a (8 authors, all listed).
- Cited for: nothing. Uncited in the paper.
- Numbers checked: n/a.
- Verdict on use: uncited. Either cite it (it is the natural benchmark reference for the MetaboNet cohorts) or remove the entry.

### jaloli2023cnnlstm
- Found: Jaloli M, Cescon M, "Long-Term Prediction of Blood Glucose Levels in Type 1 Diabetes Using a CNN-LSTM-Based Deep Neural Network", J Diabetes Sci Technol 2023;17(6):1590–1601, doi 10.1177/19322968221092785, PMID 35466701, PMCID PMC10658677, online 25 Apr 2022.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: a ReplaceBG study reporting 9.3 mg/dL at 30 min, but on a 15-minute grid and with a rolling split that re-admits test patients to training, so not comparable.
- Numbers checked (full text via text-render proxy of the SAGE page):
  - 15-minute grid: confirmed. "Following that, the CGM variable was uniformly resampled every 15 minutes in both data sets, and insulin and meal characteristics were averaged within each 15-minute time interval."
  - Rolling split re-admitting test patients: confirmed. "Forward Chaining ... the model is trained on an 80% subset of patients and forecast for the remaining 20% which are test patients. Through a rolling basis process, the same forecasted patients are then included as part of the next training data set and model is tested on a new 20% subset of patients."
  - 9.3 mg/dL: DIFFERS. Table 1 (population-level, 30-min PH, Replace-BG) gives LSTM 9.28 ± 1.31 and CNN-LSTM 9.73 ± 1.34; the text says "For 30-minute PH, our model obtained ... RMSE of 9.73 ± 1.34 mg/dL". So 9.3 is the paper's LSTM comparator, not its proposed model. Table 3 (patient-wise) gives CNN-LSTM 14.04 ± 4.47 at 30 min.
  - Replace-BG subset: 168 adults, Dexcom G4 Platinum, insulin pump users.
- Verdict on use: PARTLY SUPPORTED. The protocol description is exactly right and the "not comparable" point stands. Change "9.3" to "9.7" (the paper's own model, population-level) or write "9.3–9.7"; optionally note the patient-wise figure of 14.0.

### fang2026mthyponet
- Found: Fang S, Zhang H, Hu D, Yu X, Liu Z, Ma D, Xu W, Lin F, Xie Q, Liu F, Hu X, Ao T, Zhou D, Li Q, Zhang P, "Glucose forecasting and hypoglycemia forewarning in type 1 and type 2 diabetes using deep learning", iScience 2026;29(4):115294, doi 10.1016/j.isci.2026.115294 (Crossref).
- Discrepancies: bib gives three initial-only names plus "and others"; the record has 15 authors. Volume, issue, article number, year, DOI match.
- Full author list (15): Siyi Fang, Haowei Zhang, Die Hu, Xuefeng Yu, Zhelong Liu, Delin Ma, Weijie Xu, Fan Lin, Qiang Xie, Fang Liu, Xianlong Hu, Tangdong Ao, Dengshi Zhou, Qiang Li, Peng Zhang.
- Cited for: nothing. Uncited in the paper.
- Numbers checked: n/a.
- Verdict on use: uncited. Cite it or remove the entry; if kept, list the first six authors with full names.

### jaeb_flair
- Found: JAEB Center for Health Research public dataset 566, "FLAIR- Fuzzy Logic Automated Insulin Regulation: A Crossover Study Comparing Two Automated Insulin Delivery System Algorithms (PID vs. PID + Fuzzy Logic) in Individuals with Type 1 Diabetes", https://public.jaeb.org/dataset/566. The page asks users to attribute the source and to consult the Read Me for the exact attribution.
- Discrepancies: none material. Bib writes "FLAIR --- Fuzzy Logic" where the page has "FLAIR- Fuzzy Logic"; organisation name is styled "Jaeb Center for Health Research" on the page. No year in the bib. Participant count, devices and NCT id are not on the page itself.
- Full author list: n/a.
- Cited for: Flair as one of three held-out cohorts, and as publicly available through the MetaboNet consolidation.
- Numbers checked: none quoted.
- Verdict on use: SUPPORTED. It is the data source the manuscript says it is.

### abc4d_nct
- Found: ClinicalTrials.gov NCT02053051, brief title "Advanced Bolus Calculator for Type 1 Diabetes (ABC4D)", official title "Clinical Assessment of an Advanced Bolus Calculator for Type 1 Diabetes (ABC4D)", lead sponsor Imperial College London, first posted 3 Feb 2014, start 12 Nov 2013, completion 31 Oct 2021, interventional randomised, enrollment 25, site Imperial College Healthcare NHS Trust, London. https://clinicaltrials.gov/study/NCT02053051
- Discrepancies: none. Bib title equals the brief title; sponsor and year of first posting match.
- Full author list: n/a.
- Cited for: ABC4D as a federated client cohort; a proprietary clinical-study dataset available on request.
- Numbers checked: none quoted. (Enrollment 25 matches the 25 ABC4D subjects in GluGAN and FCNN; GPFormer kept 22 after excluding incomplete records.)
- Verdict on use: SUPPORTED.

### zhu2023glugan
- Found: Zhu T, Li K, Herrero P, Georgiou P, "GluGAN: Generating Personalized Glucose Time Series Using Generative Adversarial Networks", IEEE J Biomed Health Inform 2023;27(10):5122–5133, doi 10.1109/JBHI.2023.3271615, PMID 37134028 (Crossref, OpenAlex, Semantic Scholar and PubMed all give 5122–5133). Author-accepted PDF at https://discovery.ucl.ac.uk/id/eprint/10169613/.
- Discrepancies: PAGES WRONG. Bib has 4906--4917; every record says 5122--5133. Everything else matches.
- Full author list: n/a.
- Cited for: source of the median (IQR) age reported for ABC4D (and ARISES) in the cohort table.
- Numbers checked: the manuscript's age values are not in the extract, so I report what the source gives. Table III ("Demographic characteristics (Median(IQR)) of the OhioT1DM, ARISES, and ABC4D datasets"): ABC4D age 36.0 (29.0–46.0), 25 subjects, Dexcom G5, MDI, six-month trial NCT02053051; ARISES age 40.0 (30.0–49.0), 12 subjects, Dexcom G6, six-week trial NCT03643692. Note GPFormer's Table I gives ABC4D as 47 ± 17 (mean ± SD, 22 subjects), so the two Zhu papers describe different ABC4D subsets; the manuscript should make sure its ABC4D age matches whichever subset it actually uses.
- Verdict on use: SUPPORTED as a source of median (IQR) ages, provided the values in the manuscript's table are 36.0 (29.0–46.0) for ABC4D and 40.0 (30.0–49.0) for ARISES.

### zhu2022arises
- Found: Zhu T, Uduku C, Li K, Herrero P, Oliver N, Georgiou P, "Enhancing self-management in type 1 diabetes with wearables and deep learning", npj Digital Medicine 2022;5(1):78, doi 10.1038/s41746-022-00626-5, PMID 35760819, PMCID PMC9237131 (open access; full text read from Europe PMC XML).
- Discrepancies: none. The corrected author list "Zhu, Uduku, Li, Herrero, Oliver, Georgiou" matches Crossref, Europe PMC and the article exactly, in that order. The note's trial id NCT03643692 is confirmed in the abstract.
- Full author list: n/a (6 authors, all listed).
- Cited for: ARISES as a federated client cohort; source of its median (IQR) age; a proprietary dataset available on request.
- Numbers checked: 12 T1D adults, age "median (IQR) of 40 years (30–50)", 6/6 male, HbA1c 50.4 (41.5–57.5) mmol/mol, Dexcom G6 at 5-min resolution, six weeks per participant, RMSE 20.92 ± 3.55 at 30 min and 35.28 ± 5.77 at 60 min. (GluGAN Table III gives the same cohort as 40.0 (30.0–49.0); pick one source for the IQR upper bound.)
- Verdict on use: SUPPORTED.

### lu2026glucofmbench
- Found: Lu B, Liang Z, Pontius R, Tang S, Prioleau T, "GlucoFM-Bench: Benchmarking Time-Series Foundation Models for Blood Glucose Forecasting", arXiv:2606.06881v1, 5 Jun 2026, cs.LG. https://arxiv.org/abs/2606.06881 (full PDF read).
- Discrepancies: none.
- Full author list: n/a (5 authors, all listed).
- Cited for: (1) general time-series foundation models are benchmarked on glucose forecasting and do not yet beat a small supervised LSTM; (2) RMSE@30 baselines on HUPA-UCM and T1D-UOM: 16.71 (4.82) and 20.81 (4.26), LSTM, by-time split, univariate CGM, SD over patients.
- Numbers checked against Table 4 ("Full-shot RMSE (mg/dL) and SEG no-risk ratio (%) under the 12-hour context, 30-minute horizon setting. Values are participant-level mean (STD)."):
  - HUPA-UCM LSTM 16.71 (4.82): confirmed. T1D-UOM LSTM 20.81 (4.26): confirmed. Both are the best in their rows.
  - By-time split: confirmed ("we chronologically split each participant's CGM time series, using the first 80% for training or fine-tuning and the remaining 20% for evaluation").
  - Univariate CGM: confirmed ("GlucoFM-Bench focuses on univariate CGM forecasting without covariates").
  - SD over patients: confirmed (participant-level mean (STD)).
  - LSTM not yet beaten: confirmed ("when task-specific data are abundant, a lightweight LSTM remains strongest, outperforming TSFMs by 4–21% under full-shot training"; "full-shot LSTM establishes the predictive-performance upper bound in this benchmark").
  - Point error at the horizon: confirmed ("evaluation compares only the model prediction at the target horizon with the corresponding ground-truth CGM value").
- Verdict on use: SUPPORTED. Two side notes, not errors in the citation: the benchmark lists T1D-UOM as 17 participants at 5/15-min sampling and HUPA-UCM as 25 at 5 min (Table 1), whereas the manuscript's cohort table says 14 T1D-UOM patients; and the benchmark also reports a GPFormer row (HUPA-UCM 18.65, T1D-UOM 21.48) that the manuscript does not use.

### zhu2023fcnn
- Found: Zhu T, Li K, Herrero P, Georgiou P, "Personalized Blood Glucose Prediction for Type 1 Diabetes Using Evidential Deep Learning and Meta-Learning", IEEE Trans Biomed Eng 2023;70(1):193–204, doi 10.1109/TBME.2022.3187703, PMID 35776825. Author-accepted PDF at https://discovery.ucl.ac.uk/id/eprint/10152256/.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: RMSE@30 on ARISES and ABC4D from a personalised meta-learning forecaster using CGM plus carbohydrate and insulin, by-time split, SD over patients: 20.23 (3.38) and 20.25 (2.60).
- Numbers checked:
  - ARISES 20.23 (3.38): confirmed (Table II, PH = 30, FCNN RMSE 20.23 ± 3.38).
  - ABC4D 20.25 (2.60): confirmed (Table III, PH = 30, FCNN RMSE 20.25 ± 2.60).
  - Inputs: confirmed ("we selected three input features ... CGM, amount of bolus insulin, and carbohydrate intake").
  - By-time split: confirmed ("we first divided the data of each subject in the ARISES and ABC4D datasets into a training set including the first 80% of the data and a hold-out testing set including the remaining 20%"; "strictly followed chronological partitions").
  - SD over patients: consistent. Tables are "Mean ± STD" over per-subject personalised models; the paper does not spell out the axis, but there is only one model per subject, so the spread is across subjects.
  - Cohort facts: ARISES 12 T1D participants, six-week trial NCT03643692, Dexcom G6; ABC4D 25 T1D subjects, six months, NCT02053051, Dexcom G5; 5-minute CGM.
- Verdict on use: SUPPORTED.


---

# Reference check, group 5

Checked 2026-09-09. Sources: Crossref, OpenAlex, Semantic Scholar, arXiv API, Europe PMC / PubMed eutils, and local text extraction (pdftotext) of the open PDFs for Tan 2026, Piao 2023, Piao 2026 (arXiv 2406.15346), Sun 2025 (arXiv 2410.17933 v4), Li 2025 (arXiv 2409.09727 v2), Manchanda 2025, Kolev 2026 and De Falco 2023. Where a claim was checked on an arXiv version rather than the paywalled final text, the note says so.

## Summary table

| key | exists | metadata issues | citation use | action needed |
|---|---|---|---|---|
| tan2026uncertainty | EXISTS | none (arXiv v2, 28 Mar 2026; no journal version found) | SUPPORTED | none |
| pansheriya2026aegis | EXISTS | pages 1314--1321 and location (Las Vegas, NV) missing | PARTLY SUPPORTED: LOPO and 15-min max horizon confirmed; "T1D-UOM" and "mmol/L" cannot be verified (full text closed) | add pages; confirm "T1D-UOM" and "mmol/L" against the full paper |
| manchanda2025lstm | EXISTS | none | SUPPORTED | none |
| kolev2026benchmark | EXISTS | none | SUPPORTED | none |
| garg2022dexcomg7 | EXISTS | none | SUPPORTED | none |
| alva2023libre3 | EXISTS | none | SUPPORTED (overall MARD is 7.8%, just under the "8--9%" band) | none |
| sun2025multicontinental | EXISTS | none | SUPPORTED | none |
| piao2023graph | EXISTS | none (the arXiv document is an MRes dissertation) | SUPPORTED | none |
| piao2026gluadfl | EXISTS | none | SUPPORTED | none |
| darpit2025fedglu | EXISTS | author name order copies a swapped publisher record ("Darpit, Dave"; the author's other papers give "Dave, Darpit") | SUPPORTED | decide: keep as published or fix to "Dave, Darpit" |
| defalco2023federated | EXISTS | none | SUPPORTED | none |
| teo2024federated | EXISTS | author Nan Liu missing (added by erratum 10.1016/j.xcrm.2024.101481) | SUPPORTED | add "Liu, Nan" as third author |
| li2025challenges | EXISTS | none | SUPPORTED | none |

## Per-entry notes

### tan2026uncertainty
- Found: "Uncertainty quantification in neural network-based glucose prediction for diabetes", Hai Siong Tan, Rafe McBeth. arXiv:2603.04955, v1 5 Mar 2026, v2 28 Mar 2026, primary class cs.LG (also physics.med-ph). No DOI or journal reference. https://arxiv.org/abs/2603.04955
- Discrepancies: none.
- Full author list: n/a (two authors, no "and others").
- Cited for: one of the "other papers on these cohorts" that "report non-comparable metrics", labelled "(MARD only)".
- Numbers checked:
  - "MARD only": confirmed. The paper's point-accuracy metrics are DTS error-grid zone A and MARD: "Another crucial metric of accuracy that we used is that of the mean absolute relative difference (MARD)... Here we used it as a measure of model accuracy with respect to the measurements of the CGM device." The results tables carry zA, MARD, hypo/hyper sensitivity, Brier score, PR-AUC, MCE and Spearman correlations. The string "RMSE" does not occur anywhere in the extracted text. (Example: Table 1, 30-min horizon, MARD 4.14--4.66%.)
  - Cohort: HUPA-UCM, "real clinical data from a medical study of 25 patients" (confirms it is one of the manuscript's cohorts).
  - Split: "For each patient, data were split chronologically into 60% training, 20% validation, and 20% testing"; horizons 30 min and 1 hour; units mg/dL.
- Verdict on use: SUPPORTED. The paper reports no RMSE, so the manuscript is right that it cannot be placed in an RMSE comparison. (Note: the WebFetch summariser first claimed OhioT1DM/6 patients/RMSE; that was wrong. The local text extraction is what the verdict rests on.)

### pansheriya2026aegis
- Found: "AEGIS: AI-Driven Glucose Prediction and Personalized Insulin Dosing", Yash Kishorbhai Pansheriya, Marjan Asadinia. 2026 IEEE 16th Annual Computing and Communication Workshop and Conference (CCWC), Las Vegas, NV, USA, 5--7 Jan 2026, pp. 1314--1321, IEEE. DOI 10.1109/CCWC67433.2026.11393699 (Crossref, OpenAlex, Semantic Scholar, DBLP conf/ccwc/PansheriyaA26 all agree). Closed access; no arXiv or repository copy found.
- Discrepancies: bib has no pages (1314--1321) and no address. Minor.
- Full author list: n/a.
- Cited for: (1) "The one prior work that also splits by patient (AEGIS, on T1D-UOM via leave-one-patient-out) forecasts only to 15 minutes, so it is not comparable at our 30-minute horizon"; (2) "(15-min horizon, mmol/L)".
- Numbers checked:
  - leave-one-patient-out: confirmed. Abstract: "Under a leave-one-patient-out evaluation, XGBoost achieves strong forecasting performance at 10- and 15-minute horizons."
  - 15-minute horizon as the longest: confirmed by the same sentence (10 and 15 min only).
  - "on T1D-UOM": not checkable. The abstract only says "Using real-world data streams--CGM glucose, bolus insulin, carbohydrate intake, and physical activity". OpenAlex lists 13 matched references for the paper and none is the T1D-UOM dataset paper (Alsuhaymi et al. 2025, Sci Data) or any other dataset paper, but OpenAlex reference matching is incomplete, so this is only weak evidence either way.
  - "mmol/L": not checkable without the full text.
  - Tried: IEEE Xplore (HTTP 418 on document, abstract and REST endpoints), Semantic Scholar (references elided by publisher, no OA PDF), CORE (403), arXiv author search (no entries), the CSUN student-research page and its Box link (no content), web search.
- Verdict on use: PARTLY SUPPORTED. The split and the horizon claims match the abstract. The dataset name and the unit are stated in the manuscript in two places and I could not confirm either; someone with IEEE access should check the paper's data section before submission.

### manchanda2025lstm
- Found: "Data-Efficiency with Comparable Accuracy: Personalized LSTM Neural Network Training for Blood Glucose Prediction in Type 1 Diabetes Management", Esha Manchanda, Jialiu Zeng, Chih Hung Lo. Diabetology 2025;6(10):115, published 9 Oct 2025, MDPI. DOI 10.3390/diabetology6100115.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: "(window-averaged RMSE)" as a non-comparable metric.
- Numbers checked:
  - "window-averaged RMSE": confirmed in substance. The model "was trained to predict a 12-dimensional output corresponding to subsequent 60 min blood glucose values" and "RMSE was computed between the predicted and true glucose values over the test set for each individual", then reported as a mean over 25 subjects: "22.52 +/- 6.38 mg/dL for the individualized models, 20.50 +/- 5.66 mg/dL for the aggregated models". So the RMSE pools all twelve 5-min steps of the 60-min output window rather than a single 30-min horizon. The paper never uses the phrase "window-averaged", but that is a fair label. The paper itself notes "a direct comparison of our results with prior personalized approaches is inherently difficult, as the datasets, prediction horizons, and evaluation metrics differ substantially."
  - Cohort: HUPA UCM, 25 subjects; chronological 60:20:20 split per subject.
- Verdict on use: SUPPORTED. If you want the label to be exact, "RMSE pooled over a 60-min output window" says the same thing more precisely.

### kolev2026benchmark
- Found: "A Comprehensive Benchmark of Machine Learning Methods for Blood Glucose Prediction in Type 1 Diabetes: A Multi-Dataset Evaluation", Mikhail Kolev, Irina Naskinova, Mariyan Milev, Stanislava Stoilova, Iveta Nikolova. Applied Sciences 2026;16(8):3928, published 17 Apr 2026, MDPI. DOI 10.3390/app16083928.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: "(synthetic data only)".
- Numbers checked:
  - "synthetic data only": confirmed. Abstract: "all experiments reported here use physics-based synthetic datasets generated from the Bergman minimal model, replicating the structural properties of the D1NAMO and HUPA-UCM" datasets. Methods: because "the D1NAMO archive exceeds 10 GB and the HUPA-UCM server returned HTTP 403), all experiments reported in this paper were conducted on physics-based synthetic datasets generated from the Bergman minimal model". Limitations: "the benchmark was conducted on physics-based synthetic data rather than on the original clinical recordings."
  - 34 synthetic patients (9 D1NAMO-equivalent, 25 HUPA-UCM-equivalent); horizons 15, 30, 60, 120 min.
- Verdict on use: SUPPORTED. "On these cohorts" is loosely true: the paper targets a HUPA-UCM-equivalent synthetic cohort, not the real HUPA-UCM data, which is exactly why the manuscript excludes it.

### garg2022dexcomg7
- Found: "Accuracy and Safety of Dexcom G7 Continuous Glucose Monitoring in Adults with Diabetes", Garg SK, Kipnes M, Castorino K, Bailey TS, Akturk HK, Welsh JB, Christiansen MP, Balo AK, Brown SA, Reid JL, Beck SE. Diabetes Technology & Therapeutics 2022;24(6):373--380. DOI 10.1089/dia.2022.0011, PMID 35157505.
- Discrepancies: none (all 11 authors match).
- Full author list: n/a.
- Cited for: CGM sensor error: "mean absolute relative difference from reference glucose is approx. 8--9%, or roughly 12--14 mg/dL at this population's mean glucose".
- Numbers checked:
  - "approx. 8--9%": confirmed. Abstract: "Overall MARDs were 8.2% and 9.1%, respectively" for arm and abdomen placement; "Data from 316 participants (619 sensors, 77,774 matched pairs)"; %20/20 agreement 95.3% (arm) and 93.2% (abdomen).
  - "12--14 mg/dL": not checkable against this source. It is the manuscript's own arithmetic (8--9% of a mean glucose near 150--155 mg/dL; the manuscript's cohort table lists means such as 151.6 mg/dL for T1D-UOM), and the arithmetic is consistent.
- Verdict on use: SUPPORTED.

### alva2023libre3
- Found: "Accuracy of the Third Generation of a 14-Day Continuous Glucose Monitoring System", Alva S, Brazg R, Castorino K, Kipnes M, Liljenquist DR, Liu H. Diabetes Therapy 2023;14(4):767--776, published 6 Mar 2023, Springer. DOI 10.1007/s13300-023-01385-6, PMID 36877403, PMCID PMC10064376.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: same sentence as garg2022dexcomg7 (CGM MARD approx. 8--9%).
- Numbers checked:
  - "approx. 8--9%": confirmed with a caveat. Abstract: "The overall MARD was 7.8%, and 93.4% of the CGM values were within +/- 20% or +/- 20 mg/dL of the YSI reference for participants aged >= 6 years, with 6845 CGM-YSI matched pairs"; "For participants aged 4-5 years, MARD was 10.0%" (versus SMBG). 100 participants analysed (108 enrolled). The FreeStyle Libre 3 figure (7.8%) sits just under the "8--9%" band; with the "approx." sign the sentence is still fair, and the two devices together span 7.8--9.1%.
- Verdict on use: SUPPORTED. Optional: write "approx. 8--9% (7.8--9.1%)" if you want the exact range.

### sun2025multicontinental
- Found: "Multi-Continental Healthcare Modelling Using Blockchain-Enabled Federated Learning", Rui Sun, Zhipeng Wang, Hengrui Zhang, Ming Jiang, Yizhe Wen, Jiahao Sun, Erwu Liu, Kezhi Li. 2025 IEEE Global Blockchain Conference (GBC), Shanghai, China, pp. 1--8, published 20 Jun 2025, IEEE. DOI 10.1109/GBC60041.2025.11134459. Preprint arXiv:2410.17933 (v4, 9 Oct 2025, "Accepted by IEEE Global Blockchain Conference, 2025").
- Discrepancies: none (8 authors match; location and pages match).
- Full author list: n/a.
- Cited for: "deploy a blockchain-enabled federated glucose model across five cities on three continents, though on in-silico subjects rather than real patient records".
- Numbers checked (arXiv v4 text):
  - "five cities on three continents": confirmed. "The entire framework, including the complete workflow, was deployed and tested in a decentralized manner on four PCs and one server located in five cities across three continents: Toronto, Canada; Shanghai and Shandong, China; and Newcastle and London, UK." Also "the real deployment testing stage of our MCGP across five locations".
  - "in-silico subjects": confirmed. "The dataset utilized to evaluate the proposed framework consists of in-silico data from 30 adult T1D subjects, generated using the UVA/Padova T1D simulator".
  - "blockchain-enabled federated glucose model": confirmed (Multi-Continental Glucose Prediction, MCGP; 30-min-ahead prediction; RMSE and MARD reported).
- Verdict on use: SUPPORTED.

### piao2023graph
- Found: "Blood Glucose Level Prediction: A Graph-based Explainable Method with Federated Learning", Chengzhe Piao, Ken Li. arXiv:2312.12541, v1 19 Dec 2023, cs.LG. The PDF is a UCL Institute of Health Informatics Master of Research dissertation dated 21 Dec 2023 (title page: "A dissertation submitted in partial fulfillment of the requirements for the degree of Master of Research of University College London"). https://arxiv.org/abs/2312.12541
- Discrepancies: none against the arXiv record. "Ken Li" is how the author is listed there (Kezhi Li elsewhere). If you want the reader to know the document type, add note = {MRes dissertation, University College London}.
- Full author list: n/a.
- Cited for: "the usual setup treats individual patients as clients and runs the whole federation on a single machine".
- Numbers checked:
  - patients as clients: confirmed. Algorithm comment: "# each participant is in a client"; "the personal data is only kept by the clients separately".
  - single machine / simulated: confirmed. "Note that we leverage multi-process to simulate FL in this paper, where each client or the server is an independent process." Future work: "We will also try to deploy the FL in real mobile devices instead of only doing simulations."
  - Data: OhioT1DM 2018 and 2020, 12 participants.
- Verdict on use: SUPPORTED.

### piao2026gluadfl
- Found: "Privacy Preserved Blood Glucose Level Cross-Prediction: An Asynchronous Decentralized Federated Learning Approach", Chengzhe Piao, Taiyu Zhu, Yu Wang, Stephanie E. Baldeweg, Paul Taylor, Pantelis Georgiou, Jiahao Sun, Jun Wang, Kezhi Li. IEEE Journal of Biomedical and Health Informatics 2026;30(2):839--852, online 14 Aug 2025. DOI 10.1109/JBHI.2025.3573954, PMID 40811294. Preprint arXiv:2406.15346.
- Discrepancies: none (volume, issue, pages, year, PMID all match Crossref).
- Full author list: n/a.
- Cited for: same simulated-federation claim.
- Numbers checked (arXiv v1 text; final JBHI text is paywalled):
  - patients as clients: confirmed. "Given a set of patients P = {1, ..., N}, where each patient possesses a private dataset"; participants are "nodes in the communication graph"; 298 participants from four T1D datasets.
  - single machine: confirmed. "We implemented all deep learning methods using PyTorch 1.11.0 ... and executed them on an NVIDIA RTX 3090 Ti." Inactive-node experiments: "This approach simulates the impact of different levels of participant inactivity".
- Verdict on use: SUPPORTED.

### darpit2025fedglu
- Found: "A personalized federated learning-based glucose prediction algorithm for high-risk glycemic excursion regions in type 1 diabetes", authors per Crossref/PubMed: Darpit D (given "Dave", family "Darpit"), Vyas K, Jayagopal JK, Garcia A, Erraguntla M, Lawley M. Scientific Reports 2025;15(1):38376, 3 Nov 2025. DOI 10.1038/s41598-025-22316-4, PMID 41184401, PMCID PMC12583674. Correction: Sci Rep 2026;16(1):5742, 10 Feb 2026, DOI 10.1038/s41598-026-36109-w, PMID 41667552; its text: "The original version of this Article contained errors in Figure 9, where the left panel (hypoglycemia region) was omitted... The original Article has been corrected." The bib's note field describes this erratum correctly.
- Discrepancies: author name order. The Sci Rep record, its Research Square preprint (10.21203/rs.3.rs-7339691/v1) and the correction all carry given = "Dave", family = "Darpit", which the bib copies as "Darpit, Dave". The same author's other papers give the reverse: JMIR Diabetes 10.2196/26909, ICASSP 2022 10.1109/ICASSP43922.2022.9746129 and Springer LNBE 10.1007/978-3-030-67303-1_11 all list given = "Darpit", family = "Dave". So the person is almost certainly Darpit Dave and the Sci Rep metadata is swapped. Citing as published ("Darpit, Dave", in-text "Darpit et al.") is defensible; "Dave, Darpit" is the person's name. Pick one; the erratum did not fix it.
- Full author list: n/a.
- Cited for: same simulated-federation claim.
- Numbers checked (PMC full text):
  - patients as clients: confirmed. Clients are individual patients, 125 in total (113 from a TCH Dexcom G6 study plus 12 OhioT1DM); abstract: "sharing only model parameters across other patients".
  - single machine: confirmed by omission. "The global federated model is trained with TensorFlow-federated"; no distributed hardware or multi-site deployment is described. 30-min horizon.
- Verdict on use: SUPPORTED.

### defalco2023federated
- Found: "A Federated Learning-Inspired Evolutionary Algorithm: Application to Glucose Prediction", Ivanoe De Falco, Antonio Della Cioppa, Tomas Koutny, Martin Ubl, Michal Krcma, Umberto Scafuri, Ernesto Tarantino. Sensors 2023;23(6):2957, 8 Mar 2023, MDPI. DOI 10.3390/s23062957, PMID 36991668, PMCID PMC10059991.
- Discrepancies: none.
- Full author list: n/a.
- Cited for: same simulated-federation claim.
- Numbers checked:
  - patients as clients: confirmed. "a dEA that evolves multiple decentralized clients, each representing a single patient, holding local data samples without exchanging them"; "Each slave only contains the private data associated with a single patient." OhioT1DM, 12 subjects.
  - single machine: consistent but not stated outright. "The framework consists in a master process and a set of slaves"; no hardware, network or multi-site deployment is described anywhere in the paper.
  - Side note: the task is 7-class glucose classification, not regression.
- Verdict on use: SUPPORTED. Patients-as-clients is explicit; single-machine simulation is implied by the process-based master/slave description and the absence of any deployment.

### teo2024federated
- Found: "Federated machine learning in healthcare: A systematic review on clinical applications and technical architecture". Cell Reports Medicine 2024;5(2):101419, Feb 2024, Elsevier. DOI 10.1016/j.xcrm.2024.101419, PMID 38340728, PMCID PMC10897620. Erratum: Cell Rep Med 2024;5(3):101481, DOI 10.1016/j.xcrm.2024.101481, PMID 38508145, PMCID PMC10983106, registered in Crossref as an "erratum" update to 101419. Erratum text: "author Nan Liu was inadvertently omitted from the author list. The omission has now been corrected online."
- Discrepancies: the bib lists the 13 authors of the original as-published version. The corrected author list (Crossref, OpenAlex, and the erratum's contrib-group) has 14: Zhen Ling Teo, Liyuan Jin, Nan Liu, Siqi Li, Di Miao, Xiaoman Zhang, Wei Yan Ng, Ting Fang Tan, Deborah Meixuan Lee, Kai Jie Chua, John Heng, Yong Liu, Rick Siow Mong Goh, Daniel Shu Wei Ting. Add "Liu, Nan" after "Jin, Liyuan". (PubMed and PMC still show 13 for the original record, which is why the two sources disagreed.)
- Full author list: n/a (bib had no "and others"); corrected list given above.
- Cited for: "Of 612 federated healthcare studies only 5.2% report a real-life application".
- Numbers checked:
  - 612: confirmed. Abstract: "Out of a total of 22,693 articles under review, 612 articles are included in the final analysis."
  - 5.2%: confirmed. "The majority of articles are proof-of-concepts studies, and only 5.2% are studies with real-life application of FL."
- Verdict on use: SUPPORTED.

### li2025challenges
- Found: "From challenges and pitfalls to recommendations and opportunities: Implementing federated learning in healthcare", Ming Li, Pengcheng Xu, Junjie Hu, Zeyu Tang, Guang Yang. Medical Image Analysis 2025;101:103497, April 2025, Elsevier. DOI 10.1016/j.media.2025.103497. Preprint arXiv:2409.09727 (v2, 4 Feb 2025, "Accepted by Medical Image Analysis").
- Discrepancies: none.
- Full author list: n/a.
- Cited for: "of 107 implementation studies only ten involve real-world distributed clinical settings".
- Numbers checked (arXiv v2 text; the MedIA version is paywalled):
  - 107: confirmed. "597 studies were deemed ineligible, and 107 studies were included in our final review." Scope: "Any study up to May 2024 that involved the use of FL technologies in healthcare based on a simulated or real distributed scenario was included."
  - ten real-world: confirmed. "Only 10 studies reported real-world deployments in distributed clinical settings, while the rest remained in the realm of prototypes or simulations." Repeated in Section 5.1.1: "with only 10 studies incorporating real-world distributed clinical scenarios."
  - "implementation studies" is the manuscript's paraphrase; the review does not use that phrase but the meaning matches (studies that implement FL in a simulated or real distributed scenario).
- Verdict on use: SUPPORTED.


---

