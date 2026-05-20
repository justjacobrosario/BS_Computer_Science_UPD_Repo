# common
import numpy as np
import pandas as pd
from sklearn import linear_model

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


def homework(anime_data_extracted, X_column, Y_column):
    X = anime_data_extracted[[X_column]]
    y = anime_data_extracted[Y_column]

    model = linear_model.LinearRegression()
    model.fit(X, y)
    result = model.score(X, y)
    return result

result = homework(anime_data_extracted, X_column='Members', Y_column='Completed')
print(result)