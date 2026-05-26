
# Credit Card Fraud Detection Project  
## DSC550 Data Mining - Term Project Overview  

**David Wederstrandt**  
**October 2025 – November 2025**

---

## 1. Introduction: Understanding Fraud Detection

Credit card fraud detection represents one of the most challenging and impactful applications of machine learning in the financial services industry. Every day, millions of credit card transactions occur worldwide, and within this massive volume of legitimate purchases lies a small fraction of fraudulent activities that cost billions annually.

This project addresses the question:  
**How can we automatically identify fraudulent transactions in real time while minimizing false alarms?**

---

### 1.1 Why This Problem Matters

Financial institutions face constant fraud threats with serious consequences:

- Direct financial losses  
- Regulatory penalties  
- Loss of customer trust  
- Increased operational costs  
- Customer frustration from blocked transactions  

Fraud is rare (≈1%) but high-impact, requiring a balance between **fraud detection (recall)** and **customer experience (precision)**.

---

## 2. Understanding the Data

### 2.1 Dataset Overview

The dataset includes **100,000 transactions**:

- `TransactionID`
- `TransactionDate`
- `Amount ($1–$10,000+)`
- `MerchantID`
- `TransactionType (purchase/refund)`
- `Location`
- `IsFraud (0/1)`

Covers one full year for seasonal and temporal pattern analysis.

---

### 2.2 The Class Imbalance Challenge

- Legitimate: **99,000 (99%)**
- Fraud: **1,000 (1%)**

A naive model predicting “no fraud” achieves 99% accuracy—but is useless.

**Key Insight:**  
Accuracy is misleading → need fraud-focused metrics.

---

## 3. Data Exploration and Insights

### 3.1 Transaction Amount Patterns

Findings:

- Fraud tends to have slightly higher amounts  
- Patterns exist across quartiles  
- Both low and high values behave differently  

---

### 3.2 Temporal Patterns

- Fraud varies by **hour, day, and season**
- Late-night transactions show different risk patterns  
- Weekends vs weekdays differ  

---

### 3.3 Geographic & Merchant Patterns

- Location differences are minor  
- **Merchant patterns are critical**

**Key Insight:**  
Fraud is strongly tied to **merchant behavior**

---

## 4. Feature Engineering

### 4.1 Why It Matters

Raw data is not model-ready.  
Example:
- Timestamp → extract meaningful time signals

---

### 4.2 Time-Based Features

- Hour, Day, Month  
- Weekend indicator  
- Risk categories  
- Seasonality  

---

### 4.3 Amount-Based Features

- `Amount_Log`, `ZScore`, `Percentile`  
- Business categories  
- High/low flags  
- Pattern detection (round numbers, trailing zeros)  

---

### 4.4 Merchant-Based Features (Most Important)

- `Merchant_Fraud_Rate`  
- `Merchant_Risk_Category`  
- `Merchant_Avg_Amount`  
- `Merchant_Volume_Category`  

**Key Insight:** Context drives risk.

---

### 4.5 Encoding

- One-hot encoding  
- Binary indicators  
- 80+ features total  

---

## 5. Handling Class Imbalance (SMOTE)

### 5.1 What is SMOTE?

Creates synthetic fraud examples by interpolating between real fraud cases.

---

### 5.2 Implementation

- Applied only to training data  
- Balanced dataset (50/50)  
- Test data unchanged  

---

### 5.3 Why It Works

SMOTE helps models learn fraud patterns instead of ignoring them.

---

## 6. Models Used

### Models Compared

1. **Logistic Regression**
2. **Random Forest**
3. **XGBoost**
4. **LightGBM**

---

### Why Multiple Models?

- No single best algorithm  
- Compare performance  
- Evaluate tradeoffs  

---

## 7. Evaluation Metrics

### 7.1 Why Not Accuracy?

Accuracy fails due to imbalance.

---

### 7.2 Confusion Matrix

|                | Predicted Legit | Predicted Fraud |
|----------------|----------------|-----------------|
| Actual Legit   | TN             | FP              |
| Actual Fraud   | FN             | TP              |

---

### 7.3 Key Metrics

- **Recall** → Catch fraud  
- **Precision** → Accuracy of alerts  
- **F1 Score** → Balance  
- **F2 Score** → Focus on recall ✅  
- **PR-AUC** → Best for imbalance  

---

## 8. Results and Business Impact

### 8.1 Model Performance

| Model | Precision | Recall | F2 |
|------|----------|--------|----|
| Logistic | 0.45 | 0.75 | 0.66 |
| Random Forest | 0.52 | 0.88 | 0.77 |
| XGBoost | **0.55** | **0.90** | **0.80** |
| LightGBM | 0.53 | 0.89 | 0.79 |

**Winner: XGBoost**

---

### 8.2 Business Impact

- Fraud prevented: **$90,000**
- False positive cost: **$735**
- Net gain: **$89,265**
- ROI: **122:1**

---

### 8.3 Feature Importance

Top features:

1. Merchant Fraud Rate  
2. Merchant Avg Amount  
3. Amount  
4. Amount Z-Score  
5. Hour  

---

## 9. Key Learnings

### Technical

- Class imbalance matters  
- Feature engineering > model choice  
- Tree-based models excel  
- Context is critical  

---

### Business

- Perfect detection not required  
- Recall > Precision  
- Huge ROI  
- Continuous updates needed  

---

## 10. Recommendations

### Recommended Model

✅ **XGBoost**

---

### Deployment Plan

**Phase 1:** Monitoring  
**Phase 2:** Controlled rollout  
**Phase 3:** Full automation  

---

### Maintenance

- Monthly retraining  
- Feature updates  
- Monitoring  
- Feedback loops  

---

### Future Improvements

- Customer behavior features  
- Deep learning  
- Graph analysis  
- Real-time scoring  
- Explainable AI  

---

## 11. Conclusion

This project demonstrates the full ML pipeline:

- Problem definition  
- Data exploration  
- Feature engineering  
- Modeling  
- Evaluation  
- Business impact  

---

### Key Achievements

- ✅ 90% fraud detection  
- ✅ 122:1 ROI  
- ✅ Strong feature insights  
- ✅ Production-ready model  

---

## Appendix

### Feature Summary

- Original features: 7  
- Engineered features: 80+  

---

### Models

- Logistic Regression  
- Random Forest  
- XGBoost  
- LightGBM  

---

### Tools

- pandas  
- numpy  
- sklearn  
- xgboost  
- lightgbm  
- matplotlib / seaborn  

---

**Final Thought:**  
Machine learning transforms fraud detection by uncovering complex patterns that simple rules cannot capture, delivering real-world financial impact.

