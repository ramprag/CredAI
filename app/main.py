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
    st.title("🤖 AI-Powered Credit Health Analyzer")
    st.markdown("*Get personalized financial advice powered by AI*")

    # Initialize database
    init_db()

    # User ID for demo (in production, use auth)
    user_id = st.text_input("Enter User ID (e.g., email or phone)", value="test_user")

    with st.form("credit_input_form"):
        user_data = get_user_input_form()
        submitted = st.form_submit_button("🚀 Analyze with AI")

    if submitted and user_data:
        try:
            # Show AI processing
            with st.spinner("🤖 AI analyzing your financial profile..."):
                # Save user data
                save_user_data(user_id, user_data)

                # Load history
                history = get_user_history(user_id)

                # Calculate financial health
                credit_score, trend, financial_health = calculate_financial_health(user_data, history)
                rules_output = evaluate_credit_profile(user_data, credit_score)

                # Enhanced AI recommendation
                ai_recommendation = get_ai_recommendation(credit_score, trend, financial_health, user_data, history)

            # Generate chart
            chart_path = create_chart(user_data, history)

            # Show insights and dashboard
            show_insights(credit_score, rules_output, ai_recommendation)
            show_dashboard(user_data, credit_score, rules_output)

            # Enhanced metrics
            st.subheader("📊 Financial Health Summary")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Credit Score", f"{credit_score}/900",
                          delta="Excellent" if credit_score >= 750 else "Good" if credit_score >= 650 else "Needs Work")

            with col2:
                debt_ratio = user_data['loan_amount'] / max(user_data['income'], 1)
                st.metric("Debt Ratio", f"{debt_ratio:.1%}",
                          delta="✅ Healthy" if debt_ratio < 0.4 else "⚠️ High")

            with col3:
                # Use get() with fallback to avoid KeyError
                risk_profile = financial_health.get('risk_profile', 'Moderate')
                st.metric("Health Score", f"{financial_health['health_score']}/100",
                          delta=risk_profile)

            with col4:
                surplus = user_data['income'] - user_data['expenses']
                st.metric("Monthly Surplus", f"₹{surplus:,.0f}",
                          delta="Good" if surplus > 5000 else "Tight" if surplus > 0 else "Deficit")

            # Generate PDF with AI recommendations
            financial_health["trend"] = trend
            financial_health["ai_recommendation"] = ai_recommendation
            pdf_path = create_pdf(credit_score, financial_health, chart_path)

            with open(pdf_path, "rb") as f:
                st.download_button(
                    "📥 Download AI Financial Report",
                    f,
                    file_name="ai_credit_health_report.pdf",
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Error processing your request: {str(e)}. Please check your inputs and try again.")

if __name__ == "__main__":
    main()