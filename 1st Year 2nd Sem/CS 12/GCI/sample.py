import pandas as pd
from pandas import Series, DataFrame

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

# Preprocessing — Do NOT modify this cell
columns_to_keep = ['MAL_ID', 'Name', 'Score', 'Type', 'Episodes',
                   'Members', 'Completed', 'Watching', 'Dropped', 'Popularity']
anime_data = anime_data_raw[columns_to_keep].copy()

# Remove rows where key metric columns have missing or zero values
anime_data = anime_data.dropna(subset=['Members', 'Completed', 'Watching'])
anime_data = anime_data[(anime_data['Members'] > 0) &
                        (anime_data['Completed'] > 0) &
                        (anime_data['Watching'] > 0)]
anime_data = anime_data.reset_index(drop=True)
print(f"Dataset shape after preprocessing: {anime_data.shape}")
anime_data.head()


def homework(anime_data, metric_column, n):
    data = anime_data.sort_values(by=metric_column, ascending=False)
    total = data[metric_column].sum()
    
    ranks = data[metric_column].rank(method='first', ascending=False)
    groups = pd.qcut(ranks, q=n, labels=[str(i) for i in range(n)])
    
    res = data.groupby(groups, observed=True)[metric_column].sum()
    res = res / total
    
    res.index = [f"Group {i+1}" for i in range(len(res))]
    return res

print(homework(anime_data, "Completed", 5))
print("helo")


'''
Group 1    0.945830
Group 2    0.044025
Group 3    0.008230
Group 4    0.001560
Group 5    0.000354
Name: Completed, dtype: float64
'''

