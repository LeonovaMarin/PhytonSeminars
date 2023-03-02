import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Задача №63. Общее обсуждение
# 1. Изобразите отношение households к population с
# помощью точечного графика


file = 'california_housing_train.csv'
df = pd.read_csv(file)
#
# sns.scatterplot(data=df, x='households', y='population')
# plt.show()

# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график

# sns.relplot(data=df, x='longitude', y='median_house_value', kind='line')
# plt.show()


# 3. Представить гистограмму по housing_median_age

# sns.histplot(data=df, x='housing_median_age')
# plt.show()

# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

sns.histplot(data=df, x='median_house_value', hue='housing_median_age', legend=False)
plt.show()