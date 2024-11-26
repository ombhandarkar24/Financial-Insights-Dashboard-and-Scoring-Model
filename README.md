
# Financial Insights Dashboard and Scoring Model

This project provides a financial insights dashboard and scoring model that helps users track and analyze their financial health. The system includes a Flask API backend to calculate a financial score based on input data, a Streamlit frontend to interact with the model, and visualizations to display the results and insights.

## Dataset Information

The dataset used in this project contains financial data for families and individuals, including:

- **Family ID**: Unique identifier for the family.
- **Member ID**: Unique identifier for the family member.
- **Income**: Monthly income of the family member.
- **Savings**: Savings amount for the individual or family.
- **Expenses**: Monthly expenses, including discretionary and necessary costs.
- **Loan Payments**: Loan repayment amounts, such as mortgages, personal loans, etc.
- **Credit Card Spending**: Monthly credit card expenditure.
- **Goals Met**: Percentage of financial goals that the individual or family has met.

## Data Cleaning and Preprocessing

In this project, we perform several preprocessing and cleaning steps on the input data:

1. **Missing Data Handling**: We ensure all required fields are populated. If any data is missing, it is flagged for manual correction.
2. **Normalization**: The financial inputs (income, savings, expenses, etc.) are normalized on a 0-1 scale to handle varying ranges and ensure consistency in the scoring model.
3. **Outliers**: Outlier detection and removal steps were performed to ensure the model doesn’t get skewed by extreme values.

The goal of these preprocessing steps is to make the data ready for model input and ensure that financial scoring is accurate and fair.

## Flask API Setup Instructions

To set up and run the Flask API, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/ombhandarkar24/Financial-Insights-Dashboard-and-Scoring-Model.git
cd Financial-Insights-Dashboard-and-Scoring-Model
```

### 2. Install dependencies

Create a virtual environment and install the required dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
```

### 3. Run the Flask API

After setting up the environment, run the Flask API:

```bash
python app.py
```

This will start the Flask server at `http://localhost:5000/`.

### 4. API Endpoints

The Flask API has the following endpoints:

- **POST /calculate_score**: Accepts input data for financial information and returns a calculated financial score.
  - Input: JSON data (income, savings, expenses, etc.)
  - Output: Financial score and insights.

## Streamlit API Setup Instructions

To set up the Streamlit API, follow these steps:

### 1. Clone the repository

If you haven't already cloned the repository, run:

```bash
git clone https://github.com/ombhandarkar24/Financial-Insights-Dashboard-and-Scoring-Model.git
cd Financial-Insights-Dashboard-and-Scoring-Model
```

### 2. Install dependencies

In the same virtual environment, install Streamlit and other dependencies:

```bash
pip install streamlit
pip install -r requirements.txt
```

### 3. Run Streamlit App

Start the Streamlit application by running the following command:

```bash
streamlit run streamlit_app.py
```

This will start the Streamlit app in your browser at `http://localhost:8501/`.

## Financial Scoring Logic and Weights

The financial score is calculated based on several factors, each with a specific weight. The following are the components that contribute to the final financial score:

1. **Income**: Contributes up to 30 points. Higher income contributes more to the score.
2. **Savings**: Contributes up to 25 points. Higher savings indicate better financial health.
3. **Expenses**: Contributes up to 15 points. Lower monthly expenses lead to a higher score.
4. **Loan Payments**: Contributes up to 10 points. Lower loan repayments lead to a higher score.
5. **Credit Card Spending**: Contributes up to 10 points. Lower credit card spending improves the score.
6. **Financial Goals Met**: Contributes up to 10 points. Meeting more financial goals increases the score.

### Calculation Logic

```python
# Normalize inputs (0-1 scale)
income_score = income_normalized * 30  # Income contributes up to 30 points
savings_score = savings_normalized * 25  # Savings contribute up to 25 points
expenses_score = (1 - expenses_normalized) * 15  # Lower expenses contribute up to 15 points
loan_score = (1 - loan_payments_normalized) * 10  # Lower loan payments contribute up to 10 points
credit_score = (1 - credit_spending_normalized) * 10  # Lower credit card spending contributes up to 10 points
goals_met_score = goals_met_normalized * 10  # Financial goals contribute up to 10 points
```

The total score is calculated by summing the individual scores for each category. The final score is then clamped between 0 and 100.

### Final Clamped Score:
```python
score = max(0, min(100, score))
```

## Recommendations for Improving Financial Scores

Based on the calculated financial score, the system provides personalized recommendations to improve financial health:

- **If the score is low (<50)**: Recommendations include reducing discretionary spending (e.g., Food, Entertainment, Travel) by 10%, which could improve the score.
- **If the score is moderate (50-80)**: Recommendations are provided to help improve overall financial management.
- **If the score is high (>80)**: Congratulations! The system provides tips to maintain or further enhance financial health.

### Example Recommendations:

- "Reduce your discretionary spending by 10%, which could improve your score by X points."
- "Increase your savings by 5%, which could improve your score by Y points."

## Visualizations

The Streamlit app includes several visualizations to help users better understand their financial health:

1. **Distribution of Financial Scores**: A histogram displaying the distribution of financial scores across multiple families/individuals.
2. **Income vs Expenses Visualization**: A bar chart comparing income and expenses for each family member.
3. **Savings Over Time**: A line chart displaying savings trends over several months.

These visualizations provide a clear and intuitive way to view financial health at a glance.

## Contributing

Feel free to fork the repository, make changes, and submit a pull request! All contributions are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:

- Replace the actual content in the code comments with your custom dataset and project-specific details.
- If you have added specific models, libraries, or tools to the project, make sure to mention them in the setup instructions section.
- Ensure that the requirements.txt file includes all necessary packages (like `Flask`, `Streamlit`, `Matplotlib`, `Seaborn`, etc.).
