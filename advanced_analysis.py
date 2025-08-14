import pandas as pd
import numpy as np
from scipy import stats

# Load cleaned data
# Assumes this script is in Task_5 and cleaned_mlb_speed.csv is in the same folder

df = pd.read_csv("Task_5/cleaned_mlb_speed.csv")

# Feature Engineering
# Speed Percentile
speed_percentile = df['sprint_speed_(ft_/_sec)'].rank(pct=True) * 100
# Age Group
age_bins = [19, 24, 29, 34, 40]
age_labels = ['20-24', '25-29', '30-34', '35-40']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, include_lowest=True)
# Team Speed Rank
team_speed = df.groupby('team')['sprint_speed_(ft_/_sec)'].mean().rank(ascending=False)
df['team_speed_rank'] = df['team'].map(team_speed)
df['speed_percentile'] = speed_percentile

# Advanced Analysis Output
with open("advanced_analysis_output.txt", "w") as f:
    f.write("--- Feature Engineering ---\n")
    f.write("Sample of new features:\n")
    f.write(str(df[['player','team','position','age','age_group','sprint_speed_(ft_/_sec)','speed_percentile','team_speed_rank']].head(10)))
    f.write("\n\n")

    # T-test: Compare sprint speed between infielders (1B, 2B, 3B, SS) and outfielders (LF, CF, RF)
    infield = df[df['position'].isin(['1B','2B','3B','SS'])]['sprint_speed_(ft_/_sec)']
    outfield = df[df['position'].isin(['LF','CF','RF'])]['sprint_speed_(ft_/_sec)']
    t_stat, p_val = stats.ttest_ind(infield, outfield, nan_policy='omit')
    f.write("--- T-test: Infield vs Outfield Sprint Speed ---\n")
    f.write(f"t-statistic: {t_stat:.3f}, p-value: {p_val:.4f}\n")
    f.write(f"Mean Infield: {infield.mean():.2f}, Mean Outfield: {outfield.mean():.2f}\n\n")

    # ANOVA: Compare sprint speed across all positions
    f.write("--- ANOVA: Sprint Speed by Position ---\n")
    groups = [df[df['position']==pos]['sprint_speed_(ft_/_sec)'] for pos in df['position'].unique()]
    f_stat, p_val = stats.f_oneway(*groups)
    f.write(f"F-statistic: {f_stat:.3f}, p-value: {p_val:.4f}\n\n")

    # Regression: Predict sprint speed from age
    f.write("--- Regression: Sprint Speed vs Age ---\n")
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['age'], df['sprint_speed_(ft_/_sec)'])
    f.write(f"slope: {slope:.3f}, intercept: {intercept:.3f}, r^2: {r_value**2:.3f}, p-value: {p_value:.4f}\n\n")

    # Outlier Detection
    f.write("--- Outlier Detection (Sprint Speed) ---\n")
    z_scores = np.abs(stats.zscore(df['sprint_speed_(ft_/_sec)'], nan_policy='omit'))
    outliers = df[z_scores > 3][['player','team','position','sprint_speed_(ft_/_sec)']]
    f.write(f"Number of outliers (>3 std): {outliers.shape[0]}\n")
    f.write(str(outliers) + "\n\n")

    # Speed by Age Group
    f.write("--- Mean Sprint Speed by Age Group ---\n")
    f.write(str(df.groupby('age_group')['sprint_speed_(ft_/_sec)'].mean()) + "\n\n")

    # Speed by Team Speed Rank
    f.write("--- Mean Sprint Speed by Team Speed Rank (Top 5) ---\n")
    top_teams = df.groupby('team').mean(numeric_only=True).sort_values('sprint_speed_(ft_/_sec)', ascending=False).head(5)
    f.write(str(top_teams[['sprint_speed_(ft_/_sec)','team_speed_rank']]) + "\n\n")
