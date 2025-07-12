from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

from schemas import CustomerData

app = FastAPI(title="Customer Return Risk Analyzer")

model = joblib.load("model/return_risk_model_XGBoost.pkl")

@app.get("/")
def root():
    return {"message": "Customer Return Risk Model API is up and running."}

@app.post("/predict")
def predict(data: CustomerData):
    input_array = np.array([[
        data.total_orders,
        data.returns,
        data.return_ratio,
        data.product_category_risk_score,
        data.vague_reason_count,
        data.average_return_window,
        data.customer_rating_behavior_score,
        int(data.mismatch_flag_history),  # convert boolean to int
        data.total_monetary_value_of_returns,
        data.average_order_value,
        data.return_frequency_per_month,
        data.time_since_last_return,
        data.customer_tenure_days,
        data.number_of_different_categories_returned
    ]])

    prediction = model.predict(input_array)[0]
    return {"risk_score": round(prediction, 2)}
