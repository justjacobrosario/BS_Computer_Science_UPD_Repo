'''import numpy as np

a = np.array([1, 5, 10, 3, 4, 25, 30])

def homework(a):
    is_multipleof5 = (a%5 == 0)
    has_rem1 = (a%2 == 1)
    res = a[is_multipleof5 & has_rem1]

    return res


print(homework(a))

URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"

raw = np.loadtxt(URL, delimiter=",", usecols=[6,7,8], skiprows=1)

week_one_tmax = raw[0:7, 0]
week_one_tmin = raw[0:7, 1]
week_one_prcp = raw[0:7, 2]
week_two_tmax = raw[7:14, 0]


week_one_tmax = week_one_tmax / 10
week_one_tmin = week_one_tmin / 10
week_one_prcp = week_one_prcp / 10
week_two_tmax = week_two_tmax / 10

week_one_temp_range = week_one_tmax - week_one_tmin
'''


print("hi")