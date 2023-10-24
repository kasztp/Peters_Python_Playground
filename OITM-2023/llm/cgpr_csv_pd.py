import pandas as pd

def read_csv_file(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, sep=';')

        # Ensure the DataFrame has the expected columns
        expected_columns = ["rank", "line_num", "MLP-FL", "buggy"]
        if not all(col in df.columns for col in expected_columns):
            raise ValueError("CSV file doesn't have the expected columns.")

        return df
    except Exception as e:
        # Handle errors appropriately (e.g., log the error)
        print(f"Error reading CSV file: {e}")
        return None

# Example usage:
file_path = "d:\github_projects\Peters_Python_Playground\OITM-2023\cgpt_sample.csv"
data_frame = read_csv_file(file_path)
if data_frame is not None:
    print(data_frame.head())  # Print the first few rows of the DataFrame
