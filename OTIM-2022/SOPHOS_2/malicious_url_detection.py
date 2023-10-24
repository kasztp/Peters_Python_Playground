import os
import pandas as pd


path = os.getcwd() + "/OTIM-2022/SOPHOS_2/"


df = pd.read_csv(path + 'oitm_train_urls.csv')
print(df.head(20))


def count_tags(df, tag):
    """Count the number of times a tag appears in the dataset either alone or in combination with other tags"""
    return df['tags'].str.count(tag).sum()


print("Number of URLs sontaining 'emotet' malware: ", count_tags(df, 'emotet'))
