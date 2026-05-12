import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

series = Series(
	[2, 4, 6, 8, 10],
	index=['A', 'B', 'C', 'D', 'E']
	)

raw = {
	"FIRST" : ["Juan", "Jacob", "John"],
	"LAST" : ["Dela Cruz", "Rosario", "Cena"]
	}
processed = DataFrame(raw, index=["a", "b", "c"])

'''print("index: ", processed.index)
print("values: ", processed.values)
print("columns: ", processed.columns)'''


import requests, zipfile
from io import StringIO
import io

# Download MyAnimeList data from GitHub
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'
r = requests.get(url, stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# Load the anime data
anime_data_raw = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
#print(anime_data_raw.info())

pd.set_option("display.width", None)
pd.set_option("display.max_columns", 15)
pd.set_option("display.max_rows", 35)

#print(anime_data_raw)


def homework(anime_data, metric_column, n) -> pd.Series:
    data = anime_data.sort_values(by=metric_column, ascending=False)
    total = data[metric_column].sum()

    groups = pd.qcut(data[metric_column], q=n, labels = [str(i) for i in range(0, n)])
    
    res = data.groupby(groups, observed = True)[metric_column].sum().sort_values(ascending=False).astype(float)
    for i, val in enumerate(res):
        res.iloc[i] = val / total

    res.index = [f"Group {i+1}" for i in range(len(res))]

    return res
print(homework(anime_data_raw, "Completed", 5))

'''
Group 1    0.945830
Group 2    0.044025
Group 3    0.008230
Group 4    0.001560
Group 5    0.000354
Name: Completed, dtype: float64
'''