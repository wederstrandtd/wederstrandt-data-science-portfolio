
# DSC530 Data Exploration and Analysis  
## Final Project: Heart Disease Prediction Through Data Science  
**David Wederstrandt**

---

## 📌 Problem Statement

Cardiovascular disease is the leading global cause of death, responsible for over 20.5 million deaths annually (WHO, 2024). Early detection is critical, yet traditional diagnostic methods may miss subtle patterns in patient data.

This project explores whether machine learning can accurately predict heart disease using standard clinical measurements and what insights exploratory data analysis (EDA) can reveal about key risk factors.

---

## 📊 Data Foundation & Quality Assessment

- **Dataset:** UCI Heart Disease Dataset (Kaggle subset)  
- **Records:** 303 patients  
- **Features:** 14 clinical attributes  
- **Source:** Cleveland Clinic  

### Data Quality Highlights:
- ✅ No missing values  
- ✅ Balanced target distribution (54% positive cases)  
- ✅ Clinically realistic ranges  

### Feature Categories:
- **Demographics:** age, sex  
- **Clinical measurements:** blood pressure, cholesterol, max heart rate  
- **Diagnostics:** ECG, exercise stress tests  
- **Symptoms:** chest pain type, exercise-induced angina  

---

## 🔍 Exploratory Data Analysis (EDA) Insights

### Key Statistical Findings
- **Max Heart Rate (`thalach`)**
  - Significant difference between groups (*p < 0.05*)
  - Lower values associated with heart disease  

### Correlations
- Max heart rate: **-0.421** (strong negative)  
- ST depression (`oldpeak`): **0.428** (positive)  
- Age: **0.225** (moderate positive)  

### Categorical Insights
- **Chest pain:**
  - Asymptomatic → 83% disease rate  
- **Exercise-induced angina:**
  - 71% in diseased vs 29% healthy  
- **Gender trends:**
  - Higher prevalence in males  

---

## 🤖 Machine Learning Results

Multiple models were tested with strong performance:

- **Top Model:** Random Forest  
  - Accuracy: **87.2%**  
  - AUC: **0.924**

### Feature Importance (Top Predictors)
1. Maximum heart rate (`thalach`)  
2. ST depression (`oldpeak`)  
3. Chest pain type  
4. Number of vessels (fluoroscopy)  
5. Age & cholesterol (moderate impact)  

---

## 🔗 Clustering Analysis (K-Means)

Three patient risk profiles emerged:

### 🟢 Cluster 0 — Low Risk (42%)
- Avg age: 45  
- High heart rate: 175 bpm  
- Disease rate: 23%  

### 🟡 Cluster 1 — Moderate Risk (35%)
- Avg age: 56  
- Mixed indicators  
- Disease rate: 56%  

### 🔴 Cluster 2 — High Risk (23%)
- Avg age: 62  
- Low heart rate: 142 bpm  
- High ST depression  
- Disease rate: 84%  

---

## 🧠 Clinical Insights

### Key Takeaways:
- **Exercise capacity** is the strongest predictor  
- **Asymptomatic patients** can still be high-risk  
- **Risk clustering** supports personalized medicine  

---

## 🚀 Implementation & Future Work

### Potential Applications:
- Clinical decision support systems (EHR integration)  
- Risk-based screening strategies  
- Personalized care pathways  

### Recommendations:
- Train clinicians on ML interpretation  
- Validate models on diverse populations  
- Monitor performance over time  

---

## ⚠️ Limitations

- Single-source dataset (limited generalizability)  
- Retrospective analysis  
- Requires regulatory approval for clinical use  

---

## ✅ Conclusion

This project demonstrates how data science can enhance cardiovascular risk prediction through:

- High-performing machine learning models  
- Meaningful feature insights  
- Clinically relevant patient segmentation  

The findings support improved diagnostic accuracy and more personalized patient care.

---

## 📊 Visualizations

### Visualization 1:
**Comprehensive Risk Factor Analysis**  
- Correlation matrix  
- Distribution comparisons  

### Visualization 2:
**Clinical Decision Support Dashboard**  
- Model performance metrics  
- Risk assessment outputs  

---

## 📚 References

Di Cesare, M., et al. (2024). *The heart of the world*. Global Heart, 19(1).  
https://doi.org/10.5334/gh.1288
```
