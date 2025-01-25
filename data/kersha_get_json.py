import pandas as pd
import os
import json
from utils_logger import logger  # Import the logger for detailed logging

def convert_csv_to_json():
    """
    This script converts a CSV file to a JSON file and saves it to the 'example_data' folder.
    Logs key steps and provides optional metrics about the conversion process.
    """
    # Input and output paths
    input_file = "mtcars.csv"  # Ensure this file exists in your current directory
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
    logger.info(f"Ensured the output folder exists at {output_folder}.")
    output_file = os.path.join(output_folder, "mtcars.json")
    logger.info(f"Output file path set to {output_file}.")

    # Read the CSV and convert to JSON
    try:
        logger.info(f"Attempting to read CSV file from {input_file}.")
        data = pd.read_csv(input_file)
        logger.info("CSV file read successfully.")

        # Convert DataFrame to JSON format
        logger.info("Converting CSV data to JSON format.")
        data_json = data.to_dict(orient="records")

        # Save JSON to the output folder
        with open(output_file, "w") as file:
            json.dump(data_json, file, indent=4)
        logger.info(f"JSON file created successfully at {output_file}.")

        # Optional: Log basic metrics about the data
        log_json_metrics(data)
    except FileNotFoundError:
        logger.error(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

def log_json_metrics(data):
    """
    Logs metrics about the converted data.

    Args:
        data (pd.DataFrame): The DataFrame representing the CSV data.

    Returns:
        None
    """
    try:
        # Calculate basic metrics
        row_count = len(data)
        column_count = len(data.columns)
        numeric_summaries = data.describe().to_dict()

        # Log metrics
        logger.info("JSON Conversion Metrics:")
        logger.info("-----------------------")
        logger.info(f"Total Rows: {row_count}")
        logger.info(f"Total Columns: {column_count}")
        logger.info(f"Numeric Summaries: {numeric_summaries}")

        # Optional: Print metrics to the console
        print("\nJSON Conversion Metrics:")
        print("-----------------------")
        print(f"Total Rows: {row_count}")
        print(f"Total Columns: {column_count}")
        print("Numeric Summaries:")
        for column, stats in numeric_summaries.items():
            print(f"  {column}: {stats}")
    except Exception as e:
        logger.error(f"An error occurred while logging JSON metrics: {e}")

if __name__ == "__main__":
    logger.info("Starting convert_csv_to_json script.")
    convert_csv_to_json()
    logger.info("convert_csv_to_json script completed.")


