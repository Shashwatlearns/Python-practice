import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]
        }

df = pd.DataFrame(data, index=["Employee_1","Employee_2","Employee_3"])

#Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

#Add a new row
new_rows = pd.DataFrame([{"Name": "Sandy", "Age" : 28, "Job": "Engineer"},{"Name": "Eugene", "Age" : 60, "Job": "Manager"}], index=["Employee_4","Employee_5"])
df = pd.concat([df,new_rows])

print(df.loc["Employee_1"])
print(df)
print(df.iloc[1])