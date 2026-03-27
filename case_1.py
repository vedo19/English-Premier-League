# PREDICTION TEAM WIN IN ENGLISH PREMIER LEAGUE

import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD DATA
data = pd.read_excel("data_clean_two.xlsx")

# 2. SELECT TEAMS
main_team = "Aston Villa"
opponents = ["Arsenal", "Chelsea", "Crystal Palace", "Liverpool"]

# 3. FUNCTION TO CALCULATE AVERAGES (mean package used)
def team_averages(team_name):
    team_data = data[data["team"] == team_name]

    return {
        "xg": team_data["xg"].mean(),
        "xga": team_data["xga"].mean(),
        "goals_for": team_data["goals_for"].mean(),
        "goals_against": team_data["goals_against"].mean(),
        "shots_on_target": team_data["shots_on_target"].mean()
    }

# 4. PERFORMANCE SCORE FUNCTION (Model formula, 0.5 will be used to balance the weight of shots on target)
def performance_score(stats):
    return (
        (stats["xg"] - stats["xga"]) +
        0.5 * stats["shots_on_target"]
    )

# 5. WIN PROBABILITY FUNCTION (Simple linear mapping with clamping)
def win_probability(score_a, score_b):
    diff = score_a - score_b
    prob = 0.5 + diff * 0.1

    # Clamp between 5% and 95%
    prob = max(0.05, min(0.95, prob))
    return prob

# 6. CALCULATE MAIN TEAM STATS
main_stats = team_averages(main_team)
main_score = performance_score(main_stats)

results = []

# 7. LOOP THROUGH OPPONENTS
for opp in opponents:
    opp_stats = team_averages(opp)
    opp_score = performance_score(opp_stats)
    prob = win_probability(main_score, opp_score)

    results.append({
        "Opponent": opp,
        "Win Probability": prob
    })

# 8. RESULTS TABLE
wh_stats = team_averages(main_team)
print(f"Mean values for {main_team}:")
print(f"  xg: {wh_stats['xg']:.2f}")
print(f"  xga: {wh_stats['xga']:.2f}")
print(f"  goals_for: {wh_stats['goals_for']:.2f}")
print(f"  goals_against: {wh_stats['goals_against']:.2f}")
print(f"  shots_on_target: {wh_stats['shots_on_target']:.2f}")
print(f"\nPerformance score for {main_team}: {main_score:.2f}")
for opp in opponents:
    opp_stats = team_averages(opp)
    opp_score = performance_score(opp_stats)
    print(f"Performance score for {opp}: {opp_score:.2f}")
results_df = pd.DataFrame(results)
print("\nWin Probability Predictions:\n")
print(results_df)

# 9. BAR CHART – WIN PROBABILITY
plt.figure()
plt.bar(results_df["Opponent"], results_df["Win Probability"])
plt.title(f"{main_team} – Estimated Win Probability")
plt.ylabel("Probability")
plt.ylim(0, 1)
plt.show()
scores = [main_score]
labels = [main_team]

for opp in opponents:
    opp_stats = team_averages(opp)
    scores.append(performance_score(opp_stats))
    labels.append(opp)

plt.figure()
plt.bar(labels, scores)
plt.title("Team Performance Scores")
plt.ylabel("Score")
plt.show()