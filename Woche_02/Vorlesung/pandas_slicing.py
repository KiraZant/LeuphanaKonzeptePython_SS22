"""
This code demonstrates side effects of Pandas methods and slicing operators
"""
import pandas as pd

# Load and display data
eqs = pd.read_csv("earthquake.csv")
print(eqs.head())

# Built-in methods: do not modify original dataframe
eqs.dropna()
eqs.drop_duplicates()
eqs.replace(0, -1)

# Modifying columns
# eqs[eqs["Latitude"] >= 50]["Latitude"] = -50    # does not work and will cause a "SettingWithCopyWarning"
eqs.loc[eqs["Latitude"] >= 50, "Latitude"] = 1000.0     # sets all Latitude values >= 50 to 1000

# Working with slices of a DataFrame
slice = eqs.loc[:20, "Latitude"]    # changes on this slice may affect the original dataframe
slice = eqs.loc[eqs["Latitude"] >= 0, :]    # changes on this slice do not affect original dataframe
