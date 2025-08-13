from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import os
import tempfile

def create_chart(user_data, history, chart_path=None):
    if not chart_path:
        chart_path = os.path.join(tempfile.gettempdir(), "credit_trend.png")
    timestamps = [h[7] for h in history]  # timestamp
    loans = [h[3] for h in history]  # loan_amount
    plt.figure(figsize=(4, 2))  # Optimized for PDF
    plt.plot(timestamps, loans, marker='o')
    plt.title("Loan Amount Trend")
    plt.xlabel("Date")
    plt.ylabel("Loan Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_path, dpi=100)
    plt.close()
    return chart_path

def create_pdf(credit_score, financial_health, chart_path, filename="credit_health_report.pdf"):
    file_path = os.path.join(tempfile.gettempdir(), filename)
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("AI Credit Planner: Financial Health Report", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"<b>Credit Score:</b> {credit_score}/900", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph(f"<b>Financial Health Score:</b> {financial_health['health_score']}/100 ({financial_health.get('risk_profile', 'Moderate')})", styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph(f"<b>Trend Analysis:</b> {financial_health['trend']}", styles["Normal"]))
    story.append(Spacer(1, 10))

    # Treat ai_recommendation as a string, not a dictionary
    ai_recommendation = financial_health.get('ai_recommendation', 'No AI recommendation available')
    story.append(Paragraph("<b>AI-Powered Recommendations:</b>", styles["Heading2"]))
    story.append(Paragraph(ai_recommendation, styles["Normal"]))
    story.append(Spacer(1, 20))

    if os.path.exists(chart_path):
        story.append(Paragraph("Your Loan Trend:", styles["Heading2"]))
        story.append(Image(chart_path, width=400, height=200))

    doc.build(story)
    return file_path