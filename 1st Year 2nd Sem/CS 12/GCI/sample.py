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
print(f"Raw dataset shape: {anime_data_raw.shape}")

pd.set_option("display.width", None)
pd.set_option("display.max_columns", 15)
pd.set_option("display.max_rows", 35)

print(anime_data_raw.info())
print(anime_data_raw)