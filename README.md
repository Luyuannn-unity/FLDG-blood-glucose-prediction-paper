# FLDG — Federated & Meta-Learned Blood-Glucose Forecasting (paper)

LaTeX source for the PLOS Digital Health manuscript:
**"Federated and meta-learned blood-glucose forecasting across sites:
a cross-country deployment and a domain-generalisation benchmark."**

## Files
- `glucose_fl_paper.tex` — manuscript (PLOS template). Introduction (with prior
  work folded in, PLOS house style) is drafted; Abstract, Author summary,
  Materials and methods, Results, Discussion are marked TODO.
- `references.bib` — bibliography. Entries tagged `%% VERIFY` need author/year
  checks before submission.

## Building
This uses the PLOS LaTeX template. Before compiling you must add **`plos2025.bst`**
(ships with the official PLOS template) to this directory; the manuscript sets
`\bibliographystyle{plos2025}`. On Overleaf, upload `plos2025.bst` alongside the
source, or switch the menu compiler accordingly.

Set `glucose_fl_paper.tex` as the main document in Overleaf.
