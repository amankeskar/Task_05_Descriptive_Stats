import pandas as pd

# Read the Excel file (update to read_csv if using CSV)
df = pd.read_excel("Task_5/MLB_Max Running Speed (2015 to May 2021).xlsx")

# Clean column names
cols = [col.strip().replace(" ", "_").lower() for col in df.columns]
df.columns = cols

# Convert sprint_speed_(ft_/_sec) to numeric (if not already)
df['sprint_speed_(ft_/_sec)'] = pd.to_numeric(df['sprint_speed_(ft_/_sec)'], errors='coerce')

# Drop duplicates
df = df.drop_duplicates()

# Drop rows with missing values in critical columns (season, player, sprint_speed)
df = df.dropna(subset=['season', 'player', 'sprint_speed_(ft_/_sec)'])

# Filter for 2020 season only
df = df[df['season'] == 2020]

# Show summary
# print(df.columns)
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())

# Save cleaned data in the same folder as this script
df.to_csv("cleaned_mlb_speed.csv", index=False)



# Descriptive statistics
print('--- Sprint Speed Summary ---')
print(df['sprint_speed_(ft_/_sec)'].describe())

print('\n--- Unique Players and Teams ---')
print('Unique players:', df['player'].nunique())
print('Unique teams:', df['team'].nunique())

print('\n--- Age Distribution ---')
print('Min age:', df['age'].min())
print('Max age:', df['age'].max())
print('Mean age:', df['age'].mean())
print('Median age:', df['age'].median())

print('\n--- Top 10 Fastest Players ---')
print(df[['player','team','position','sprint_speed_(ft_/_sec)']].sort_values('sprint_speed_(ft_/_sec)', ascending=False).head(10))

print('\n--- Top 10 Slowest Players ---')
print(df[['player','team','position','sprint_speed_(ft_/_sec)']].sort_values('sprint_speed_(ft_/_sec)').head(10))

print('\n--- Mean Sprint Speed by Position ---')
print(df.groupby('position')['sprint_speed_(ft_/_sec)'].mean().sort_values(ascending=False))

print('\n--- Number of Players per Position ---')
print(df['position'].value_counts())

print('\n--- Correlation: Age vs Sprint Speed ---')
print(df[['age', 'sprint_speed_(ft_/_sec)']].corr())

print('\n--- Missing Data Summary ---')
print(df.isnull().sum())

## Visualizations have been moved to visualizations.py for clarity.

