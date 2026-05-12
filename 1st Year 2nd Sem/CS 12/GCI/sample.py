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
print(anime_data_raw.info())

pd.set_option("display.width", None)
pd.set_option("display.max_columns", 15)
pd.set_option("display.max_rows", 35)

def homework(anime_data: pd.DataFrame, metric_column: str, n: int) -> pd.Series:
    total = anime_data.shape[0]
    print("TOTALLLL: ", total)
    anime_data.sort_values(by=metric_column, ascending=False)
print(homework(anime_data_raw, "Completed", 10))