import csv

def read_csv_and_store_structured_data(file_path):
    structured_data = []
    
    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        
        for row in csv_reader:
            # Convert string values to appropriate data types if needed
            row['rank'] = int(row['rank'])
            row['line_num'] = int(row['line_num'])
            row['MLP-FL'] = float(row['MLP-FL'])
            row['buggy'] = bool(int(row['buggy']))  # Assuming 'buggy' is represented as 0 or 1
            
            structured_data.append(row)
    
    return structured_data

# Example usage:
file_path = 'd:\github_projects\Peters_Python_Playground\OITM-2023\cgpt_sample.csv'
data = read_csv_and_store_structured_data(file_path)

# Accessing the structured data
for row in data:
    print(row['rank'], row['line_num'], row['MLP-FL'], row['buggy'])
