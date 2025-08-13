from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import os

def create_chart(user_data, history, chart_path="credit_trend.png"):
    timestamps = [h[6] for h in history]  # timestamp
    loans = [h[3] for h in history]  # loan_amount
    plt.figure(figsize=(6, 3))
    plt.plot(timestamps, loans, marker='o')
    plt.title("Loan Amount Trend")
    plt.xlabel("Date")
    plt.ylabel("Loan Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def create_pdf(credit_score, financial_health, chart_path, filename="credit_health_report.pdf"):
    file_path = f"{filename}"
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("AI Credit Planner: Financial Health Report", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"<b>Credit Score:</b> {credit_score}/900", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph(f"<b>Financial Health Score:</b> {financial_health['health_score']}/100 ({financial_health['risk_profile']})", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph(f"<b>Trend Analysis:</b> {financial_health['trend']}", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph(f"<b>Debt Repayment Plan:</b> {financial_health['repayment_plan'].get('strategy', 'None')}", styles["Normal"]))
    story.append(Paragraph(f"- {financial_health['repayment_plan'].get('monthly_payment', 'No loans to repay.')}", styles["Normal"]))
    story.append(Paragraph(f"- Tip: {financial_health['repayment_plan'].get('tip', 'Maintain timely payments.')}", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph(f"<b>Investment Suggestions:</b>", styles["Normal"]))
    for inv in financial_health["investments"]:
        story.append(Paragraph(f"- {inv}", styles["Normal"]))
    story.append(Spacer(1, 20))

    if os.path.exists(chart_path):
        from reportlab.platypus import Image
        story.append(Paragraph("Your Loan Trend:", styles["Heading2"]))
        story.append(Image(chart_path, width=400, height=200))

    doc.build(story)
    return file_path