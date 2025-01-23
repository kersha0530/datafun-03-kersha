import json
import pandas as pd

# Read JSON
json_file = 'fetch_scripts/data.json'  # Replace with your actual JSON file path
with open(json_file, 'r') as file:
    data = json.load(file)

# Example Metric: Count the number of keys
key_count = len(data)

# Save Result
result = pd.DataFrame({'Metric': ['Key Count'], 'Value': [key_count]})
result.to_json('data_processed/processed_json.json', orient='records')

print("JSON file processed and saved in data_processed/processed_json.json")
