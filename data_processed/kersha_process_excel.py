import pandas as pd
import os

def process_excel():
    # Input and output file paths
    input_file = "example_data/mtcars.xlsx"
    output_folder = "data_processed"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "processed_mtcars.xlsx")
    
    # Read the Excel file
    data = pd.read_excel(input_file, sheet_name="MTCars")
    
    # Example Metric: Calculate the average MPG
    average_mpg = data["mpg"].mean()
    
    # Save the result as a new Excel file
    result = pd.DataFrame({"Metric": ["Average MPG"], "Value": [average_mpg]})
    result.to_excel(output_file, index=False, sheet_name="Processed Data")
    print(f"Processed data saved in {output_file}.")

if __name__ == "__main__":
    process_excel()



