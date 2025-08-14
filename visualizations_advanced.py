import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load cleaned data and engineered features
# Assumes this script is in Task_5 and cleaned_mlb_speed.csv is in the same folder

df = pd.read_csv("Task_5/cleaned_mlb_speed.csv")

# Recreate engineered features if needed
speed_percentile = df['sprint_speed_(ft_/_sec)'].rank(pct=True) * 100
age_bins = [19, 24, 29, 34, 40]
age_labels = ['20-24', '25-29', '30-34', '35-40']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, include_lowest=True)
team_speed = df.groupby('team')['sprint_speed_(ft_/_sec)'].mean().rank(ascending=False)
df['team_speed_rank'] = df['team'].map(team_speed)
df['speed_percentile'] = speed_percentile

# Outlier detection
z_scores = np.abs((df['sprint_speed_(ft_/_sec)'] - df['sprint_speed_(ft_/_sec)'].mean()) / df['sprint_speed_(ft_/_sec)'].std())
df['outlier'] = z_scores > 3

# 1. Speed Percentile Histogram
plt.figure(figsize=(8,5))
sns.histplot(df['speed_percentile'], bins=20, color='mediumslateblue')
plt.title('Sprint Speed Percentile Distribution')
plt.xlabel('Percentile')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Task_5/speed_percentile_histogram.png')
plt.close()

# 2. Mean Sprint Speed by Age Group
plt.figure(figsize=(8,5))
sns.barplot(x=df['age_group'].value_counts().index, y=df.groupby('age_group')['sprint_speed_(ft_/_sec)'].mean().values, palette='viridis')
plt.title('Mean Sprint Speed by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Mean Sprint Speed (ft/sec)')
plt.tight_layout()
plt.savefig('Task_5/mean_speed_by_age_group.png')
plt.close()

# 3. Team Speed Rank (Top 10)
top_teams = df.groupby('team')['sprint_speed_(ft_/_sec)'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_teams.index, y=top_teams.values, palette='coolwarm')
plt.title('Top 10 Teams by Mean Sprint Speed')
plt.xlabel('Team')
plt.ylabel('Mean Sprint Speed (ft/sec)')
plt.tight_layout()
plt.savefig('Task_5/top_teams_speed_rank.png')
plt.close()

# 4. Outlier Highlight: Age vs Sprint Speed
plt.figure(figsize=(8,5))
sns.scatterplot(x='age', y='sprint_speed_(ft_/_sec)', data=df, hue='outlier', palette={False:'mediumseagreen', True:'crimson'}, s=60, edgecolor='black')
plt.title('Sprint Speed Outliers (Age vs Speed)')
plt.xlabel('Age')
plt.ylabel('Sprint Speed (ft/sec)')
plt.legend(title='Outlier')
plt.tight_layout()
plt.savefig('Task_5/outlier_scatter.png')
plt.close()
