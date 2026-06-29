# wederstrandt-data-science-portfolio

Technical portfolio of data science coursework and project deliverables across data preparation, exploratory analysis, statistical modeling, predictive analytics, data mining, visualization, and generative AI communication artifacts.

## Portfolio Objectives
- Demonstrate end-to-end analytical workflows from raw data acquisition to communication-ready outputs.
- Showcase practical use of statistical and machine learning methods across multiple domains.
- Provide reproducible artifacts that can be reviewed in notebook, report, and presentation formats.
- Emphasize technical storytelling: not only building models, but also documenting assumptions, limitations, and decisions.

## Repository Structure

### Core Folders
- `Intro_to_data_science/`: Introductory project deliverables (paper + presentation assets).
- `Statistics/`: Statistical modeling coursework (regression/GLM comparison, R Markdown analysis, and dataset).
- `eda/`: Exploratory data analysis notebooks and notes for cardiovascular disease outcomes.
- `predictive_analytics/`: Predictive modeling exercises and supporting notes.
- `data_mining/`: Data mining term project artifacts, including fraud detection notebook.
- `data_preparation/`: Multi-source data ingestion and preparation workflows.
- `data_preparation/Final Project/`: Source-specific and integrated DSC540 final project notebooks (API, flat file, HTML, integrated pipeline).
- `data_visualization/`: Visualization-focused R Markdown, PDFs, and infographic assets.
- `data_presentation/`: Stakeholder-facing narrative and notebook outputs.
- `generative_ai/`: Generative AI milestone documentation and presentation assets.

Each directory includes a local `README.md` that covers the technical scope, file inventory, and tooling notes.

## Technology Stack
- Python (Jupyter notebooks for EDA, predictive analytics, and data mining)
- R / R Markdown (statistical and visualization reporting)
- Markdown for technical and narrative documentation
- Multi-format deliverables (`.ipynb`, `.Rmd`, `.pdf`, `.docx`, `.pptx`, `.png`, `.csv`)

## Analytical Workflow Pattern
Most technical projects in this repository follow a common lifecycle:
1. Data sourcing and ingestion (file-based, API-based, or HTML/web extraction).
2. Data cleaning and transformation into analysis-ready tables.
3. Exploratory analysis and feature-level diagnostics.
4. Modeling, statistical testing, or comparative evaluation.
5. Communication via notebook outputs, reports, and presentation artifacts.

## Reproducibility Baseline
1. Use Python 3.10+ for notebook-based folders and a recent R installation for `.Rmd` assets.
2. Create an isolated environment before installing dependencies.
3. Run notebooks top-to-bottom to preserve execution state.
4. Re-render report files from source (`.Rmd`) where available.
5. Check folder-specific README files for project-level run notes and caveats.

## Data and Artifact Notes
- Some folders contain final deliverables only (PDF, DOCX, PPTX) and may not include full source code.
- Some analyses depend on external services or web access during data acquisition phases.
- File naming conventions mirror original coursework submissions for traceability.

## How To Use This Repository
1. Start at the folder-level `README.md` to understand the scope and key files.
2. Open notebooks (`.ipynb`) in Jupyter or VS Code and execute cells sequentially.
3. Render `.Rmd` files in an R-enabled environment to reproduce PDF/report outputs.
4. Use document/presentation artifacts for final communication deliverables.


## Notes
- Directory name `data_preparation` is preserved as-is to match existing repository paths.
- Many folders contain final academic artifacts in addition to executable notebooks/scripts.

## Suggested Review Order
1. `data_preparation/` for ingestion and transformation patterns.
2. `eda/` and `Statistics/` for exploratory and inferential depth.
3. `predictive_analytics/` and `data_mining/` for modeling workflows.
4. `data_visualization/` and `data_presentation/` for communication design.
5. `generative_ai/` and `Intro_to_data_science/` for supporting milestone context.
