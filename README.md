# 📊 Smart Attrition Prediction – Module 3

## 🎯 Objective
To predict employee attrition risk using ML models and extract interpretable business insights.

## 🧠 Key Techniques
- Logistic Regression, Random Forest, XGBoost
- SMOTE for class balancing
- Hyperparameter tuning (GridSearchCV)
- Feature importance + SHAP explanations

## 🔍 Dataset
- Source: [Mention source or synthetic]
- Rows: 1176
- Features: 50+

## 🛠️ Technologies Used
- Python, scikit-learn, XGBoost, SHAP
- Pandas, NumPy, Matplotlib, Seaborn

## 🧪 Models & Evaluation
| Model             | Precision | Recall | F1-Score | Accuracy |
|------------------|-----------|--------|----------|----------|
| Logistic Reg.     | 0.33      | 0.72   | 0.46     | 0.72     |
| Random Forest     | 0.49      | 0.45   | 0.47     | 0.84     |
| XGBoost           | 0.50      | 0.43   | 0.46     | 0.84     |

## 🔥 Top Attrition Drivers
### Random Forest:
1. YearsAtCompany
2. Age
3. MonthlyIncome

### XGBoost:
1. OverTime_Yes
2. SatisfactionIndex
3. YearsAtCompany

## 📈 SHAP Values
> Visuals show how each feature contributes to individual predictions.
![shap-summary](outputs/picture.png)

## 📄 Business Insights
📄 [View Business Report](Business_Report_Module3.md)


## 🧰 Setup
```bash
git clone https://github.com/JPragna/-Smart_Attrition_Prediction_Module_3
cd Smart_Attrition_Prediction_Module_3
pip install -r requirements.txt
