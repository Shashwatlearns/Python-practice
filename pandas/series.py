import pandas as pd

# Initializing data and series
data = [100, 102, 104, 2000, 0, 223, 500]
series = pd.Series(data, index=["a", "b", "c", "d", "e", "f", "g"])

# Printing initial series and accessing by label
print(series)
print(series.loc["a"])

# Modifying a value using label-based indexing
series.loc["a"] = 400

# Accessing by position and printing updated series
print(series.iloc[0])
print(series)

# Filtering and inspecting index
print(series[series >= 200])
print(series.index)

# Creating a series from a dictionary
calories = {
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700
}
series1 = pd.Series(calories)

# Printing dictionary-based series
print(series1)
print(series1["Day 1"])

# Updating value and filtering
series1.loc["Day 3"] += 3000
print(series1)
print(series1[series1 >= 2000])
