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
       index    ID
row 1    0      100
row 2    1      101
row 3    2      102
```

### 2) DataFrame
: 2-Dimension
: has rows and columns
```md
               column 1    column 2
       index    ID          NAME
row 1    0      100         Juan
row 2    1      101         Jacob
row 3    2      102         JJ
```

## 3. Data Extraction