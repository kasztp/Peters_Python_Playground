import pandas as pd
import numpy as np


def load_data(path: str) -> pd.DataFrame:
    """Load the data from the given path into a Pandas Dataframe."""
    with open(path, 'r') as f:
        data = [[item.strip() for item in line.split(',')] for line in f.readlines()]
    data = pd.DataFrame(data)
    return data


def get_data_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate correlation between the columns of the given data.
    Return a Pandas DataFrame containing the correlation coefficients.
    
    :param data: PandasDataFrame - the data
    :return: PandasDataFrame - the correlation coefficients
    """
    return data.corr()


def get_most_correlated_columns(data: pd.DataFrame) -> tuple:
    """Find the two most correlated columns in the given data.
    Return a tuple of the two column names.
    
    :param data: PandasDataFrame - the data
    :return: tuple - the two most correlated column names
    """
    corr = get_data_statistics(data)
    max_corr = 0
    max_corr_col1 = None
    max_corr_col2 = None
    for col1 in corr.columns:
        for col2 in corr.columns:
            if col1 == col2:
                continue
            if corr[col1][col2] > max_corr:
                max_corr = corr[col1][col2]
                max_corr_col1 = col1
                max_corr_col2 = col2
    return max_corr_col1, max_corr_col2


def get_most_correlated_columns_to(data: pd.DataFrame, column: str):
    """Find the most correlated columns to the given column in the given data.
    Return the name of the most correlated columns in a descending order with coefficents.
    
    :param data: PandasDataFrame - the data
    :param column: str - the column name
    :return: dict - the most correlated columns name in descending order with coefficients
    """
    corr = get_data_statistics(data)
    corr = corr.sort_values(by=column, ascending=False)
    return corr[column]


if __name__ == "__main__":
    all_data = pd.DataFrame()
    for i in range(1, 4):
        data = load_data(f"bolt{i}.csv")
        all_data = all_data.append(data)
    

        # One-hot encode the data
        one_hot = pd.get_dummies(data.stack()).sum(level=0)

        # Calculate the correlation matrix
        #corr_matrix = one_hot.corr()

        # calculate confidence matrix
        corr_matrix = one_hot.corr(method='kendall')

        print(corr_matrix)

        # Create a DataFrame from the correlation matrix
        corr_df = corr_matrix.stack().reset_index()

        # Rename the columns
        corr_df.columns = ['Item1', 'Item2', 'Correlation']

        # Remove self-correlation entries
        corr_df = corr_df[corr_df['Item1'] != corr_df['Item2']]

        # Remove duplicate entries
        corr_df['Ordered_Items'] = corr_df.apply(lambda x: tuple(sorted([x['Item1'], x['Item2']])), axis=1)
        corr_df = corr_df.drop_duplicates(subset='Ordered_Items')

        # Drop the Ordered_Items column
        corr_df = corr_df.drop(columns='Ordered_Items')

        # Sort by correlation
        corr_df = corr_df.sort_values(by='Correlation', ascending=False)
        print(f"Bolt {i}")
        print(corr_df)
        print("A legkorreláltabb elemek:")
        print(corr_df.head(10))
    # One-hot encode the data
    one_hot = pd.get_dummies(all_data.stack()).sum(level=0)

    # Calculate the correlation matrix
    #corr_matrix = one_hot.corr()

    # calculate confidence matrix
    corr_matrix = one_hot.corr(method='kendall')
    print(corr_matrix)


    # Create a DataFrame from the correlation matrix
    corr_df = corr_matrix.stack().reset_index()

    # Rename the columns
    corr_df.columns = ['Item1', 'Item2', 'Correlation']

    # Remove self-correlation entries
    corr_df = corr_df[corr_df['Item1'] != corr_df['Item2']]

    # Remove duplicate entries
    corr_df['Ordered_Items'] = corr_df.apply(lambda x: tuple(sorted([x['Item1'], x['Item2']])), axis=1)
    corr_df = corr_df.drop_duplicates(subset='Ordered_Items')

    # Drop the Ordered_Items column
    corr_df = corr_df.drop(columns='Ordered_Items')

    # Sort by correlation
    corr_df = corr_df.sort_values(by='Correlation', ascending=False)
    print(f"Összes Bolt")
    print(corr_df)
    print("A legkorreláltabb elemek:")
    print(corr_df.head(10))