

"""задача 40"""

df[df['population'] <= 500]['median_house_value'].mean()

df['population'] <= 500

"""Задача 42"""

df['population'].quantile(.25)

df['population'] < df['population'].quantile(.25)

print(df[df['population'] < df['population'].quantile(.25)]['households'].max())