import pandas as pd

df = pd.read_csv(r"C:\\Users\\amank\\OneDrive - Syracuse University\\Syracuse Master Folder\\Research Analyst Project for OPT\\Task_5\\cleaned_mlb_speed.csv")

with open("desc_stats_output.txt", "w") as f:
    f.write('--- Sprint Speed Summary ---\n')
    f.write(str(df['sprint_speed_(ft_/_sec)'].describe()) + '\n\n')

    f.write('--- Unique Players and Teams ---\n')
    f.write(f"Unique players: {df['player'].nunique()}\n")
    f.write(f"Unique teams: {df['team'].nunique()}\n\n")

    f.write('--- Age Distribution ---\n')
    f.write(f"Min age: {df['age'].min()}\n")
    f.write(f"Max age: {df['age'].max()}\n")
    f.write(f"Mean age: {df['age'].mean()}\n")
    f.write(f"Median age: {df['age'].median()}\n\n")

    f.write('--- Top 10 Fastest Players ---\n')
    f.write(str(df[['player','team','position','sprint_speed_(ft_/_sec)']].sort_values('sprint_speed_(ft_/_sec)', ascending=False).head(10)) + '\n\n')

    f.write('--- Top 10 Slowest Players ---\n')
    f.write(str(df[['player','team','position','sprint_speed_(ft_/_sec)']].sort_values('sprint_speed_(ft_/_sec)').head(10)) + '\n\n')

    f.write('--- Mean Sprint Speed by Position ---\n')
    f.write(str(df.groupby('position')['sprint_speed_(ft_/_sec)'].mean().sort_values(ascending=False)) + '\n\n')

    f.write('--- Number of Players per Position ---\n')
    f.write(str(df['position'].value_counts()) + '\n\n')

    f.write('--- Correlation: Age vs Sprint Speed ---\n')
    f.write(str(df[['age', 'sprint_speed_(ft_/_sec)']].corr()) + '\n\n')

    f.write('--- Missing Data Summary ---\n')
    f.write(str(df.isnull().sum()) + '\n')
