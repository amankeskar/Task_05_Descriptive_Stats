import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Task_5/cleaned_mlb_speed.csv")

# Boxplot: Sprint Speed by Position (with color)
plt.figure(figsize=(10,6))
sns.boxplot(x='position', y='sprint_speed_(ft_/_sec)', data=df, palette='Set2')
plt.title('Sprint Speed by Position')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Task_5/boxplot_sprint_speed_by_position.png')
plt.close()

# Histogram: Distribution of Sprint Speeds (with color)
plt.figure(figsize=(8,5))
sns.histplot(df['sprint_speed_(ft_/_sec)'], bins=20, kde=True, color='dodgerblue')
plt.title('Distribution of Sprint Speeds')
plt.xlabel('Sprint Speed (ft/sec)')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Task_5/histogram_sprint_speed.png')
plt.close()

# Scatter Plot: Age vs Sprint Speed (with color)
plt.figure(figsize=(8,5))
sns.scatterplot(x='age', y='sprint_speed_(ft_/_sec)', data=df, color='mediumseagreen', s=60, edgecolor='black')
sns.regplot(x='age', y='sprint_speed_(ft_/_sec)', data=df, scatter=False, color='crimson', line_kws={'label':'Linear fit'})
plt.title('Age vs Sprint Speed')
plt.xlabel('Age')
plt.ylabel('Sprint Speed (ft/sec)')
plt.legend()
plt.tight_layout()
plt.savefig('Task_5/scatter_age_vs_sprint_speed.png')
plt.close()

# Improved Bar Plot: Mean Sprint Speed by Team (Top 10, with color)
team_stats = df.groupby('team').agg(
    mean_speed=('sprint_speed_(ft_/_sec)', 'mean'),
    player_count=('player', 'count')
).sort_values('mean_speed', ascending=False)
top_teams = team_stats.head(10)
plt.figure(figsize=(12,6))
bar = sns.barplot(x=top_teams.index, y=top_teams['mean_speed'], palette='coolwarm')
plt.title('Top 10 Teams by Mean Sprint Speed (with Player Count)')
plt.xlabel('Team')
plt.ylabel('Mean Sprint Speed (ft/sec)')
for i, (team, row) in enumerate(top_teams.iterrows()):
    plt.text(i, row['mean_speed'] + 0.03, f"n={row['player_count']}", ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('Task_5/barplot_top_teams_mean_speed.png')
plt.close()

# Count Plot: Number of Players per Position (with color)
plt.figure(figsize=(8,5))
sns.countplot(x='position', data=df, order=df['position'].value_counts().index, palette='pastel')
plt.title('Number of Players per Position')
plt.xlabel('Position')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('Task_5/countplot_players_per_position.png')
plt.close()
