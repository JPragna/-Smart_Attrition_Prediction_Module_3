# Module 3: Attrition Prediction Model 🚀

This module focuses on building a robust and interpretable machine learning model to **predict employee attrition** risk and identify key factors driving it. The work forms part of the larger project: **Smart Attrition Prediction & Employee Wellness Recommendation Engine**.

---

## 📌 Objective

- Predict whether an employee is at risk of leaving the organization.
- Minimize false alarms (High Precision) while identifying as many at-risk employees as possible (High Recall).
- Interpret model predictions using explainable AI tools.

---

## 📊 Dataset Overview

- Source: HR dataset with 1000+ employees (from Module 2).
- Key features include: `Age`, `JobSatisfaction`, `OverTime`, `MonthlyIncome`, `YearsAtCompany`, `SatisfactionIndex`, `WorkBalanceScore`, etc.
- Target variable: `Attrition` (0 = No, 1 = Yes)

---

## 🧠 Algorithms Used

| Model               | Notes                                      |
|--------------------|--------------------------------------------|
| Logistic Regression | Baseline, interpretable                   |
| Random Forest       | Handles non-linearity, built-in feature importance |
| XGBoost             | Great for imbalanced data, performance-optimized |

---

## 📌 Handling Class Imbalance

- Initial Class Distribution:
  - Class 0 (No Attrition): 986
  - Class 1 (Attrition): 190

- Techniques Used:
  - **SMOTE** for oversampling the minority class
  - **Class weights** added to logistic regression
  - **Stratified K-Fold CV** for balanced evaluation

---

## 🔍 Model Performance (Post-SMOTE)

| Model              | Precision (Class 1) | Recall (Class 1) | F1 Score (Class 1) | Accuracy |
|-------------------|---------------------|------------------|--------------------|----------|
| Logistic Regression | 0.33                | 0.72             | 0.46               | 72%      |
| Random Forest       | 0.49                | 0.45             | 0.47               | 84%      |
| XGBoost             | 0.50                | 0.43             | 0.46               | 84%      |

✅ Best performance: **Random Forest** (balanced precision and recall)

---

## 🔎 Key Features Driving Attrition

### 🎯 Random Forest Top 3 Features:
- `YearsAtCompany`
- `Age`
- `MonthlyIncome`

### 🎯 XGBoost Top 3 Features:
- `OverTime_Yes`
- `SatisfactionIndex`
- `YearsAtCompany`

---

## 🧠 Explainability with SHAP

- SHAP (SHapley Additive exPlanations) was used for **model interpretability**.
- Visualized how individual features like `OverTime`, `SatisfactionIndex`, and `YearsAtCompany` influenced predictions.

📎 See SHAP visual outputs in [`/outputs/shap_values`](./outputs/shap_values/)

---

## 📈 Visual Snapshots

- ✅ Confusion matrices
- ✅ Feature importance bar plots
- ✅ SHAP summary plots

📎 All visuals are stored in [`/outputs/`](./outputs/)

---

## 📁 Repository Structure

