# Reference check — Group B (Federated Learning core / Healthcare FL / DG & Personalisation)

**Manuscript:** `paper/revision/glucose_fl_paper_working.tex`
**Bib:** `paper/revision/references.bib`
**Checked:** 2026-07-07 against Crossref, arXiv, DBLP, PMLR, CVF, MLSys, publisher pages.

All 17 assigned keys are cited in one dense related-work paragraph (tex lines ~195–230). Every reference **exists** and metadata is essentially correct. The only metadata issue is a title/venue inconsistency on `fallah2020perfedavg`. Every method description in the paper faithfully matches its source. The two machinery fault-diagnosis papers (`flda2023`, `fedadv2022`) are correctly cited as *examples of adversarial domain alignment* — not misattributed to medical work.

## Summary table

| Key | Metadata | Claim support | Confidence | Note |
|---|---|---|---|---|
| mcmahan2017fedavg | CORRECT | SUPPORTS | High | FedAvg / AISTATS 2017 |
| li2020fedprox | CORRECT | SUPPORTS | High | proximal term — correct |
| karimireddy2020scaffold | CORRECT | SUPPORTS | High | control variates — correct |
| rieke2020future | CORRECT | SUPPORTS | High | DOI verified |
| sheller2020federated | CORRECT | SUPPORTS | High | DOI verified |
| kaissis2020secure | CORRECT | SUPPORTS | High | DOI verified |
| li2018mldg | CORRECT | SUPPORTS | High | MLDG meta-train/meta-test — correct |
| deng2020apfl | CORRECT | SUPPORTS | High | adaptive convex mixture — correct |
| li2021ditto | CORRECT | SUPPORTS | High | proximal-to-global personal model — correct |
| li2021moon | CORRECT | SUPPORTS | High | model-contrastive — correct |
| fallah2020perfedavg | **WRONG-FIELD:title** | SUPPORTS | High | bib uses arXiv title; NeurIPS'20 title differs |
| chen2018fedmeta | CORRECT | SUPPORTS | High | FedMeta arXiv 1802.07876 |
| li2025fedDGsurvey | CORRECT | SUPPORTS | High | DOI verified |
| fedcl2023 | CORRECT | SUPPORTS | High | DOI verified |
| flda2023 | CORRECT | SUPPORTS | High | fault-diagnosis, cited as adv. alignment — OK |
| fedadv2022 | CORRECT | SUPPORTS | High | fault-diagnosis, cited as adv. alignment — OK |
| zhou2022dgsurvey | CORRECT | SUPPORTS | High | DOI verified |

## Detailed notes

### Core FL

**mcmahan2017fedavg** — cite (l.195): "Federated learning (FL) addresses this tension~\cite{mcmahan2017fedavg}: sites train on their own data and exchange only model updates…". Claim: FL trains on-site and exchanges only updates. Metadata CORRECT: *Communication-Efficient Learning of Deep Networks from Decentralized Data*, McMahan et al., AISTATS 2017 (PMLR 54). Claim SUPPORTS. URL: https://proceedings.mlr.press/v54/mcmahan17a.html

**li2020fedprox** — cite (l.202): "…motivating proximal regularisation~\cite{li2020fedprox}…". Claim: FedProx adds proximal regularisation for heterogeneity. Metadata CORRECT: *Federated Optimization in Heterogeneous Networks*, Li, Sahu, Zaheer, Sanjabi, Talwalkar, Smith, MLSys 2020. Claim SUPPORTS — FedProx adds a proximal term μ/2·‖w−w^t‖² to the local objective. URL: https://proceedings.mlsys.org/paper_files/paper/2020/hash/1f5fe83998a09396ebe6477d9475ba0c-Abstract.html (arXiv 1812.06127)

**karimireddy2020scaffold** — cite (l.203): "…and control-variate variance reduction~\cite{karimireddy2020scaffold}". Claim: SCAFFOLD uses control variates for variance reduction. Metadata CORRECT: SCAFFOLD, Karimireddy et al., ICML 2020 (PMLR 119). Claim SUPPORTS — uses server/client control variates to correct client-drift (variance reduction). URL: https://proceedings.mlr.press/v119/karimireddy20a.html (arXiv 1910.06378)

### Healthcare FL

**rieke2020future** — cite (l.199): grouped as FL "widely adopted for collaborative medical machine learning". Metadata CORRECT (Crossref-verified): npj Digital Medicine 3(1):119, 2020, DOI 10.1038/s41746-020-00323-1. Claim SUPPORTS (position/vision paper on FL for digital health).

**sheller2020federated** — same cite (l.199). Metadata CORRECT (Crossref): Scientific Reports 10:12598, 2020, DOI 10.1038/s41598-020-69250-1 (Crossref lists issue 1; bib omits `number`, harmless). Claim SUPPORTS (multi-institutional FL without sharing patient data).

**kaissis2020secure** — same cite (l.199). Metadata CORRECT (Crossref): Nature Machine Intelligence 2:305–311, 2020, DOI 10.1038/s42256-020-0186-1 (Crossref issue 6; bib omits `number`, harmless). Claim SUPPORTS.

### DG & personalisation

**zhou2022dgsurvey** — cite (l.213): "Domain generalisation seeks models that transfer to unseen distributions~\cite{zhou2022dgsurvey}". Metadata CORRECT (Crossref DOI verified): *Domain Generalization: A Survey*, Zhou, Liu, Qiao, Xiang, Loy, TPAMI 45(4):4396–4415, 2022, DOI 10.1109/TPAMI.2022.3195549 (Crossref shows early-access pages 1–20; final vol/issue/pages in bib are the correct published values). Claim SUPPORTS.

