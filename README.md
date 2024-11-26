# Financial Insights Dashboard and API

This project provides a financial scoring model with an interactive dashboard (built using Streamlit) and an API (built using Flask) for calculating and visualizing financial scores based on user inputs. It also offers insights and recommendations to improve financial health.

## Features
1. **Flask API**:
   - Accepts financial data via POST requests.
   - Calculates financial scores based on various inputs.
   - Provides JSON responses with scores and recommendations.
2. **Streamlit Dashboard**:
   - User-friendly interface for inputting financial data.
   - Displays financial scores, insights, and recommendations.
   - Includes visualizations like score distribution and spending breakdown.
3. **Model Logic**:
   - A scoring model that normalizes financial parameters and calculates a score between 0 and 100.
   - Provides insights into credit card spending, expenses, loans, and savings.
   - Generates actionable recommendations (e.g., "Reduce discretionary spending by 10% to improve your score by X points").

---

## Installation and Setup

### Prerequisites
1. Python 3.8 or later.
2. Pip (Python package installer).

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
