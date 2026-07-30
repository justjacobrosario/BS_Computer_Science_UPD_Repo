import numpy as np
import pandas as pd
from pandas import DataFrame

# Libraries for retrieving data from the web and handling zip files
import requests, zipfile
from io import StringIO
import io

# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

# Load and clean the data
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_data_extracted = anime_data[anime_data['Score'] != 'Unknown'].copy()
anime_data_extracted['Score'] = pd.to_numeric(anime_data_extracted['Score'])

pd.set_option('display.max_columns', 6) 

def homework(anime_data_extracted):
	types = anime_data_extracted["Type"].unique()
	new = {"Type" : [], "Mean" : []}
	for type in types:
		new["Type"].append(type)
		new["Mean"].append(anime_data_extracted[(anime_data_extracted["Type"] == type)]["Score"].mean())
	new = DataFrame(new)
	return new

def homework(anime_data_extracted):
    types = anime_data_extracted["Type"].unique()
    new = []
    for type in types:
        new.append(anime_data_extracted[(anime_data_extracted["Type"] == type)]["Score"].mean())
    new = pd.Series(sorted(new, reverse=True))
    return new


#print(anime_data_extracted["Type"].unique())
#print(anime_data_extracted[(anime_data_extracted["Type"] == type)]["Score"].mean())

result = homework(anime_data_extracted)
print(result)
