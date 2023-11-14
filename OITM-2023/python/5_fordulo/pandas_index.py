import pandas as pd

beers = [
    ["A", "B", "C"],
    ["import", "Heineken", 300],
    ["import", "Hoegaarden", 400],
    ["hazai", "Soproni", 300],
    ["hazai", "Borsodi", 400],
    ["import", "Budweiser", 500]
]

df = pd.DataFrame(beers[1:], columns=beers[0])
print(df)


o1 = df.loc[6:4,'B':'B']
o2 = df.loc[2:4,'B':'C']
o3 = df.loc[6:4,'B':'C']
o4 = df.loc[df['A'] == 'hazai', 'B': 'B']
#o5 = df.loc[df['A'] == 'hazai', 1:2]
#o6 = df.iloc[6:4,'B':'B']
o7 = df.iloc[2:4,1:2]
o8 = df.iloc[2:3,1:2]
#o9 = df.iloc[df['A']=='hazai', 1:2]

print(f"o1: {type(o1)}")
print(o1)
print(f"o2: {type(o2)}")
print(o2)
print(f"o3: {type(o3)}")
print(o3)
print(f"o4: {type(o4)}")
print(o4)
#print(f"o5: {type(o5)}")
#print(o5)
#print(f"o6: {type(o6)}")
#print(o6)
print(f"o7: {type(o7)}")
print(o7)
print(f"o8: {type(o8)}")
print(o8)
#print(f"o9: {type(o9)}")
#print(o9)
