# wederstrandt-data-science-portfolio

![Portfolio](https://img.shields.io/badge/Portfolio-Data%20Science-0A7E8C)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-Reporting-276DC3?logo=r&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-EDA%20%7C%20Modeling%20%7C%20Storytelling-4C956C)

Technical portfolio of data science coursework and project deliverables across data preparation, exploratory analysis, statistical modeling, predictive analytics, data mining, visualization, and generative AI communication artifacts.

## 30-Second Recruiter Summary
- Target roles: Data Analyst, Junior Data Scientist.
- Core stack: Python, scikit-learn, Jupyter, R, R Markdown, Markdown.
- Proof points: data prep across multiple source types, imbalanced fraud modeling, API-driven CLI automation, and stakeholder-facing communication artifacts.
- Best starting point: review the flagship projects below, then drill into folder-level README files.

## Flagship Projects (Start Here)
| Project | What It Demonstrates | Measurable Outcome |
|---|---|---|
| [Programming Python](2.%20Programming_Python/) | API integration and CLI workflow design | Weather app supports 50 states + DC normalization and returns 1-5 day forecasts from live OpenWeather endpoints |
| [Data Preparation](5.%20Data_Preparation/) | Multi-source ETL and schema alignment | 4 notebooks cover API, flat-file, HTML extraction, and final integrated pipeline into analysis-ready tables |
| [Data Mining](6.%20Data_Mining/) | Imbalanced classification for fraud risk | End-to-end notebook includes distribution checks, preprocessing, model training, and skew-aware evaluation workflow |
| [Predictive Analytics (Collaboration)](7.%20Predictive_Analytics/) | Team communication and stakeholder-ready analytics storytelling | 3 coordinated deliverables (DOCX, PDF, PPTX) produced in collaboration with Dong Lee on diabetes risk analysis |

## Quick Portfolio Snapshot
| Dimension | Coverage |
|---|---|
| Primary domains | Data preparation, EDA, statistics, predictive analytics, data mining, visualization, GenAI communication |
| Core tooling | Python, Jupyter, R, R Markdown, Markdown |
| Artifact formats | `.ipynb`, `.Rmd`, `.pdf`, `.docx`, `.pptx`, `.png`, `.csv` |
| Portfolio style | End-to-end workflow plus stakeholder-ready communication |

## Portfolio Objectives
- Demonstrate end-to-end analytical workflows from raw data acquisition to communication-ready outputs.
- Showcase practical use of statistical and machine learning methods across multiple domains.
- Provide reproducible artifacts that can be reviewed in notebook, report, and presentation formats.
- Emphasize technical storytelling: not only building models, but also documenting assumptions, limitations, and decisions.

## Repository Structure

### Core Folders
- `1. Intro_to_data_science/`: Introductory project deliverables.
- `2. Programming_Python/`: Python programming scripts and API-driven CLI project.
- `3. Statistics/`: Statistical modeling coursework, reports, and datasets.
- `4. Exploritory_Data_Analysis/`: EDA notebooks and analysis notes.
- `5. Data_Preparation/`: Multi-source data ingestion and preparation workflows.
- `6. Data_Mining/`: Data mining term project artifacts, including fraud detection notebook.
- `7. Predictive_Analytics/`: Collaborative predictive analytics communication deliverables.
- `8. Data_Visualization/`: Visualization-focused R Markdown and report assets.
- `9. Generative_AI/`: Generative AI milestone documentation and presentation assets.
- `10. Advanced Data Science/`: Reserved for future advanced coursework artifacts.

Active project directories include local `README.md` files that cover technical scope, file inventory, and tooling notes.

## Folder Map
| Folder | Theme | Typical Output |
|---|---|---|
| `1. Intro_to_data_science/` | Introductory analysis communication | Foundational deliverables |
| `2. Programming_Python/` | Python programming and API integration | CLI scripts and helper modules |
| `3. Statistics/` | Regression and GLM analysis | R Markdown reports and interpretations |
| `4. Exploritory_Data_Analysis/` | Exploratory profiling and hypothesis formation | Pattern discovery notebooks |
| `5. Data_Preparation/` | Multi-source ETL and normalization | Cleaned, integrated data workflows |
| `6. Data_Mining/` | Imbalanced fraud detection classification | Comparative classification metrics |
| `7. Predictive_Analytics/` | Collaborative predictive analytics communication | Report and slide deliverables |
| `8. Data_Visualization/` | Visual storytelling and report artifacts | R Markdown output and report assets |
| `9. Generative_AI/` | Milestone communication artifacts | Report and presentation deliverables |
| `10. Advanced Data Science/` | Advanced methods and synthesis | In progress |

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

## Programming_Python Spotlight
The folder `2. Programming_Python/` contains a command-line weather application that integrates with the OpenWeather API.

### OpenWeather CLI App
- Script: `2. Programming_Python/openweather_forecast.py`
- Helper module: `2. Programming_Python/us_state_lookup.py`
- Input flow:
    - Prompts for location in `city, state` format.
    - Accepts state abbreviation (`CO`) or full state name (`Colorado`).
    - Prompts for forecast window (1-5 days).
- API key flow:
    - Uses `API_KEY` from `.env` when available.
    - If `.env` is missing, prompts user to either paste an API key for one run or save it to a new/updated `.env`.


## Notes

- Many folders contain final academic artifacts in addition to executable notebooks/scripts.
