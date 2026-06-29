# Exploratory Data Analysis

[Track](https://img.shields.io/badge/Track-Exploratory%20Data%20Analysis-2A9D8F)
![Notebook](https://img.shields.io/badge/Primary%20Artifact-Jupyter%20Notebook-F37726?logo=jupyter&logoColor=white)

## Scope
This directory contains exploratory data analysis (EDA) work for cardiovascular disease outcomes.

## At A Glance
| Category | Details |
|---|---|
| Domain | Cardiovascular disease outcomes |
| Primary asset | `dsc530_wederstrandt_final_project.ipynb` |
| Supporting context | `cardiovascular_disease.md` |
| Goal | Discover patterns and guide feature selection |

## Objective
Identify meaningful patterns in patient-level or outcome-related variables to support downstream hypothesis testing and predictive modeling decisions.

## Contents
- `dsc530_wederstrandt_final_project.ipynb`: Notebook with exploratory profiling, descriptive statistics, and preliminary inference.
- `cardiovascular_disease.md`: Project notes and context.

## Technical Focus
- Distribution analysis and feature-level pattern discovery.
- Initial relationship analysis to identify candidate predictors.
- Early-stage hypothesis formation for downstream modeling.

## Tooling
- Python 3.x
- Jupyter Notebook
- Typical stack: `pandas`, `numpy`, `matplotlib`, `seaborn`

## EDA Workflow
1. Ingest and inspect schema, types, and missingness patterns.
2. Compute summary statistics for central tendency and spread.
3. Visualize univariate distributions and bivariate relationships.
4. Flag potential outliers, skew, and data-quality concerns.
5. Document candidate features and hypotheses for modeling.

## Expected Outcomes
- A structured profile of the dataset and target-related variables.
- A shortlist of influential predictors or interactions to test later.
- Documentation of data issues requiring preprocessing.

## Reproducibility Notes
- Run notebook cells sequentially to maintain variable state.
- Install visualization and analysis dependencies before execution.
- Use markdown notes as a bridge between exploratory findings and model planning.

## Outcome Quality Signals
- Clear summary statistics with missingness awareness.
- Visual evidence for distributions and relationships.
- Explicit hypotheses ready for downstream modeling.
