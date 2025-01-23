import pandas as pd
import os

def process_excel():
    # Input and output file paths
    input_file = "example_data/mtcars.xlsx"
    output_folder = "data_processed"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
    output_file = os.path.join(output_folder, "processed_mtcars.xlsx")

    try:
        # Read the Excel file
        data = pd.read_excel(input_file, sheet_name="MTCars")

        # Example Metric: Calculate the average MPG
        average_mpg = data["mpg"].mean()

        # Save the processed data
        result = pd.DataFrame({
            "Metric": ["Average MPG"],
            "Value": [average_mpg]
        })
        result.to_excel(output_file, index=False, sheet_name="Processed Data")
        print(f"Processed Excel file saved successfully at {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_excel()




