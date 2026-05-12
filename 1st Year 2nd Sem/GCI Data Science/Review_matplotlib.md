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
df = pd.read_csv("day.csv")
print(df.head())

'''
   instant      dteday  season  yr  ...  windspeed  casual  registered   cnt
0        1  2011-01-01       1   0  ...   0.160446     331         654   985
1        2  2011-01-02       1   0  ...   0.248539     131         670   801
2        3  2011-01-03       1   0  ...   0.248309     120        1229  1349
3        4  2011-01-04       1   0  ...   0.160296     108        1454  1562
4        5  2011-01-05       1   0  ...   0.186900      82        1518  1600

[5 rows x 16 columns]
'''
```