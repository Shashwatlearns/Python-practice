import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("Pokemon.csv")

type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index,type_count.values,color="pink",edgecolor="black")

plt.title("Pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()