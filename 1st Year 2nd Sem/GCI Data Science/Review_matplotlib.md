---
subject: GCI
field: programming
subfield: data science
---

> let's use a bike sharing dataset to further understand matplotlib

## 1. Bike Sharing dataset  example
: rental counts depend on
1. weather\
2. temp
3. season
4. working day vs weekend
5. other  environ. factors

: goal: what factors influence daily bike rentals the most

## 2. Loading and Comprehending the Data

### 2.1. Import Library

in terminal:
`pip install matplotlib`
`pip install seaborn`

```python
# Core libraries
import numpy as np
import pandas as pd


# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
%matplotlib inline
```

`import matplotlib.pyplot as plt`
: for plotting functions in `pyplot`

`%matplotlib inline`
: jupyter notebook command

#### 2.1.1. Seaborn
: under Matplotlib
: improves styles and functions for statistical visualization

### 2.2. Downloading the Dataset

```python
import requests
import zipfile
import io

# URL of the dataset
url = "https://cdn.uci-ics-mlr-prod.aws.uci.edu/275/bike%2Bsharing%2Bdataset.zip"

# Download the file
response = requests.get(url)

# Extract the zip file
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    z.extractall()

print("Dataset downloaded and extracted successfully.")
```
: this will download day.csv and hour.csv

### 2.3. Inspecting the Dataset

: to tabularize the data, use pandas
```python
pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 5)

df = pd.read_csv("day.csv")
print(df.head())

'''
     instant      dteday  season  yr  mnth  holiday  weekday  workingday  weathersit      temp     atemp       hum  windspeed  casual  registered   cnt
0          1  2011-01-01       1   0     1        0        6           0           2  0.344167  0.363625  0.805833   0.160446     331         654   985
1          2  2011-01-02       1   0     1        0        0           0           2  0.363478  0.353739  0.696087   0.248539     131         670   801
..       ...         ...     ...  ..   ...      ...      ...         ...         ...       ...       ...       ...        ...     ...         ...   ...
729      730  2012-12-30       1   1    12        0        0           0           1  0.255833  0.231700  0.483333   0.350754     364        1432  1796
730      731  2012-12-31       1   1    12        0        1           1           2  0.215833  0.223487  0.577500   0.154846     439        2290  2729

[731 rows x 16 columns]
'''
```

#### 2.3.1. Structural Inspection
: before visualizing trends and patterns, inspect the structure of the data set first (the shape, column types, etc.)

```python
print("Shape: ", df.shape)
print(df.info())

'''
Shape:  (731, 16)
<class 'pandas.DataFrame'>
RangeIndex: 731 entries, 0 to 730
Data columns (total 16 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   instant     731 non-null    int64  
 1   dteday      731 non-null    str    
 2   season      731 non-null    int64  
 3   yr          731 non-null    int64  
 4   mnth        731 non-null    int64  
 5   holiday     731 non-null    int64  
 6   weekday     731 non-null    int64  
 7   workingday  731 non-null    int64  
 8   weathersit  731 non-null    int64  
 9   temp        731 non-null    float64
 10  atemp       731 non-null    float64
 11  hum         731 non-null    float64
 12  windspeed   731 non-null    float64
 13  casual      731 non-null    int64  
 14  registered  731 non-null    int64  
 15  cnt         731 non-null    int64  
dtypes: float64(4), int64(11), str(1)
memory usage: 91.5 KB
'''
```

: Important info from `df.shape` and `df.info()`
1. Dataset Size:  
: 731 daily observations (rows), 16 variables (columns)
2. Missing Values: 
: since no `null` values, (all 731 non-nulls), there are NO missing vals
: since there is no missing values, no need for data cleaning, proceed to analysis
3. Variable Types: 
int64, float64, object (str)
4. Key Variable of Interest:
: variable to be observed for all other variables 
(i.e. the `cnt`; total daily rentals)

##