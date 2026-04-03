import pandas as pd

df = pd.read_csv("pokemon.csv")


#Whole dataframe
print(df.mean(numeric_only = True), end="\n\n\n\n")
print(df.sum(numeric_only = True), end="\n\n\n\n")
print(df.min(numeric_only = True), end="\n\n\n\n")
print(df.max(numeric_only = True), end="\n\n\n\n")
print(df.count(), end="\n\n\n\n")


#Single column
print(df["Height"].mean(), end="\n\n")
print(df["Height"].sum(), end="\n\n")
print(df["Height"].min(), end="\n\n")
print(df["Height"].max(), end="\n\n")
print(df["Height"].count(), end="\n\n")

#groupby
group = df.groupby("Type1")

print(group["Height"].mean(), end="\n\n")
print(group["Height"].sum(), end="\n\n")
print(group["Height"].min(), end="\n\n")
print(group["Height"].max(), end="\n\n")
print(group["Height"].count(), end="\n\n")


















