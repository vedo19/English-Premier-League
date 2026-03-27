# English Premier League Data Analysis (Last 5 Seasons)

## Overview
This repository is a Business Intelligence and analytics project based on English Premier League data from the last 5 seasons.

The dataset includes match and team-level variables such as:
- team and opponent
- match result
- venue
- formation
- xg (expected goals)
- xga (expected goals against)
- possession
- shots on target
- referee
- goals for / goals against
- and other match statistics

The project is split into 3 practical parts:
1. Python scripts for prediction and model checking
2. Excel analysis for descriptive statistics and regression
3. Power BI dashboard for interactive visual exploration

---

## Repository Structure
- `case_1.py` -> simple win probability estimation for one team against selected opponents
- `case_2.py` -> train/test evaluation of the same idea on historical data
- `data_clean_two.xlsx` -> cleaned dataset used by both Python scripts
- `BI_Football_Analysis_Workfile.xlsx` -> Excel-based BI and statistical analysis
- `Projekat_utakmice.pbix` -> Power BI dashboard project
- `Premier League Data Analysis & Prediction.pptx` -> presentation material

---

## Part 1: Python Scripts

### 1) `case_1.py` - Win Probability for Aston Villa (vs selected teams)
Goal: estimate Aston Villa win probability against a few opponents (Arsenal, Chelsea, Crystal Palace, Liverpool) using average team performance statistics.

How it works:
1. Load the cleaned Excel data.
2. For each team, compute average values of:
   - xg
   - xga
   - goals_for
   - goals_against
   - shots_on_target
3. Build a simple performance score:

   score = (xg - xga) + 0.5 * shots_on_target

4. Compare Aston Villa score with opponent score.
5. Convert score difference into win probability using a linear mapping:

   prob = 0.5 + 0.1 * (score_A - score_B)

6. Clamp the result to [0.05, 0.95] to avoid extreme outputs.
7. Print a result table and plot:
   - bar chart of Aston Villa win probability vs opponents
   - bar chart of team performance scores

This script is intentionally simple and easy to interpret.

### 2) `case_2.py` - Train/Test Validation
Goal: test how good this simple modeling approach is compared to real match outcomes.

How it works:
1. Load the same cleaned Excel data.
2. Create target variable:
   - actual_win = 1 if goals_for > goals_against, else 0
3. Split data into train/test sets (80/20, random_state=42).
4. Compute team average features only from training data:
   - xg, xga, shots_on_target
5. Use the same performance score formula:

   score = (xg - xga) + 0.5 * shots_on_target

6. Convert score difference to probability with logistic function:

   prob = 1 / (1 + exp(-(score_A - score_B)))

7. Predict win if probability > 0.5.
8. Evaluate:
   - overall test accuracy
   - Aston Villa specific prediction accuracy
9. Visualize Aston Villa predicted probability distribution (histogram).

Why this is useful:
- It gives a basic baseline model.
- It shows how much predictive signal we can get from simple aggregated statistics.
- It creates a bridge between descriptive BI and predictive analytics.

---

## Part 2: Excel Analysis (`BI_Football_Analysis_Workfile.xlsx`)
Excel is used for tabular BI analysis and statistical summaries, including:
- data manipulation and filtering
- descriptive statistics
- average wins and average goals by team
- regression statistics (linear regression)
- comparison of team-level performance metrics

This part supports the Python and Power BI parts by providing transparent, easy-to-audit calculations.

---

## Part 3: Power BI Dashboard (`Projekat_utakmice.pbix`)
Power BI is used for interactive visualization of the same football dataset.

Dashboard capabilities include:
- filtering by team, opponent, and match context
- viewing match outcomes and key KPIs
- inspecting formation, shots on goal, referee, and other variables
- comparing patterns across teams and matches

This part is focused on visual storytelling and interactive decision support.

---

## Technologies Used
- Python
  - pandas
  - numpy
  - matplotlib
  - scikit-learn (train/test split)
- Microsoft Excel
- Microsoft Power BI

---

## How to Run Python Scripts
1. Ensure Python 3 is installed.
2. Install required packages:

   pip install pandas numpy matplotlib scikit-learn openpyxl

3. Keep `data_clean_two.xlsx` in the same folder as scripts.
4. Run scripts:

   python case_1.py
   python case_2.py

---

## Notes
- The Python models are intentionally simple and educational.
- Results depend on feature engineering choices and train/test split.
- The project can be extended with richer features, time-aware validation, or advanced ML models.
