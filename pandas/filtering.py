import pandas as pd

df = pd.read_csv("Pokemon.csv")

tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"] == 1]
water_pokemon = df[(df["Type1"] == "Water") |
                   (df["Type2"] == "Water")]
ff_pokemon = df[(df["Type1"] == "Fire") &
                 (df["Type2"] == "Flying")]
print(tall_pokemon, end="\n\n\n\n")
print(heavy_pokemon, end="\n\n\n\n")
print(legendary_pokemon, end="\n\n\n\n")
print(water_pokemon, end="\n\n\n\n")
print(ff_pokemon, end="\n\n\n\n")