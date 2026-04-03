import pandas as pd

df = pd.read_csv("Pokemon.csv", index_col="Name")

#selection by column
# print(df["Name"])
# print(df["Height"])
# print(df[["Name", "Height", "Weight"]].to_string())

#selection by rows
#print(df.loc[1])
print(df.loc["Pikachu"])
print(df.loc["Gengar", ["Height", "Weight"]])
print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
print(df.iloc[0:10:2,0:3])
