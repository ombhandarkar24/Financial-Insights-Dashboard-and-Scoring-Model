import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Scoring Calculation Function
def calculate_financial_score(income, savings, expenses, loan_payments, credit_card_spending, goals_met):
    MAX_INCOME = 10000
    MAX_SAVINGS = 5000
    MAX_EXPENSES = 3000
    MAX_LOAN_PAYMENTS = 1000
    MAX_CREDIT_SPENDING = 1000
    MAX_GOALS_MET = 100

    income_normalized = min(income / MAX_INCOME, 1)
    savings_normalized = min(savings / MAX_SAVINGS, 1)
    expenses_normalized = min(expenses / MAX_EXPENSES, 1)
    loan_payments_normalized = min(loan_payments / MAX_LOAN_PAYMENTS, 1)
    credit_spending_normalized = min(credit_card_spending / MAX_CREDIT_SPENDING, 1)
    goals_met_normalized = min(goals_met / MAX_GOALS_MET, 1)

    income_score = income_normalized * 30
    savings_score = savings_normalized * 25
    expenses_score = max(0, (1 - expenses_normalized)) * 15
    loan_score = max(0, (1 - loan_payments_normalized)) * 10
    credit_score = max(0, (1 - credit_spending_normalized)) * 10
    goals_met_score = goals_met_normalized * 10

    contributions = {
        "Income": income_score,
        "Savings": savings_score,
        "Expenses": expenses_score,
        "Loan Payments": loan_score,
        "Credit Card Spending": credit_score,
        "Goals Met": goals_met_score,
    }

    score = sum(contributions.values())
    score = max(0, min(100, score))
    return score, contributions


# Generate Recommendations
def generate_recommendations(contributions, income, expenses, loan_payments, credit_card_spending, savings):
    recommendations = []
    if contributions["Expenses"] < 15:
        reduction_amount = expenses * 0.1
        potential_gain = 15 * (reduction_amount / 3000)
        recommendations.append(f"Reduce monthly expenses by $100 to $200 to improve your score by approximately {potential_gain:.2f} points.")
    if contributions["Loan Payments"] < 10:
        reduction_amount = loan_payments * 0.1
        potential_gain = 10 * (reduction_amount / 1000)
        recommendations.append(f"Reduce loan payments by $50 to improve your score by {potential_gain:.2f} points.")
    if contributions["Credit Card Spending"] < 10:
        reduction_amount = credit_card_spending * 0.1
        potential_gain = 10 * (reduction_amount / 1000)
        recommendations.append(f"Lower credit card spending by $50 to $100 to enhance your score by {potential_gain:.2f} points.")
    if contributions["Savings"] < 25:
        additional_savings = savings * 0.2
        potential_gain = 25 * (additional_savings / 5000)
        recommendations.append(f"Increase savings by $200 to $400 to improve your score by {potential_gain:.2f} points.")
    if not recommendations:
        recommendations.append("Your financial score is excellent. Keep up the great work!")
    return recommendations


# Streamlit App
st.title("Financial Scoring Model and Recommendations")

# Input Fields
st.header("Enter Family Financial Information")
family_id = st.text_input("Family ID")
member_id = st.text_input("Member ID")
income = st.number_input("Income ($)", min_value=0, step=1000)
savings = st.number_input("Savings ($)", min_value=0, step=1000)
expenses = st.number_input("Monthly Expenses ($)", min_value=0, step=100)
loan_payments = st.number_input("Loan Payments ($)", min_value=0, step=100)
credit_card_spending = st.number_input("Credit Card Spending ($)", min_value=0, step=100)
goals_met = st.number_input("Financial Goals Met (%)", min_value=0, max_value=100, step=1)

# Calculate Financial Score
if st.button("Calculate Financial Score"):
    score, contributions = calculate_financial_score(
        income, savings, expenses, loan_payments, credit_card_spending, goals_met
    )
    st.subheader(f"Calculated Financial Score: {score:.2f}")

    # Display Contributions
    st.subheader("Score Contributions:")
    for key, value in contributions.items():
        st.write(f"{key}: {value:.2f}")

    # Generate Recommendations
    recommendations = generate_recommendations(contributions, income, expenses, loan_payments, credit_card_spending, savings)
    st.subheader("Recommendations to Improve Your Financial Score:")
    for rec in recommendations:
        st.write(f"- {rec}")

    # Visualization 1: Bar Chart (Contributions)
    fig, ax = plt.subplots(figsize=(8, 6))
    categories = list(contributions.keys())
    values = list(contributions.values())
    sns.barplot(x=values, y=categories, palette="Blues_d", ax=ax)
    ax.set_title("Financial Score Contributions")
    ax.set_xlabel("Points")
    ax.set_ylabel("Categories")
    st.pyplot(fig)

    # Visualization 2: Pie Chart (Contribution Percentages)
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.pie(values, labels=categories, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("Blues", len(values)))
    plt.title("Contribution Breakdown")
    st.pyplot(fig)

    # Visualization 3: Simulated Score Trend (What-if Analysis)
    improvements = np.arange(0, 21, 5)  # Simulate improvements (0% to 20%)
    simulated_scores = [calculate_financial_score(
        income, savings + savings * (improve / 100),
        expenses - expenses * (improve / 100),
        loan_payments - loan_payments * (improve / 100),
        credit_card_spending - credit_card_spending * (improve / 100),
        goals_met
    )[0] for improve in improvements]

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(improvements, simulated_scores, marker="o", linestyle="--", color="blue")
    plt.title("Simulated Financial Score Trend")
    plt.xlabel("Improvement Percentage")
    plt.ylabel("Simulated Financial Score")
    plt.grid(True)
    st.pyplot(fig)
