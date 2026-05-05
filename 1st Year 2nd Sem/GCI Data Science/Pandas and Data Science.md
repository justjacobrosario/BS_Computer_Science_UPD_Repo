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

##### 1. Setting column or row limit
```python
pd.set_option('display.max_columns', 6) 
pd.set_option('display.max_rows', 7) 
```
##### 2. Simple preview via `.head()`
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

### 2) Data frame extraction methods

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

#### 2] Transposition
`.T`

:basically switch rows to columns and vice-versa

#### 3] Extracting only a column/s
`data_frame_var["column_name, ..."]`

```python
print(anime_data["Name"])
'''
0                           Cowboy Bebop
1        Cowboy Bebop: Tengoku no Tobira
2                                 Trigun
3                     Witch Hunter Robin
4                         Bouken Ou Beet
                      ...               
17557    Daomu Biji Zhi Qinling Shen Shu
17558                       Mieruko-chan
17559    Higurashi no Naku Koro ni Sotsu
17560        Yama no Susume: Next Summit
17561                      Scarlet Nexus
Name: Name, Length: 17562, dtype: str
'''
```


#### 4] Extracting a row/s
`data_frame_var.loc[index_num]`
:if only one row, this returns a series, else a data frame
: if mulitple rows, the index slicing here is INCLUSIVE

```python
print(anime_data.head().loc[0:3])

'''
   MAL_ID                             Name Score  ... Score-3 Score-2 Score-1
0       1                     Cowboy Bebop  8.78  ...  1357.0   741.0  1580.0
1       5  Cowboy Bebop: Tengoku no Tobira  8.39  ...   221.0   109.0   379.0
2       6                           Trigun  8.24  ...   664.0   316.0   533.0
3       7               Witch Hunter Robin  7.27  ...   353.0   164.0   131.0

[4 rows x 35 columns]
'''
```

`data_frame_var.loc[index_num, [col1, col2]]`
: you can only view needed columns

```python
print(anime_data.head().loc[0:3, ["Name", "Score"]])

'''
                              Name Score
0                     Cowboy Bebop  8.78
1  Cowboy Bebop: Tengoku no Tobira  8.39
2                           Trigun  8.24
3               Witch Hunter Robin  7.27
'''
```


#### 5] Assigning and Replacing Values
: like in Python dicts, assigning a value to a new key will make a new key-value pair, while referring to an existing key replaces the existing value

```python
anime_data['Score'] = 0
```

#### 6] Extracting Data with Conditions
: basically just use conditional operators  and the condition itself

: one can return a DataFrame of bools depending on the condition
e.g.
```python
data1 = {
    'id': ['0', '1', '2', '3', '4', '6', '8', '11', '12', '13'],
    'city': ['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo', 'Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'birth_year': [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
    'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steeve', 'Mituru', 'Aoi', 'Tarou', 'Suguru', 'Mitsuo']
}
df1 = DataFrame(data1)
filtered = print(df1["city"] == "Tokyo")
filtered

'''
0     True
1    False
2    False
3    False
4     True
5     True
6    False
7    False
8    False
9     True
Name: city, dtype: bool
'''
```

: by indexing the condition to the dataframe itself, you are filtering the rows that is true to the condition/s
e.g.
```python
data1 = {
    'id': ['0', '1', '2', '3', '4', '6', '8', '11', '12', '13'],
    'city': ['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo', 'Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'birth_year': [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
    'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steeve', 'Mituru', 'Aoi', 'Tarou', 'Suguru', 'Mitsuo']
}
df1 = DataFrame(data1)
filtered = print(df1[(df1["city"] == "Tokyo")])
filtered

'''
   id   city  birth_year     name
0   0  Tokyo        1990  Hiroshi
4   4  Tokyo        1982   Steeve
5   6  Tokyo        1991   Mituru
9  13  Tokyo        1981   Mitsuo
'''
```

#### 7] Checking for missing data `nan` (null)
`.isnull()` returns a dataframe of bools regarding if the cell is `nan` or not


#### 8] Sorting Values
: Series and DataFrame objects can be sorted

##### 1. Sort by Index via `.sort_index()`
##### 2. Sort by values via `.sort_values(by="column_name", ascending=True)`
e.g.
```python
df1.sort_values(by="birth_year", ascending=True)
'''
   id      city  birth_year     name
0   0     Tokyo        1990  Hiroshi
1   1     Osaka        1989    Akiko
2   2     Kyoto        1992     Yuki
3   3  Hokkaido        1997   Satoru
4   4     Tokyo        1982   Steeve
5   6     Tokyo        1991   Mituru
6   8     Osaka        1988      Aoi
7  11     Kyoto        1990    Tarou
8  12  Hokkaido        1995   Suguru
9  13     Tokyo        1981   Mitsuo
'''
```


### 3) DataFrame modifying methods
#### 1] Merging Data
: lets use anime_list, anime_data, anime_synop as sample dataframes
```python
print(anime_data.head())
'''
   MAL_ID                             Name Score  ... Score-3 Score-2 Score-1
0       1                     Cowboy Bebop  8.78  ...  1357.0   741.0  1580.0
1       5  Cowboy Bebop: Tengoku no Tobira  8.39  ...   221.0   109.0   379.0
2       6                           Trigun  8.24  ...   664.0   316.0   533.0
3       7               Witch Hunter Robin  7.27  ...   353.0   164.0   131.0
4       8                   Bouken Ou Beet  6.98  ...    83.0    50.0    27.0
'''
print(anime_list.head())
'''
   user_id  anime_id  rating  watching_status  watched_episodes
0        0        67       9                1                 1
1        0      6702       7                1                 4
2        0       242      10                1                 4
3        0      4898       0                1                 1
4        0        21      10                1                 0
'''
print(anime_synop.head())
'''
   MAL_ID  ...                                          sypnopsis
0       1  ...  In the year 2071, humanity has colonized sever...
1       5  ...  other day, another bounty—such is the life of ...
2       6  ...  Vash the Stampede is the man with a $$60,000,0...
3       7  ...  ches are individuals with special powers like ...
4       8  ...  It is the dark century and the people are suff...
'''
```

