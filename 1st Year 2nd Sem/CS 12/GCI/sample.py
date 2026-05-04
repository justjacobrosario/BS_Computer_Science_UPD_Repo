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

url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# donwload from url
r = requests.get(url, stream=True)

# read and extract
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
print(r)