---
subject: GCI
field: programming
subfield: data science
---

# 1: Data Science Process (OSEMM)

## 1) Obtain
: Gather data from relevant sources

## 2) Scrub
: Clean data to formats that machine understands
: Convert to digestible data format for machine to process it

## 3) Explore
: Find significant patterns and trends using statistical methods

## 4) Model
: construct models to predict and forecast using those patterns

## 5) Interpret
: Put the results into good use

: about 80% of all work comes from Obtain to Explore

# 2: Scrub (Data Cleaning)

### 1. Types of Data
#### 1] Structured Data
: Tabular and Standardized
: e.g.
	1. Fixed length file
	2. Excel/CSV
	3. RDB Data

#### 2] Semi-structured Data
: Not Tabular
: Standardized
: e.g.
	1. XML
	2. JSON
	3. HTML
#### 3] Unstructured Data
: Not Tabular
: Not Standardized
: e.g.
	1. text
	2. audio
	3. image
	4. video
	5. sensor log

# 3: Pandas

: a library that enables data to be used as a numeric table
: enables processing various types of data
: i.e. can handle data like as if you were using Excel

libraries used
```python
import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame
```

## 1. Pros and Cons

### 1) Pros
1. Can process numerical data, time-series data, and charac strings
2. Strong in data aggregation and other data processing methods
3. Reads and writes csv, excel, json, and other file formats

### 2) Cons
1. Slow calculation speed
2. High memory consumption

## 2. Pandas Data Structures

### 1) Series
: 1-Dimension
: only has rows
```md
               column 1
       index    Val
row 1    0      2
row 2    1      4
row 3    2      6
```

e.g.
```python
series = Series([2, 4, 6, 8, 10])
print(series)

"""
0     2
1     4
2     6
3     8
4    10
dtype: int64
"""
```

: left part is the indices, and the right are the values
: `dtype`tells the data type

#### 1] Change the index
```python
series = Series(
	[2, 4, 6, 8, 10],
	index=['A', 'B', 'C', 'D', 'E']
	)

print(series)
'''
series = Series(
	[2, 4, 6, 8, 10],
	index=['A', 'B', 'C', 'D', 'E']
	)

print(series)
'''
```

#### 2] .values and .index
```python
series = Series(
	[2, 4, 6, 8, 10],
	index=['A', 'B', 'C', 'D', 'E']
	)

print(series.values)
# [ 2  4  6  8 10]
```

### 2) DataFrame
: 2-Dimension
: has rows and columns
```md
               column 1    column 2
       index    FIRST       LAST
row 1    0      Juan        Dela Cruz
row 2    1      Jacob       Rosario
row 3    2      John        Cena
```


: in a form of a dictionary
```python
raw = {
	"FIRST" : ["Juan", "Jacob", "John"],
	"LAST" : ["Dela Cruz", "Rosario", "Cena"]
	}
processed = DataFrame(raw)

print(processed)
'''
   FIRST       LAST
0   Juan  Dela Cruz
1  Jacob    Rosario
2   John       Cena
'''
```

#### 1] Change the index
: same thing using `index=[...]`

#### 2] Dataframe methods
: `.index`, `.values`, `.columns`
```python
raw = {
	"FIRST" : ["Juan", "Jacob", "John"],
	"LAST" : ["Dela Cruz", "Rosario", "Cena"]
	}
processed = DataFrame(raw, index=["a", "b", "c"])

print("index: ", processed.index)
print("values: ", processed.values)
print("columns: ", processed.columns)
```

#### 3] Previewing a large Data frame
: u can use `.head()` to view some column and rows
: `.head(n)` where n is the number of rows itll display

## 3. Data Extraction

### 1) Downloading ZIP files

: additional imports
```python
import requests, zipfile
from io import StringIO
import io
```

#### 1] Download and extract data from the URL

```python

url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# donwload from url
r = requests.get(url, stream=True)

# read and extract
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
# basically the file is in the same folder

```

#### 2] Reading as a DataFrame
`panda.read_csv("file_name.csv")`

```python
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')

print(anime_data.head())

'''
   MAL_ID                             Name Score  ... Score-3 Score-2 Score-1
0       1                     Cowboy Bebop  8.78  ...  1357.0   741.0  1580.0
1       5  Cowboy Bebop: Tengoku no Tobira  8.39  ...   221.0   109.0   379.0
2       6                           Trigun  8.24  ...   664.0   316.0   533.0
3       7               Witch Hunter Robin  7.27  ...   353.0   164.0   131.0
4       8                   Bouken Ou Beet  6.98  ...    83.0    50.0    27.0

[5 rows x 35 columns]
'''
```

### 2) Data frame advanced methods

#### 1] Number and type of data per column
`.info()`

```python
anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')

anime_data.info()

"""
RangeIndex: 17562 entries, 0 to 17561
Data columns (total 35 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   MAL_ID         17562 non-null  int64
 1   Name           17562 non-null  str  
 2   Score          17562 non-null  str  
 3   Genres         17562 non-null  str  
 4   English name   17562 non-null  str  
 5   Japanese name  17562 non-null  str  
 6   Type           17562 non-null  str  
 7   Episodes       17562 non-null  str  
 8   Aired          17562 non-null  str  
 9   Premiered      17562 non-null  str  
 10  Producers      17562 non-null  str  
 11  Licensors      17562 non-null  str  
 12  Studios        17562 non-null  str  
 13  Source         17562 non-null  str  
 14  Duration       17562 non-null  str  
 15  Rating         17562 non-null  str  
 16  Ranked         17562 non-null  str  
 17  Popularity     17562 non-null  int64
 18  Members        17562 non-null  int64
 19  Favorites      17562 non-null  int64
 20  Watching       17562 non-null  int64
 21  Completed      17562 non-null  int64
 22  On-Hold        17562 non-null  int64
 23  Dropped        17562 non-null  int64
 24  Plan to Watch  17562 non-null  int64
 25  Score-10       17562 non-null  str  
 26  Score-9        17562 non-null  str  
 27  Score-8        17562 non-null  str  
 28  Score-7        17562 non-null  str  
 29  Score-6        17562 non-null  str  
 30  Score-5        17562 non-null  str  
 31  Score-4        17562 non-null  str  
 32  Score-3        17562 non-null  str  
 33  Score-2        17562 non-null  str  
 34  Score-1        17562 non-null  str  
dtypes: int64(9), str(26)
memory usage: 4.7 MB
"""
```

: basically tells if the data of each column has a count (non-null) or not (null), the data type (dtype), etc