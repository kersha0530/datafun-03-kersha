import pandas as pd
import os

# Ensure the output folder exists
output_folder = "data_processed"
os.makedirs(output_folder, exist_ok=True)

# Load the mtcars.csv file
input_file = "mtcars.csv"  
data = pd.read_csv(input_file)

# Calculate the average miles per gallon (mpg)
average_mpg = data["mpg"].mean()

# Save the result in the data_processed folder
output_file = f"{output_folder}/processed_mtcars.csv"
result = pd.DataFrame({"Metric": ["Average MPG"], "Value": [average_mpg]})
result.to_csv(output_file, index=False)

print(f"Processed data saved in {output_file}")

