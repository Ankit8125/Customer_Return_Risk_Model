from pydantic import BaseModel

class CustomerData(BaseModel):
    total_orders: int
    returns: int
    return_ratio: float
    product_category_risk_score: float
    vague_reason_count: int
    average_return_window: int
    customer_rating_behavior_score: float
    mismatch_flag_history: bool
    total_monetary_value_of_returns: float
    average_order_value: float
    return_frequency_per_month: float
    time_since_last_return: int
    customer_tenure_days: int
    number_of_different_categories_returned: int
