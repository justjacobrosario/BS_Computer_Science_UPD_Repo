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

print(anime_data_extracted)
#print(anime_data_extracted["Type"].unique())
#print(anime_data_extracted[(anime_data_extracted["Type"] == type)]["Score"].mean())

result = homework(anime_data_extracted)
print(result)

import ast
import inspect
import textwrap

def hw2_public_tests(homework_func):
    print("=== HW2 Public Tests ===")

    # Get the source code of the homework function
    source = textwrap.dedent(inspect.getsource(homework_func))
    tree = ast.parse(source)

    # ---------- Test 1: No import statements ----------
    print("Test 1: No import statements in function...", end=" ")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            print("NG")
            if isinstance(node, ast.Import):
                names = ", ".join(alias.name for alias in node.names)
            else:
                names = node.module
            print(f"  Found import statement: '{names}'")
            print("  Remove all import statements before submitting.")
            return
    print("OK")

    # ---------- Test 2: No data loading code ----------
    print("Test 2: No data loading code in function...", end=" ")
    blocked_calls = {"read_csv", "read_excel", "read_json", "read_html",
                     "get", "post", "ZipFile", "extractall", "urlopen"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func_name = ""
            if isinstance(node.func, ast.Attribute):
                func_name = node.func.attr
            elif isinstance(node.func, ast.Name):
                func_name = node.func.id
            if func_name in blocked_calls:
                print("NG")
                print(f"  Found data loading call: '{func_name}()'")
                print("  Do not include data downloading/loading code in your function.")
                return
    print("OK")

    # ---------- Test 3: No hardcoded file paths or URLs ----------
    print("Test 3: No hardcoded file paths or URLs...", end=" ")
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            val = node.value
            if val.startswith("http") or ".csv" in val or ".zip" in val:
                print("NG")
                print(f"  Found hardcoded path/URL: '{val[:60]}...'")
                print("  Do not include file paths or URLs in your function.")
                return
    print("OK")

    print("=== All Public Tests Passed ===")

hw2_public_tests(homework)