# PREDICTION TEAM WIN IN ENGLISH PREMIER LEAGUE (TRAIN / TEST)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 1. LOAD DATA
data = pd.read_excel("data_clean_two.xlsx")

# 2. CREATE TARGET VARIABLE (ACTUAL RESULT)
# Win = 1, Draw/Loss = 0
data["actual_win"] = (data["goals_for"] > data["goals_against"]).astype(int)

# 3. TRAIN / TEST SPLIT (80/20)
train_data, test_data = train_test_split(
    data,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

# 4. FUNCTION TO CALCULATE TEAM AVERAGES (TRAINING DATA ONLY)
def team_averages(team_name):
    team_data = train_data[train_data["team"] == team_name]

    if team_data.empty:
        return None

    return {
        "xg": team_data["xg"].mean(),
        "xga": team_data["xga"].mean(),
        "shots_on_target": team_data["shots_on_target"].mean()
    }

# 5. PERFORMANCE SCORE FUNCTION
def performance_score(stats):
    return (stats["xg"] - stats["xga"]) + 0.5 * stats["shots_on_target"]

# 6. WIN PROBABILITY FUNCTION (LOGISTIC – STABLE)
def win_probability(score_a, score_b):
    diff = score_a - score_b
    return 1 / (1 + np.exp(-diff))

# 7. TESTING PHASE
predictions = []

for _, row in test_data.iterrows():
    team = row["team"]
    opponent = row["opponent"]

    team_stats = team_averages(team)
    opp_stats = team_averages(opponent)

    # Skip if stats not available (rare teams)
    if team_stats is None or opp_stats is None:
        continue

    team_score = performance_score(team_stats)
    opp_score = performance_score(opp_stats)

    prob = win_probability(team_score, opp_score)
    predicted_win = 1 if prob > 0.5 else 0

    predictions.append({
        "team": team,
        "opponent": opponent,
        "win_probability": prob,
        "predicted_win": predicted_win,
        "actual_win": row["actual_win"]
    })

results_df = pd.DataFrame(predictions)


# 8. MODEL ACCURACY (OVERALL)
accuracy = (results_df["predicted_win"] == results_df["actual_win"]).mean()
print(f"\nModel accuracy on test data: {accuracy:.2%}")


# 9. CASE STUDY: Aston Villa
main_team = "Aston Villa"
aston_villa_results = results_df[results_df["team"] == main_team]

aston_villa_accuracy = (
    aston_villa_results["predicted_win"] == aston_villa_results["actual_win"]
).mean()

print(f"\n{main_team} prediction accuracy: {aston_villa_accuracy:.2%}")

# 10. VISUALIZATION – WIN PROBABILITY DISTRIBUTION
plt.figure()
plt.hist(aston_villa_results["win_probability"], bins=10)
plt.title(f"{main_team} – Predicted Win Probability (Test Matches)")
plt.xlabel("Win Probability")
plt.ylabel("Number of Matches")
plt.show()
