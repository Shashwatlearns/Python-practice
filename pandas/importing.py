import pandas as pd

df = pd.read_csv("Pokemon.csv")
df1 = pd.read_json("Pokemon.json")
print(df.to_string())
print(df1.to_string())