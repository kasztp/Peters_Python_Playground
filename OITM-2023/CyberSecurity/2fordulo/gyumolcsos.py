import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load the data from the given path into a Pandas DataFrame.
    Rename columns to the following:
    - 1st column: Alma
    - 2nd column: Banan
    - 3rd column: Citrom
    - 4th column: Dinnye
    - 5th column: Eper
    
    :param path: str - the path to the data file
    :return: PandasDataFrame - the data
    """
    data = pd.read_csv(path, header=None)
    data.rename(columns={0: 'Alma', 1: 'Banan', 2: 'Citrom', 3: 'Dinnye', 4: 'Eper'}, inplace=True)
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
    data = load_data("gyumolcsos.csv")
    print(get_most_correlated_columns(data))
    print(get_most_correlated_columns_to(data, 'Eper'))