**li2018mldg** — cite (l.215): "meta-learning for domain generalization (MLDG) simulates train/test domain shift within each update so the model learns to generalise rather than memorise~\cite{li2018mldg}". Metadata CORRECT: *Learning to Generalize: Meta-Learning for Domain Generalization*, Li, Yang, Song, Hospedales, AAAI 2018. Claim SUPPORTS — MLDG splits source domains into meta-train / meta-test each iteration to simulate domain shift (matches Li et al. 2018). URL: https://ojs.aaai.org/index.php/AAAI/article/view/11596 (arXiv 1710.03463)

**li2025fedDGsurvey** — cite (l.216): "…an active area surveyed by Li et al.~\cite{li2025fedDGsurvey}…". Metadata CORRECT (Crossref DOI verified): *Federated Domain Generalization: A Survey*, Li et al., Proceedings of the IEEE 113(4):370–410, 2025, DOI 10.1109/JPROC.2025.3596173. Claim SUPPORTS.

**chen2018fedmeta** — cite (l.219): "Meta-learning approaches adapt the model-agnostic meta-learning objective to federation, for communication-efficient convergence~\cite{chen2018fedmeta}". Metadata CORRECT: *Federated Meta-Learning with Fast Convergence and Efficient Communication*, Chen, Luo, Dong, Li, He, arXiv 1802.07876, 2018. Claim SUPPORTS — FedMeta uses MAML/Meta-SGD meta-learners in the federated setting and reports 2.8–4.3× communication reduction + faster convergence. URL: https://arxiv.org/abs/1802.07876

**fallah2020perfedavg** — cite (l.220): "…or for models that personalise to a new client in a few gradient steps~\cite{fallah2020perfedavg}". Metadata **WRONG-FIELD:title** (minor): bib title *"Personalized Federated Learning: A Meta-Learning Approach"* is the arXiv 2002.07948 title, but the cited **NeurIPS 2020** proceedings title is *"Personalized Federated Learning with Theoretical Guarantees: A Model-Agnostic Meta-Learning Approach"* (Fallah, Mokhtari, Ozdaglar). Venue (NeurIPS 2020) is correct. Claim SUPPORTS — Per-FedAvg is a MAML-style method personalising in a few gradient steps.
Suggested fix: either (a) match the proceedings title and keep `booktitle=NeurIPS 2020`, or (b) keep the short title but change to an `@misc`/arXiv 2002.07948 entry so title and venue are consistent. URL (proceedings): https://proceedings.neurips.cc/paper/2020/hash/24389bfe4fe2eba8bf9aa9203a44cdad-Abstract.html

**deng2020apfl** — cite (l.221–222): "APFL learns an adaptive convex mixture of the global and a local model~\cite{deng2020apfl}". Metadata CORRECT: *Adaptive Personalized Federated Learning*, Deng, Kamani, Mahdavi, arXiv 2003.13461, 2020. Claim SUPPORTS — APFL forms an adaptive convex combination α·local + (1−α)·global with learned mixing weight α. URL: https://arxiv.org/abs/2003.13461

**li2021ditto** — cite (l.222–223): "Ditto regularises each client's personal model toward the global one with a tunable proximal strength~\cite{li2021ditto}". Metadata CORRECT: *Ditto: Fair and Robust Federated Learning Through Personalization*, Li, Hu, Beirami, Smith, ICML 2021 (PMLR 139). Claim SUPPORTS — Ditto trains a personal model with a λ/2·‖v−w*‖² proximal term pulling it toward the global model w*. URL: https://proceedings.mlr.press/v139/li21h.html

**li2021moon** — cite (l.224–225): "Other approaches instead align client representations, via model-contrastive objectives~\cite{li2021moon}". Metadata CORRECT: *Model-Contrastive Federated Learning* (MOON), Li, He, Song, CVPR 2021, pp. 10713–10722. Claim SUPPORTS — MOON contrasts local vs. global model representations. URL: https://openaccess.thecvf.com/content/CVPR2021/html/Li_Model-Contrastive_Federated_Learning_CVPR_2021_paper.html

**fedcl2023** — cite (l.225–226): "…federated contrastive learning for multi-centre medical imaging~\cite{fedcl2023}". Metadata CORRECT (Crossref DOI verified): *FedCL: Federated contrastive learning for multi-center medical image classification*, Liu, Wu, Wang, Yang, Pan, Pattern Recognition 143:109739, 2023, DOI 10.1016/j.patcog.2023.109739. Claim SUPPORTS.

**flda2023** — cite (l.226–227): "…or adversarial domain alignment~\cite{flda2023,fedadv2022}". Metadata CORRECT (Crossref DOI verified): *Federated multi-source domain adversarial adaptation framework for machinery fault diagnosis with data privacy*, Zhao, Hu, Shao, Hu, Reliability Engineering & System Safety 236:109246, 2023, DOI 10.1016/j.ress.2023.109246. Claim SUPPORTS — this is a machinery fault-diagnosis paper, and it is cited (correctly) as a generic example of federated **adversarial domain alignment**, not as medical work. Appropriate.

**fedadv2022** — same cite (l.226–227). Metadata CORRECT (Crossref DOI verified): *Federated adversarial domain generalization network: A novel machinery fault diagnosis method with data privacy*, Wang, Huang, Shi, Wang, Shen, Zhu, Knowledge-Based Systems 256:109880, 2022, DOI 10.1016/j.knosys.2022.109880. Claim SUPPORTS — machinery fault-diagnosis paper cited (correctly) as an adversarial domain-alignment example. Appropriate.

## Bottom line
No fabricated references, no misattributed method descriptions, and the fault-diagnosis papers are honestly framed. The single actionable metadata fix is the `fallah2020perfedavg` title/venue mismatch. Optional tidy-ups: add `number` fields for `sheller2020federated` (1) and `kaissis2020secure` (6) to match Crossref.
