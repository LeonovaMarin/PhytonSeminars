import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Задача №65. Решение в группах
# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

file = 'penguins.csv'
df = pd.read_csv(file)
# print(df.head())
# print(df.describe())

# sns.boxplot(data=df, x='species', y='bill_length_mm')
# plt.show()

# cols = ['bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# plt.show()

# sns.scatterplot(data=df, x='species', y='island')
# plt.show()

# sns.scatterplot(data=df, x='bill_length_mm', y='species')
# plt.show()
# sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='bill_length_mm', size='bill_length_mm', sizes=(2, 100))
# plt.show()

# sns.PairGrid(data=df, hue='species').map(sns.scatterplot).add_legend()
# plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True)
# plt.show()
#
# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# sns.heatmap(data=df[cols], annot=True)
# plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot = True, square=True, vmin=-1, vmax=1, center= 0, cmap= 'crest', cbar_kws={'orientation': 'horizontal'})
# plt.show()

df[['bill_length_mm', 'bill_len']]
df.groupby('bill_len')['bill_length_mm'].mean()
fd.groupby('bill_len')['bill_length_mm'].mean().plot(kind='bar')
plt.show()