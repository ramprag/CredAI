import streamlit as st

def show_insights(credit_score, rules_output, ai_recommendation):
    st.subheader("📊 Credit Score Summary")
    st.metric("Credit Score", f"{credit_score} / 1000")

    st.subheader("✅ Rule-Based Insights")
    for rule, status in rules_output.items():
        st.write(f"**{rule}**: {status}")

    st.subheader("🤖 AI Recommendation")
    st.info(ai_recommendation)

def show_dashboard(user_data, credit_score, rules_output):
    st.subheader("📈 Credit Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Income", f"₹{user_data['income']}")
    col2.metric("Expenses", f"₹{user_data['expenses']}")
    col3.metric("Loan Amount", f"₹{user_data['loan_amount']}")

    st.progress(min(credit_score / 1000, 1.0))
