import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

series = Series(
	[2, 4, 6, 8, 10],
	index=['A', 'B', 'C', 'D', 'E']
	)

print(series.values)
