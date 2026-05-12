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

#### 2.1.1. Seaborn
: under Matplotlib
: improves styles and functions for statistical visualization

