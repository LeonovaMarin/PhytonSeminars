import pandas as pd
import matplotlib


df = pd.read_csv('sample_data/california_housing_train.csv')

print(df.head())
#
# df.head(n=10)
#
# df.tail()
#
# df.shape
#
# df.isnull()
#
# df.isnull().sum()
#
# df.dtypes
#
# df.columns
#
# df['latitude']
#
# df[df['housing_median_age'] < 20]
#
# df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]
#
# df[(df['housing_median_age'] > 20) & (df['median_house_value'] > 70000)]
#
# df[df['median_income'] < 2 ,  'median_house_value']
#
# df[df['housing_median_age'] < 20], 'total_rooms'
#
# print(df['median_house_value'].max())
#
# print(df['median_house_value'].min())
#
# from typing_extensions import dataclass_transform
#
#
#
# df[(df['median_income'] == 3.1250)]['population'].max()
#
# print(df[df['median_house_value'] < df['median_house_value'].quantile(.25)]['population'].max())
#
# df.describe()
#
# df[['latitude', 'population']]
#





