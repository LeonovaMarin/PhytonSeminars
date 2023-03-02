import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

df = pd.read_csv('sample_data/california_housing_train.csv')
#
# """задача 40"""
#
# df[df['population'] <= 500]['median_house_value'].mean()
#
# df['population'] <= 500
# print(df['population'] <= 500)
#


# """Задача 42"""
#
# df['population'].quantile(.25)
#
# df['population'] < df['population'].quantile(.25)
#
# print(df[df['population'] < df['population'].quantile(.25)]['households'].max())