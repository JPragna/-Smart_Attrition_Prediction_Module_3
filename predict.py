import joblib
import pandas as pd

model = joblib.load("xgb_model.pkl")
data = pd.read_csv("new_employee_data.csv")  # your test input
predictions = model.predict(data)
print(predictions)
