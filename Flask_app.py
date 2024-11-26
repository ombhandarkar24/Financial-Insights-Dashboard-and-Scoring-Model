from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Function to calculate the financial score
def calculate_financial_score(data):
    try:
        # Calculate the key metrics
        data['savings_to_income'] = (data['Savings'] / data['Income']) * 100
        data['expenses_to_income'] = (data['Monthly_Expenses'] / data['Income']) * 100
        data['loan_to_income'] = (data['Loan_Payments'] / data['Income']) * 100

        # Credit Card Spending as a percentage of income
        data['credit_card_trend'] = data['Credit_Card_Spending'] / data['Income'] * 100

        # Calculate the total spending by category
        category_spending = data.groupby('Category')['Amount'].sum()  # Sum of spending by category
        total_spending = data['Amount'].sum()
        category_spending_percent = (category_spending / total_spending) * 100

        # Define categories and assign weight to each based on whether they are essential or non-essential
        essential_categories = ['Groceries', 'Healthcare', 'Utilities', 'Food']
        non_essential_categories = ['Entertainment', 'Travel']

        # Initialize the category score
        category_spending_score = {}

        # Apply scoring logic based on category
        for category in category_spending_percent.index:
            if category in essential_categories:
                # For essential categories, spending has less impact on score
                category_spending_score[category] = 100
            elif category in non_essential_categories:
                # For non-essential categories, higher spending reduces the score
                if category_spending_percent[category] > 20:
                    category_spending_score[category] = 50  # Lower score if spending > 20% on non-essential
                else:
                    category_spending_score[category] = 80  # Neutral impact

        # Assign spending category score to each row based on family category spending
        data['spending_category_score'] = 0
        for index, row in data.iterrows():
            category = row['Category']
            data.at[index, 'spending_category_score'] = category_spending_score.get(category, 100)

        # Inside the calculate_financial_score function
            data['financial_goals_score'] = data['Financial_Goals_Met']  # Ensure the correct column name is used



        # Final Scoring Calculation
        data['financial_score'] = (
            data['savings_to_income'] * 0.2 +
            (100 - data['expenses_to_income']) * 0.2 +
            (100 - data['loan_to_income']) * 0.2 +
            (100 - data['credit_card_trend']) * 0.15 +
            data['spending_category_score'] * 0.15 +
            data['financial_goals_score'] * 0.1
        )

        # Ensure final score is between 0 and 100
        data['financial_score'] = data['financial_score'].clip(0, 100)

        # Extract Family ID, Member ID, and financial score
        results = data[['Family_ID', 'Member_ID', 'financial_score']]

        # Generate insights
        insights = {
            "savings_insight": f"Savings are below recommended levels, affecting your score by {100 - data['savings_to_income'].mean():.2f} points.",
            "expenses_insight": f"Expenses are high relative to income, affecting your score by {100 - data['expenses_to_income'].mean():.2f} points.",
            "loan_insight": f"Loan payments are affecting your score by {100 - data['loan_to_income'].mean():.2f} points.",
            "credit_card_trend_insight": f"Credit card spending is affecting your score by {100 - data['credit_card_trend'].mean():.2f} points."
        }

        return results, insights
    except Exception as e:
        print(f"Error in calculate_financial_score: {str(e)}")
        return None, {"error": str(e)}

# Home route to show the input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to calculate the financial score from the form submission
@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    try:
        # Get the 'Financial_Goals_Met' from the form
        financial_goals_met = request.form.get('Financial_Goals_Met', '').strip()

        # Check if the 'Financial_Goals_Met' field is empty
        if financial_goals_met == '':
            return jsonify({"error": "Financial Goals Met field is missing."}), 400

        # Convert to a float
        try:
            financial_goals_met = float(financial_goals_met)
        except ValueError:
            return jsonify({"error": f"Invalid value for Financial Goals Met: {financial_goals_met}"}), 400

        # Prepare data
        data = {
            "Family_ID": request.form['Family_ID'],
            "Member_ID": request.form['Member_ID'],
            "Income": float(request.form['Income']),
            "Savings": float(request.form['Savings']),
            "Monthly_Expenses": float(request.form['Monthly_Expenses']),
            "Loan_Payments": float(request.form['Loan_Payments']),
            "Credit_Card_Spending": float(request.form['Credit_Card_Spending']),
            "Category": request.form['Category'],
            "Amount": float(request.form['Amount']),
            "Financial_Goals_Met": financial_goals_met
        }

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Call the financial score calculation function
        results, insights = calculate_financial_score(df)

        if results is None:
            return jsonify(insights), 500

        # Render the result in result.html template
        return render_template('result.html', 
                               financial_score=results.to_dict(orient='records'),
                               insights=insights)

    except KeyError as e:
        return jsonify({"error": f"Missing data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
