import streamlit as st
from ui.form import get_user_input_form
from ui.layout import show_insights, show_dashboard
from rules.engine import evaluate_credit_profile
from services.credit_score import calculate_financial_health, get_ai_recommendation
from db import init_db, save_user_data, get_user_history
from reports.pdf_generator import create_pdf, create_chart
import os

def main():
    st.set_page_config(page_title="AI Credit Planner", layout="wide")
    st.title("💳 AI-Based Credit Health Analyzer")

    # Initialize database
    init_db()

    # User ID for demo (in production, use auth)
    user_id = st.text_input("Enter User ID (e.g., email or phone)", value="test_user")

    with st.form("credit_input_form"):
        user_data = get_user_input_form()
        submitted = st.form_submit_button("Analyze")

    if submitted and user_data:
        # Save user data
        save_user_data(user_id, user_data)

        # Load history
        history = get_user_history(user_id)

        # Calculate financial health
        credit_score, trend, financial_health = calculate_financial_health(user_data, history)
        rules_output = evaluate_credit_profile(user_data, credit_score)
        ai_recommendation = get_ai_recommendation(credit_score, trend, financial_health)

        # Generate chart
        chart_path = create_chart(user_data, history)

        # Show insights and dashboard
        show_insights(credit_score, rules_output, ai_recommendation)
        show_dashboard(user_data, credit_score, rules_output)

        # Generate PDF
        financial_health["trend"] = trend  # Add trend to financial_health for PDF
        pdf_path = create_pdf(credit_score, financial_health, chart_path)
        with open(pdf_path, "rb") as f:
            st.download_button("Download Financial Health Report", f, file_name="credit_health_report.pdf")

if __name__ == "__main__":
    main()