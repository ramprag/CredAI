# REPLACE your app/ui/form.py with this enhanced version:

import streamlit as st

def get_user_input_form():
    """Enhanced form to collect data for AI-powered recommendations"""

    st.markdown("### 💰 Basic Financial Information")
    col1, col2 = st.columns(2)

    with col1:
        income = st.number_input("Monthly Income (₹)", min_value=0, value=50000,
                                 help="Your total monthly income from all sources")
        expenses = st.number_input("Monthly Expenses (₹)", min_value=0, value=30000,
                                   help="Your essential monthly expenses (rent, food, utilities)")
        loan_amount = st.number_input("Total Outstanding Debt (₹)", min_value=0, value=0,
                                      help="Credit cards, personal loans, car loans (exclude home loan)")

    with col2:
        credit_util = st.slider("Credit Card Utilization (%)", 0, 100, 30,
                                help="How much of your credit limit are you using?")
        missed_payments = st.number_input("Missed Payments (last 12 months)", min_value=0, max_value=12, value=0,
                                          help="Any late payments on credit cards or loans")

    st.markdown("### 👤 Personal & Risk Profile")
    col3, col4 = st.columns(2)

    with col3:
        age = st.number_input("Age", min_value=18, max_value=80, value=30,
                              help="Your current age")
        dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=0,
                                     help="Spouse, children, parents you financially support")

    with col4:
        job_stability = st.selectbox("Job Stability",
                                     ["stable", "uncertain", "new_job", "self_employed"],
                                     help="How stable is your current income source?")

        risk_appetite = st.selectbox("Investment Risk Appetite",
                                     ["low", "moderate", "high"],
                                     help="How comfortable are you with investment risks?")

    st.markdown("### 🎯 Financial Goals & Preferences")

    financial_goals = st.multiselect(
        "Select Your Financial Goals (next 2-5 years)",
        ["emergency_fund", "debt_free", "buy_house", "buy_car", "child_education",
         "retirement_planning", "travel", "start_business", "wedding"],
        help="What are you saving/planning for?"
    )

    col5, col6 = st.columns(2)
    with col5:
        current_investments = st.multiselect(
            "Current Investments",
            ["none", "fd", "mutual_funds", "stocks", "ppf", "nps", "gold", "real_estate"],
            help="What investments do you currently have?"
        )

    with col6:
        preferred_investment_duration = st.selectbox(
            "Investment Time Horizon",
            ["1-2 years", "3-5 years", "5-10 years", "10+ years"],
            help="How long can you invest without needing the money?"
        )

    st.markdown("### 🏦 Banking & Credit Information")
    col7, col8 = st.columns(2)

    with col7:
        primary_bank = st.selectbox(
            "Primary Bank",
            ["SBI", "HDFC", "ICICI", "Axis", "Kotak", "PNB", "BOB", "Others"],
            help="Which bank do you primarily use?"
        )

        existing_credit_cards = st.number_input(
            "Number of Credit Cards", min_value=0, max_value=10, value=1,
            help="How many credit cards do you currently have?"
        )

    with col8:
        last_credit_check = st.selectbox(
            "Last Credit Score Check",
            ["never", "6+ months ago", "3-6 months ago", "1-3 months ago", "this month"],
            help="When did you last check your credit score?"
        )

        loan_types = st.multiselect(
            "Types of Current Loans",
            ["none", "credit_card", "personal_loan", "car_loan", "home_loan", "education_loan"],
            help="What types of loans do you currently have?"
        )

    # Additional context
    st.markdown("### 💭 Additional Information")
    financial_concerns = st.text_area(
        "Any specific financial concerns or questions?",
        placeholder="E.g., planning to switch jobs, major expense coming up, worried about debt, want to start investing...",
        help="This helps AI provide more personalized advice"
    )

    return {
        # Basic financial data
        "income": income,
        "expenses": expenses,
        "loan_amount": loan_amount,
        "credit_util": credit_util,
        "missed_payments": missed_payments,

        # Personal profile
        "age": age,
        "dependents": dependents,
        "job_stability": job_stability,
        "risk_appetite": risk_appetite,

        # Goals and preferences
        "financial_goals": financial_goals,
        "current_investments": current_investments,
        "preferred_investment_duration": preferred_investment_duration,

        # Banking info
        "primary_bank": primary_bank,
        "existing_credit_cards": existing_credit_cards,
        "last_credit_check": last_credit_check,
        "loan_types": loan_types,

        # Additional context
        "financial_concerns": financial_concerns
    }