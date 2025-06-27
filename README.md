# 📦 Smart Attrition Prediction – Module 3: Attrition Risk Modeling

## 📌 Overview

This module focuses on building an interpretable, high-performance machine learning model to predict employee attrition using HR data. It is part of the larger project **"Smart Attrition Prediction & Employee Wellness Recommendation Engine"**.

We apply classification techniques with resampling, hyperparameter tuning, and explainability to help HR teams reduce turnover and retain key talent.

---

## 🌟 Objectives

* Predict the likelihood of employee attrition
* Minimize false alarms (high precision)
* Capture actual attrition cases (high recall)
* Interpret model predictions with SHAP and feature importance

---

## 🛠️ Tools & Technologies

* **Languages**: Python (Pandas, NumPy)
* **Modeling**: scikit-learn, XGBoost
* **Imbalance Handling**: SMOTE (imbalanced-learn)
* **Model Explainability**: SHAP
* **Visualization**: Matplotlib, Seaborn

---
## 🚀 Features

- 🔄 **Handles class imbalance** using SMOTE and weighted models
- 📊 **Models used**: Logistic Regression, Random Forest, XGBoost
- 📈 **Evaluation**: Confusion matrix, ROC-AUC, Precision, Recall
- 🧠 **Explainability**: SHAP used to understand feature importance
- 🎯 **Best Accuracy Achieved**: ~84% (XGBoost)

---
## 📁 Project Structure

```
Smart_Attrition_Prediction_Module_3/
├── notebooks/
│ └── Attrition_Model_Development.ipynb
├── data/
│ └── M3_Cleaned_Final.csv
├── models/
│ └── xgb_model.pkl
├── predict.py
├── shap_plot.py (optional)
├── visuals/
├── README.md
```

---

## 🔍 Key Steps

### ✅ 1. Feature Selection

* Removed noisy or highly correlated features (VIF + EDA)
* Final feature set: 35 columns selected from 60+ after analysis

### ✅ 2. Model Training

* Models: Logistic Regression, Random Forest, XGBoost
* Resampling with SMOTE
* Stratified 5-fold Cross-validation
* Used class weights where applicable

### ✅ 3. Evaluation

* **Metrics**: Precision, Recall, F1 Score (not just accuracy)
* **Best Model**: XGBoost (after tuning)
* Hyperparameter tuning with GridSearchCV

### ✅ 4. Interpretability

* Feature Importance (Random Forest and XGBoost)
* SHAP Values for local + global explanation

---

## 📊 Model Comparison

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.72     | 0.33      | 0.72   | 0.46     |
| Random Forest       | 0.84     | 0.49      | 0.45   | 0.47     |
| **XGBoost (Best)**  | 0.84     | 0.50      | 0.43   | 0.46     |

---

## 📈 Top Features Driving Attrition

### 🔹 Random Forest

* YearsAtCompany
* Age
* MonthlyIncome

### 🔹 XGBoost

* OverTime\_Yes
* SatisfactionIndex
* YearsAtCompany

### 🧠 SHAP Insights:

* Employees with **low satisfaction + frequent overtime** are at highest attrition risk.

---

## 📄 Deliverables

\- \[x] ✔️ Cleaned & Feature-Selected Dataset

\- \[x] ✔️ Trained Models with Cross-validation

\- \[x] ✔️ SMOTE & Hyperparameter Tuning

\- \[x] ✔️ SHAP Value Analysis

\- \[x] ✔️ Business Report: Top 3 Drivers of Attrition

\- \[x] ✔️ Visualizations & Performance Metrics

---

## 📌 Business Insights Summary

> The top drivers of attrition are **Overtime**, **Low Job Satisfaction**, and **Short Tenure**. Targeted HR interventions (e.g., work-life balance programs, incentive structure, career pathing) can reduce early exits.

---

## 🚀 How to Run

1. Clone the repo
   `git clone https://github.com/JPragna/-Smart_Attrition_Prediction_Module_3.git`

2. Install dependencies
   `pip install -r requirements.txt`

3. Open and run `notebooks/Attrition_Model_Development.ipynb`
   (Ensure Jupyter/Colab is set up)

---
or 
## 🛠️ How to Use

### 1. 📊 Train the Model
Run the notebook:
notebooks/Attrition_Model_Development.ipynb

This trains the models and outputs performance metrics + SHAP plots.

### 2. 🔮 Make Predictions
After training, run:
python predict.py
Ensure your new input data is placed in:

bash
Copy code
data/new_employee_data.csv

## 📊 Model Evaluation

To assess and compare model performance, we evaluated the models using confusion matrices and ROC curves:

### ✅ Evaluated Models:

* Logistic Regression
* Random Forest
* XGBoost

### 📊 Evaluation Visuals:

| Model               | Evaluation Image |
| ------------------- | ---------------- |
| Logistic Regression |                  |
| Random Forest       |                  |
| XGBoost             |                  |

> 📁 All visual outputs are in the `model_evaluation_visual/` folder.

### 🧠 Key Insight

> Ensemble models like Random Forest and XGBoost showed stronger precision and recall. SHAP confirms that overtime and job dissatisfaction are major attrition indicators.

---

## 👩‍💼 Author

**Pragna J**
Data Science Intern | AI Enthusiast

---

## ⭐️ If you like this repo, don't forget to star it!
