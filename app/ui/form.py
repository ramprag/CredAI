import streamlit as st

def get_user_input_form():
    income = st.number_input("Monthly Income (₹)", min_value=0)
    expenses = st.number_input("Monthly Expenses (₹)", min_value=0)
    loan_amount = st.number_input("Total Loan Amount (₹)", min_value=0)
    credit_util = st.slider("Credit Card Utilization (%)", 0, 100, 30)
    missed_payments = st.number_input("Missed Payments (in last 12 months)", min_value=0)

    return {
        "income": income,
        "expenses": expenses,
        "loan_amount": loan_amount,
        "credit_util": credit_util,
        "missed_payments": missed_payments
    }
