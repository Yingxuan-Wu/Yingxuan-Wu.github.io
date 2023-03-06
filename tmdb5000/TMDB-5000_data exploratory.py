import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("tmdb_5000_movies.csv")

#print(data.describe())
#print(data.info())
#print(data.budget.describe())
#plt.scatter(data.popularity, data.vote_average)
##df = data.select_dtypes(['number'])
#df1 = df.pop('id')

#pair = sns.pairplot(df)

#pair.figure.savefig("output.png")

df2 = data.iloc[:, 1:2]
print(df2.head())

import re

pattern = r'(?<="name": ")([A-Za-z]+)'

df3 = []
df3 = df2['genres'].str.extractall(pattern)
print(df3.head())


df3.value_counts().plot(kind="barh", figsize=(12, 6))
plt.title("Value counts of the genre tags")
plt.xlabel("tag type")
plt.xticks(rotation=0)
plt.ylabel("Count")
plt.show()