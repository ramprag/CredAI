# rules/engine.py

def evaluate_credit_profile(user_data: dict, credit_score: int) -> dict:
    rules = {
        "Credit score above 700": credit_score > 700,
        "Has stable income": user_data.get("income", 0) > 25000,
        "Low expenses ratio": user_data.get("expenses", 0) < 0.5 * user_data.get("income", 0),
        "Low debt": user_data.get("existing_debt", 0) < 0.3 * user_data.get("income", 0)
    }
    return rules
