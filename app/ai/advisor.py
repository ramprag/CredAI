def generate_advice(credit_score: float, income: float, debts: float) -> str:
    if credit_score >= 750:
        risk_level = "Excellent"
        suggestion = "You're managing your credit exceptionally well. Consider long-term investments or prepaying loans."
    elif 650 <= credit_score < 750:
        risk_level = "Good"
        suggestion = "You're on the right path. Lowering your debt can help push you into excellent range."
    elif 550 <= credit_score < 650:
        risk_level = "Average"
        suggestion = "Focus on reducing existing debts and avoid new credit lines to improve your financial health."
    else:
        risk_level = "Poor"
        suggestion = "Immediate action needed. Limit unnecessary spending, build emergency funds, and consult a financial advisor."

    debt_ratio = debts / income if income > 0 else 0
    if debt_ratio > 0.5:
        debt_comment = "Your debt-to-income ratio is high. Aim to reduce debts."
    else:
        debt_comment = "Your debt-to-income ratio is manageable. Keep tracking it monthly."

    return (
        f"🧠 **AI Financial Health Checkup**\n\n"
        f"- Credit Score: **{credit_score:.0f}** ({risk_level})\n"
        f"- Debt-to-Income Ratio: **{debt_ratio:.2f}**\n"
        f"- Advice: {suggestion}\n"
        f"- Comment: {debt_comment}"
    )
