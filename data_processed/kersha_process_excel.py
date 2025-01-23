import pandas as pd

# Read Excel
excel_file = 'fetch_scripts/data.xlsx'  # Replace with your actual Excel file path
data = pd.read_excel(excel_file)

# Example Metric: Count the number of rows
row_count = len(data)

# Save Result
result = pd.DataFrame({'Metric': ['Row Count'], 'Value': [row_count]})
result.to_excel('data_processed/processed_excel.xlsx', index=False)

print("Excel file processed and saved in data_processed/processed_excel.xlsx")
