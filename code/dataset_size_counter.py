# New
# Author: DAI Xin
# This python code calculate the total number of instances, i.e. m.


import os
import csv
import json

# Count the total number of rows in all CSV files
def count_rows_in_csv(directory):
    total_rows = 0
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                rows = sum(1 for row in reader)  # Count rows
                rows -= 1  # Exclude the header
                total_rows += rows
                print(f"{file_name}: {rows} rows")
    return total_rows

# Count the total number of statements in the JSON file
def count_statements_in_json(json_file):
    total_statements = 0
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # The statements are stored in the inner lists of the values of the dictionary
        # Separated by comma
        for key, value in data.items():
            if isinstance(value, list) and len(value) > 0 and isinstance(value[0], list):
                statements = len(value[0])
                total_statements += statements
                print(f"{key}: {statements} statements")
    return total_statements

# Count the total number of columns in all CSV files
def count_columns_in_csv(directory):
    total_columns = 0
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as csv_file:
                first_line = csv_file.readline().strip()  # Read the first row
                columns = first_line.split("#")  # Split the row by '#' to identify columns
                num_columns = len(columns)  # Count the columns
                total_columns += num_columns
                print(f"{file_name}: {num_columns} columns")
    return total_columns

# Paths to access the data
csv_directory = "../data/all_csv"
json_file_path_1 = "../collected_data/r1_training_all.json"
json_file_path_2 = "../collected_data/r2_training_all.json"

# Calculations of rows, statements
print("Counting rows in CSV files...")
total_csv_rows = count_rows_in_csv(csv_directory)

print("Counting statements in JSON file...")
json_statements_1 = count_statements_in_json(json_file_path_1)
json_statements_2 = count_statements_in_json(json_file_path_2)
total_json_statements = json_statements_1 + json_statements_2

# Calculations of columns
print("Counting columns in CSV files...")
total_columns = count_columns_in_csv(csv_directory)

# Calculations of rows, statements, columns
print()
print(f"Total rows in CSV files: {total_csv_rows}")
print(f"Total statements in JSON file: {total_json_statements}")
print(f"Total columns across all CSV files: {total_columns}")

print()
print(f"m: Grand Total of Instances (rows + statements): {total_csv_rows + total_json_statements}")
print(f"d: Toal features (columns) across all CSV files: {total_columns}")

# Final result of datasize
print(f"m * d = {(total_csv_rows + total_json_statements) * total_columns}")