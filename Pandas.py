import pandas as pd

#Data xolumns structure
data = [["Martin","Brokeš",23],
        ["Franta","Vomáčka",19],
        ["Jozef","Kukuricídus",50]]
col_names = ["Name","Surname","Age"]

df1 = pd.DataFrame(data,columns=col_names)
print(df1)

#Definition of DataFrame using a dictionary

data2 = {"Name":["Jakub","Karel","Jan"],
        "Surname":["Novak","Prochazka","Novotny"],
        "Age":[1,2,3]
        }

df2 = pd.DataFrame(data2)
print(df2)

#Index of a table

new_indices = list(range(1,4))
df2.index = new_indices
print(df2)

#Adding a new column

human_id = [f"ID{x}" for x in range(1,4)]
df2["id"] = human_id
df2.set_index("id",inplace=True)
print(df2)

#display first/last n columns of a table

print(df2.head())
print(df2.tail(2))
print(df2.info())
print(df2.describe())

# Access multiple columns

print(df2[["Name","Surname"]])

# Access data using locators

print(df2.loc[:,"Age"])
print(df2.iloc[:,[2,1]])

df2 = df2.reset_index(drop=True)
print(df2)

# Inserting rows using locators

df2.loc["3",:] = ["Martin","Brokeš",23]
print(df2)

#new types

df2["Age"] = df2["Age"].astype(int)
print(df2)

#concatenating and merging (as sql join)

df3 = pd.concat([df2,df2])
print(df3)
print(df3.nunique())

print(df2)
df4 = df2.merge(df2,on="Age",how="left")
print(df4)