##### 1. Merging relative to the intersection (inner join)
`pd.merge()`
: by default it merges the 'inner join' part (only data that is presentin both two DataFrame is seen)
e.g.
```python
pd.set_option('display.max_columns', 7) 
merged = pd.merge(anime_data, anime_synop)
print(merged)
'''
       MAL_ID                             Name    Score  ...  Score-2  \
0           1                     Cowboy Bebop     8.78  ...    741.0   
1           5  Cowboy Bebop: Tengoku no Tobira     8.39  ...    109.0   
2           6                           Trigun     8.24  ...    316.0   
3           7               Witch Hunter Robin     7.27  ...    164.0   
4           8                   Bouken Ou Beet     6.98  ...     50.0   
...       ...                              ...      ...  ...      ...   
16209   48481  Daomu Biji Zhi Qinling Shen Shu  Unknown  ...  Unknown   
16210   48483                     Mieruko-chan  Unknown  ...  Unknown   
16211   48488  Higurashi no Naku Koro ni Sotsu  Unknown  ...  Unknown   
16212   48491      Yama no Susume: Next Summit  Unknown  ...  Unknown   
16213   48492                    Scarlet Nexus  Unknown  ...  Unknown   

       Score-1                                          sypnopsis  
0       1580.0  In the year 2071, humanity has colonized sever...  
1        379.0  other day, another bounty—such is the life of ...  
2        533.0  Vash the Stampede is the man with a $$60,000,0...  
3        131.0  ches are individuals with special powers like ...  
4         27.0  It is the dark century and the people are suff...  
...        ...                                                ...  
16209  Unknown  No synopsis information has been added to this...  
16210  Unknown  ko is a typical high school student whose life...  
16211  Unknown          Sequel to Higurashi no Naku Koro ni Gou .  
16212  Unknown                          New Yama no Susume anime.  
16213  Unknown  Solar calendar year 2020: grotesque organisms ...  
'''
```
: since this datafram is too wide, it is cut in half in display
: notice that the "MAL_ID" is the common column between them, so thats the key on which to merge

##### 2. Merging relative to index
`.join([dataframe1, dataframe2])`

```python
merged = pd.join(anime_data, anime_synop)
print(merged)
```

#### 2] Concatenating DataFrames
##### 1. Default concatenation
`pd.concat()`
: it concatenates data frames vertically
e.g.
```python
data1 = {
    'id': ['0', '1', '2', '3', '4', '6', '8', '11', '12', '13'],
    'city': ['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo', 'Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'birth_year': [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
    'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steeve', 'Mituru', 'Aoi', 'Tarou', 'Suguru', 'Mitsuo']
}
df1 = DataFrame(data1)

data3 = {
    'id': ['117', '118', '119', '120', '125'],
    'city': ['Chiba', 'Kanagawa', 'Tokyo', 'Fukuoka', 'Okinawa'],
    'birth_year': [1990, 1989, 1992, 1997, 1982],
    'name': ['Suguru', 'Kouichi', 'Satochi', 'Yukie', 'Akari']
}
df3 = DataFrame(data3)


concat = pd.concat([df1, df3])
print(concat)


'''
    id      city  birth_year     name
0    0     Tokyo        1990  Hiroshi
1    1     Osaka        1989    Akiko
2    2     Kyoto        1992     Yuki
3    3  Hokkaido        1997   Satoru
4    4     Tokyo        1982   Steeve
5    6     Tokyo        1991   Mituru
6    8     Osaka        1988      Aoi
7   11     Kyoto        1990    Tarou
8   12  Hokkaido        1995   Suguru
9   13     Tokyo        1981   Mitsuo
0  117     Chiba        1990   Suguru
1  118  Kanagawa        1989  Kouichi
2  119     Tokyo        1992  Satochi
3  120   Fukuoka        1997    Yukie
4  125   Okinawa        1982    Akari
'''
```
: however notice that the index is clunky and inconsistent

to fix that
```python
concat = pd.concat([df1, df3], ignore_index=True)
print(concat)


'''
     id      city  birth_year     name
0     0     Tokyo        1990  Hiroshi
1     1     Osaka        1989    Akiko
2     2     Kyoto        1992     Yuki
3     3  Hokkaido        1997   Satoru
4     4     Tokyo        1982   Steeve
5     6     Tokyo        1991   Mituru
6     8     Osaka        1988      Aoi
7    11     Kyoto        1990    Tarou
8    12  Hokkaido        1995   Suguru
9    13     Tokyo        1981   Mitsuo
10  117     Chiba        1990   Suguru
11  118  Kanagawa        1989  Kouichi
12  119     Tokyo        1992  Satochi
13  120   Fukuoka        1997    Yukie
14  125   Okinawa        1982    Akari
```
: we can also sort the column alphabetically

```python
concat = pd.concat([df1, df3], ignore_index=True, sort= True)
print(concat)
```