import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

Pokemon = input("Enter Pokemon Name: ")

try:
    print(df.loc[Pokemon])

except KeyError:
    print(f"{Pokemon} not in DataFrame")