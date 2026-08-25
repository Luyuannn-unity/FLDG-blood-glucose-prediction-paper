# FLDG — Federated & Meta-Learned Blood-Glucose Forecasting (paper)

LaTeX source for the PLOS Digital Health manuscript
**"Federated and meta-learned blood-glucose forecasting across sites:
a domain-generalisation benchmark and a four-institution deployment."**

Start with `START_HERE.md`. It says which file is live, what is locked in, and
what is still open.

## Files
- `revision/glucose_fl_paper_working.tex` — the live manuscript. Edit this one.
- `revision/glucose_fl_paper_v1..vN.tex` — frozen snapshots, one per revision
  iteration. The highest N is the newest.
- `revision/references.bib` — bibliography.
- `revision/figures/` — `fl_system.pdf` (source `fl_system_fig.py`) and
  `data_efficiency.pdf` (source `data_efficiency_fig.py`, which regenerates it
  from the per-seed result CSVs).
- `glucose_fl_paper.tex` — the author's original Overleaf copy. Superseded by the
  working file. Do not edit.
- `plos2015.bst` — PLOS Vancouver BibTeX style, committed so the bibliography
  builds out of the box.
- `reviews/` — reviewer critiques, per-iteration change logs
  (`iterN_revisions.md`), reference checks, the submission checklist
  (`SUBMISSION_TODO.md`) and the open-items list (`REQUIRED_FROM_YOU.md`).

## Building
No local LaTeX toolchain is assumed. On Overleaf, set
`revision/glucose_fl_paper_working.tex` as the main document and compile with
pdfLaTeX. BibTeX with `\bibliographystyle{plos2015}` over `references.bib`
resolves the references with no extra setup. The current PLOS template ships an
identical style file renamed `plos2025.bst`. For final submission you may swap
in that file and change the one `\bibliographystyle{...}` line to match.

## Numbers
Every number in the manuscript traces to the clean-retrain outputs in
`release_bundle/output_clean_retrain/` (see `START_HERE.md` and `../CHANGES.md`).
