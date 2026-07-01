# Credit Card Fraud Detection Analysis

![Track](https://img.shields.io/badge/Track-Data%20Mining-264653)
![Use%20Case](https://img.shields.io/badge/Use%20Case-Fraud%20Detection-B56576)
![Modeling](https://img.shields.io/badge/Task-Imbalanced%20Classification-6D597A)

## Scope
This directory contains coursework and project artifacts focused on supervised learning for fraud detection.

## At A Glance
| Category | Details |
|---|---|
| Main notebook | `credit_card_fraud_detection_analysis.ipynb` |
| Supporting notes | Included in notebook markdown cells |
| Core challenge | Class imbalance |
| Evaluation style | Precision/Recall/F1/ROC-AUC aware |

## Problem Framing
Fraud detection is typically an imbalanced classification problem where minority-class recall and precision often matter more than raw accuracy.

## Contents
- `dsc550_wederstrandt_d_term_project_fraud_detection.ipynb`: End-to-end notebook for data loading, preprocessing, model training, and fraud-classification evaluation.
- `dm.md`: Supporting notes and project context.

## Technical Focus
- Binary classification for imbalanced classes.
- Feature engineering and data-quality handling for transactional data.
- Model comparison using metrics appropriate for skewed labels (for example, precision, recall, F1, and ROC-AUC).

## Tooling
- Python 3.x
- Jupyter Notebook
- Typical stack: `pandas`, `numpy`, `scikit-learn`, `matplotlib`/`seaborn`

## Reproducibility Notes
1. Open the notebook in Jupyter or VS Code.
2. Install required Python packages in your environment.
3. Execute cells to reproduce preprocessing and model outputs.

## Typical Pipeline Stages
1. Data inspection and target distribution analysis.
2. Feature cleanup, encoding, and transformation.
3. Train/validation splitting with attention to class balance.
4. Candidate model training and threshold-aware evaluation.
5. Error analysis on false positives and false negatives.

## Expected Deliverables
- A reproducible notebook showing data preparation through model evaluation.
- Comparative metric summaries aligned to fraud-risk priorities.
- Supporting notes describing assumptions and limitations.

## Operational Considerations
- Optimize for the business cost of misclassification, not only aggregate accuracy.
- Revisit thresholds and sampling strategy as class distribution changes.

## Portfolio Highlight
This folder emphasizes realistic model evaluation for high-cost decision contexts where false positives and false negatives carry different business impacts.
