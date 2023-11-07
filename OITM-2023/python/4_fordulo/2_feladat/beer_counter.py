import os
import pandas as pd
from collections import Counter


def load_data():
    return pd.read_excel(os.path.join(os.getcwd(), 'questionnaire.xlsx'))


if __name__ == '__main__':
    beer_df = load_data()
    #print(beer_df.head())

    # get first row of the dataframe as string
    first_row = beer_df.iloc[0].to_string()
    print(first_row)
    first_row = first_row.lower().split(",")
    print(first_row)
    first_row = [x.strip() for x in first_row]
    print(first_row)

    # separate items starting with number to a new list
    beer_amounts = [x for x in first_row if x[0].isdigit()]
    print(beer_amounts)
    # split items containing multiple ; separated values
    beer_amounts = [x.split(";") for x in beer_amounts]
    # flatten the list
    beer_amounts = [item.strip() for sublist in beer_amounts for item in sublist]
    print(beer_amounts)
    beer_amounts = [item.split() for item in beer_amounts]
    print(beer_amounts)
    sum_of_all_beers = sum([int(x[0].strip(".")) for x in beer_amounts])
    print(sum_of_all_beers)
    beer_amounts = [[item[0], " ".join(item[1:])] for item in beer_amounts]
    print(beer_amounts)

    # get the beer names
    beer_names = [x for x in first_row if not x[0].isdigit()]
    
    # count beer names 
    beer_names = Counter(beer_names)
    print(beer_names)
    print(sum(beer_names.values()))

