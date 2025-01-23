import pandas as pd
import os
import json

def convert_csv_to_json():
    # Input and output paths
    input_file = "mtcars.csv"  # Ensure this file exists in your current directory
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "mtcars.json")

    # Read the CSV and convert to JSON
    try:
        data = pd.read_csv(input_file)
        data_json = data.to_dict(orient="records")  # Convert DataFrame to JSON format

        # Save JSON to the output folder
        with open(output_file, "w") as file:
            json.dump(data_json, file, indent=4)
        print(f"JSON file created successfully at {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert_csv_to_json()

