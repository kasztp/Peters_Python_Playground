import re
import time
from statistics import mean, stdev
from typing import Callable, Final

import pandas as pd

# Constants
MIN_DESCRIPTION_LENGTH: Final[int] = 32
DESCRIPTION_COLUMN: Final[str] = 'obs_description'
CLEAN_PATTERN: Final = re.compile(r'\d+|[^\w\s]|\n')


def clean_text_data_pandas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans text data in the description column of a DataFrame.

    Removes digits, special characters, newlines, and converts text to lowercase.

    Args:
        df (pd.DataFrame): Input DataFrame containing text data to clean.

    Returns:
        pd.DataFrame: A new DataFrame with cleaned text in the description column.

    Notes:
        - This function creates a copy of the input DataFrame.
        - The cleaning process removes all digits, punctuation, special characters, and newlines.
        - All text is converted to lowercase.
        - Assumes that DESCRIPTION_COLUMN is defined in the global scope.
    """
    combined_pattern = r'\d+|[^\w\s]|\n'

    cleaned_df = df.copy()
    cleaned_df[DESCRIPTION_COLUMN] = (
        cleaned_df[DESCRIPTION_COLUMN]
        .str.replace(combined_pattern, '', regex=True)
        .str.lower()
    )
    return cleaned_df


def clean_text_data_re(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean text data in the description column using regex pattern substitution.

    This function creates a copy of the input DataFrame, then processes the 
    text in the description column by:
    1. Converting all text to lowercase
    2. Removing content that matches the CLEAN_PATTERN regex pattern

    Args:
        df (pd.DataFrame): Input DataFrame containing text data to clean

    Returns:
        pd.DataFrame: A new DataFrame with cleaned text in the description column
    """
    cleaned_df = df.copy()
    cleaned_df[DESCRIPTION_COLUMN] = cleaned_df[DESCRIPTION_COLUMN].apply(
        lambda x: CLEAN_PATTERN.sub('', x.lower())
    )
    return cleaned_df


def generate_test_data(n_rows: int) -> pd.DataFrame:
    """
    Generate a DataFrame with test text data containing various patterns.
    This function creates a pandas DataFrame with a single column 'obs_description'
    containing a mix of text patterns (including special characters, numbers, and newlines).
    The patterns cycle through a predefined set, with the row index appended to each entry.
    Args:
        n_rows (int): Number of rows to generate in the DataFrame
    Returns:
        pd.DataFrame: A DataFrame with a single column 'obs_description' containing test data
    Examples:
        >>> df = generate_test_data(3)
        >>> print(len(df))
        3
        >>> print(df['obs_description'][0])
        'Sample123 text! with\\n numbers456 0'
    """

    # Mix of different text patterns
    patterns = [
        "Sample123 text! with\n numbers456",
        "Complex@#$ data123 with\n\n multiple!!@ special chars",
        "Simple text only",
        "12345 Numbers only 67890",
        "Mix of everything123!@#$\n\n and more"
    ]

    return pd.DataFrame({
        'obs_description': [
            patterns[i % len(patterns)] + f" {i}"
            for i in range(n_rows)
        ]
    })


def benchmark_function(func: Callable, df: pd.DataFrame, num_runs: int = 5) -> tuple[float, float]:
    """
    Benchmarks the execution time of a given function over a specified number of runs.

    Args:
        func (Callable): The function to be benchmarked.
        df (pd.DataFrame): The DataFrame to be passed as an argument to the function.
        num_runs (int, optional): The number of times to run the function for benchmarking. Defaults to 5.

    Returns:
        tuple[float, float]: A tuple containing the mean and standard deviation of the execution times.
    """
    times = []

    for _ in range(num_runs):
        start = time.perf_counter()
        func(df)
        end = time.perf_counter()
        times.append(end - start)

    return mean(times), stdev(times)


def run_benchmarks():
    """
    Run benchmarks to compare the performance of two text cleaning functions on datasets of varying sizes.
    The function generates test data of different sizes, runs a warm-up to avoid first-run bias, and then benchmarks
    the performance of `clean_text_data_pandas` and `clean_text_data_re` functions. The results, including mean and 
    standard deviation of execution times, are collected and returned as a pandas DataFrame.
    Returns:
        pd.DataFrame: A DataFrame containing the benchmark results with columns:
            - 'size': The size of the dataset.
            - 'pandas_mean': The mean execution time for `clean_text_data_pandas`.
            - 'pandas_std': The standard deviation of execution time for `clean_text_data_pandas`.
            - 're_mean': The mean execution time for `clean_text_data_re`.
            - 're_std': The standard deviation of execution time for `clean_text_data_re`.
    """

    dataset_sizes = [1000, 10000, 100000]
    results = []

    for size in dataset_sizes:
        df = generate_test_data(size)

        # Warm up run (to avoid first-run bias)
        clean_text_data_pandas(df)
        clean_text_data_re(df)

        # Actual benchmarks
        pandas_mean, pandas_std = benchmark_function(clean_text_data_pandas, df, 10)
        re_mean, re_std = benchmark_function(clean_text_data_re, df, 10)

        results.append({
            'size': size,
            'pandas_mean': pandas_mean,
            'pandas_std': pandas_std,
            're_mean': re_mean,
            're_std': re_std
        })

    return pd.DataFrame(results)


# Run and display results
if __name__ == "__main__":
    print("Running benchmarks...")
    results = run_benchmarks()

    pd.set_option(
        'display.float_format',
        '{:.4f}'.format
    )
    print("\nResults (times in seconds):")
    print(results)

    # Calculate and display performance differences
    results['speedup'] = (results['pandas_mean'] / results['re_mean'] - 1) * 100
    print("\nPerformance improvement of re over pandas (%):")
    for _, row in results.iterrows():
        print(f"Dataset size {row['size']}: {row['speedup']:.1f}% faster")
