import pandas as pd

df = pd.read_csv('Watched.csv')

print(sorted(df['UserID'].unique()))