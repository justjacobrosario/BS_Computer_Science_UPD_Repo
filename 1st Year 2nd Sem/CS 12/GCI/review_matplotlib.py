# Core libraries
import numpy as np
import pandas as pd


# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

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

pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df = pd.read_csv("day.csv")


plt.figure(figsize=(6,4))
plt.scatter(df["temp"], df["cnt"])

plt.title("気温とレンタル数の関係")
plt.xlabel("気温")
plt.ylabel("レンタル数")

plt.show()