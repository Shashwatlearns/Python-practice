import pandas as pd

df = pd.read_csv("Pokemon.csv")

#Dropping columns
# df = df.drop(columns=["Legendary", "No"])


#handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2": "None"})


#Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIREEE",
#                                    "Water" : "PANII"})


#standerdize text
# df["Name"] = df ["Name"].str.lower()


#fix data types
# df["Legendary"] = df["Legendary"].astype("bool")

#removing duplicates
df = df.drop_duplicates()

print(df.to_string())


