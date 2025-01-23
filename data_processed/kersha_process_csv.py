import pandas as pd

# Read CSV
csv_file = 'fetch_scripts/data.csv'  # Replace with your actual CSV file path
data = pd.read_csv(csv_file)

# Example Metric: Calculate the average of a numeric column
average_value = data['numeric_column'].mean()

# Save Result
result = pd.DataFrame({'Metric': ['Average'], 'Value': [average_value]})
result.to_csv('data_processed/processed_csv.csv', index=False)

print("CSV file processed and saved in data_processed/processed_csv.csv")
