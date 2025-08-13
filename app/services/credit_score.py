def calculate_financial_health(user_data: dict, history: list) -> tuple[int, str, dict]:
    income = user_data.get("income", 0)
    expenses = user_data.get("expenses", 0)
    loan_amount = user_data.get("loan_amount", 0)
    credit_util = user_data.get("credit_util", 0)
    missed_payments = user_data.get("missed_payments", 0)

    # Weighted credit score (0–900)
    base_score = 500
    income_factor = min(income / 100000, 2) * 100  # Max 200 points
    debt_factor = max(0, (1 - loan_amount / max(income, 1)) * 150)  # Max 150 points
    util_factor = max(0, (1 - credit_util / 100) * 150)  # Max 150 points
    payment_factor = max(0, (1 - missed_payments / 12) * 100)  # Max 100 points
    credit_score = max(300, min(int(base_score + income_factor + debt_factor + util_factor + payment_factor), 900))

    # Financial health score (0–100)
    debt_to_income = loan_amount / max(income, 1)
    health_score = 100
    health_score -= min(40, debt_to_income * 40)  # Debt-to-income penalty
    health_score -= min(30, credit_util / 100 * 30)  # Credit utilization penalty
    health_score -= min(20, missed_payments * 5)  # Missed payments penalty
    health_score = max(0, int(health_score))

    # Trend analysis
    trend = "No historical data available."
    if history and len(history) > 1:
        prev_data = history[1]  # Second most recent entry
        prev_loan = prev_data[3]  # loan_amount
        loan_change = loan_amount - prev_loan
        if loan_change > 0:
            trend = f"Your loan amount increased by ₹{loan_change:.0f} since last input."
            credit_score -= min(50, loan_change / 10000)  # Penalty for debt increase
        elif loan_change < 0:
            trend = f"Your loan amount decreased by ₹{-loan_change:.0f}, great job!"
            credit_score += min(50, -loan_change / 10000)  # Bonus for debt reduction
        else:
            trend = "Your loan amount is stable."

    # Debt repayment plan
    repayment_plan = {}
    if loan_amount > 0:
        monthly_payment = loan_amount / 36  # Assume 3-year repayment
        repayment_plan["strategy"] = "Debt Snowball"
        repayment_plan["monthly_payment"] = f"Pay ₹{monthly_payment:.0f}/month for 3 years to clear ₹{loan_amount:.0f}."
        repayment_plan["tip"] = "Focus on paying off smallest loans first for quick wins."

    # Investment suggestions
    investments = []
    risk_profile = "Conservative" if health_score < 50 else "Moderate" if health_score < 75 else "Aggressive"
    if risk_profile == "Conservative":
        investments.append("Fixed Deposit: 6–7% p.a., invest ₹5,000/month for 3 years to generate ₹20,000 for debt repayment.")
        investments.append("Debt Mutual Fund: SBI Debt Hybrid Fund, 6–8% p.a., invest ₹3,000/month.")
    elif risk_profile == "Moderate":
        investments.append("Balanced Mutual Fund: HDFC Balanced Advantage Fund, 8–10% p.a., invest ₹5,000/month to clear ₹50,000 debt in 5 years.")
        investments.append("Fixed Deposit: 6–7% p.a., invest ₹2,000/month.")
    else:
        investments.append("Equity Mutual Fund: Parag Parikh Flexi Cap Fund, 10–12% p.a., invest ₹5,000/month to clear ₹100,000 debt in 5 years.")
        investments.append("Balanced Mutual Fund: ICICI Prudential Equity & Debt Fund, 9–11% p.a., invest ₹3,000/month.")

    return credit_score, trend, {
        "health_score": health_score,
        "repayment_plan": repayment_plan,
        "investments": investments,
        "risk_profile": risk_profile
    }

def get_ai_recommendation(credit_score: int, trend: str, financial_health: dict) -> str:
    health_score = financial_health["health_score"]
    repayment_plan = financial_health["repayment_plan"]
    investments = financial_health["investments"]
    risk_profile = financial_health["risk_profile"]

    recommendation = (
            f"Your financial health score is {health_score}/100 ({risk_profile} risk profile). {trend}\n\n"
            f"**Debt Repayment Plan**: {repayment_plan.get('strategy', 'None')}\n"
            f"- {repayment_plan.get('monthly_payment', 'No loans to repay.')}\n"
            f"- Tip: {repayment_plan.get('tip', 'Maintain timely payments.')}\n\n"
            f"**Investment Suggestions**:\n"
            + "\n".join([f"- {inv}" for inv in investments])
    )
    return recommendation