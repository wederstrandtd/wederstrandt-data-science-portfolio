# Data_Preparation

![Track](https://img.shields.io/badge/Track-Data%20Preparation-3D5A80)
![Pipeline](https://img.shields.io/badge/Pipeline-API%20%7C%20Flat%20File%20%7C%20HTML-98C1D9)

## Scope
This directory contains data preparation and integration work for the DSC540 final project. The focus is on ingesting and normalizing data from multiple source types.

## At A Glance
| Category | Details |
|---|---|
| Primary folder | `Final Project/` |
| Workflow style | Multi-source ETL |
| Core output | Analysis-ready integrated dataset |
| Main skills | Extraction, cleaning, schema alignment |

## Objective
Build a unified, analysis-ready dataset from heterogeneous inputs while documenting extraction, cleaning, and transformation logic.

## Contents
- `Final Project/`: Consolidated project notebooks by source modality.

## Technical Focus
- Data acquisition from APIs, flat files, and HTML sources.
- Cleaning, schema standardization, and transformation pipelines.
- Preparation of analysis-ready datasets for downstream modeling or reporting.

## Tooling
- Python 3.x
- Jupyter Notebook
- Typical stack: `pandas`, `requests`, `beautifulsoup4`, and standard ETL utilities

## ETL Architecture
1. Source ingestion by modality (API, file, HTML).
2. Source-level cleaning and type normalization.
3. Schema alignment across disparate datasets.
4. Consolidation into integrated analytical tables.
5. Validation checks for completeness and consistency.

## Data Quality Practices
- Standardize column names and data types before joins.
- Track missing values and imputation/handling decisions.
- Verify key uniqueness and relationship cardinality.
- Capture transformation assumptions in notebook markdown.

## How To Navigate
1. Start in `Final Project/` and review notebooks by source type.
2. Validate extraction logic at the source level.
3. Finish with the integrated final notebook for the combined workflow.

## Notes
- Folder name `data_preparation` is intentionally retained to match repository structure.

## Visual Navigation
1. Start with source-specific extraction notebooks.
2. Validate quality checks and schema consistency.
3. Finish with an integrated consolidation workflow.
