from itertools import chain
import pandas as pd

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(len(alphabet))

table = {}

for i, character in enumerate(alphabet):
    table[character] = chain.from_iterable([[character+str(x)]*(26-i)+[None]*i for x in range(1, 27)])

alphabet_df2 = pd.DataFrame(table)

models_df = pd.DataFrame({
    'A': ['A1', 'A1', 'A1', 'A2', 'A2'],
    'B': ['B1', 'B1', None, 'B2', None],
    'C': ['C1', None, None, None, None],
    'model_key': ['A=1_B=1_C=1', 'A=1_B=1', 'A=1', 'A=2_B=2', 'A=2'],
    'train_size': [200, 400, 600, 300, 500],
})


def export_data(df, filename):
    df.to_csv(filename, index=False)


print(models_df, '\n', alphabet_df2)

#export_data(alphabet_df2, 'test.csv')