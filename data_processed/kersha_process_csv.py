import pandas as pd
import os
import requests


def process_csv():
    # Input and output file paths
    input_file = "example_data/mtcars.csv"
    output_folder = "data_processed"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
    output_file = os.path.join(output_folder, "processed_mtcars.csv")

    try:
        # Read the CSV file
        data = pd.read_csv(input_file)

        # Example Metric: Calculate the average MPG
        average_mpg = data["mpg"].mean()

        # Save the processed data
        result = pd.DataFrame({
            "Metric": ["Average MPG"],
            "Value": [average_mpg]
        })
        result.to_csv(output_file, index=False)
        print(f"Processed CSV file saved successfully at {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_csv()


