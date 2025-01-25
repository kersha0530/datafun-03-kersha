import pandas as pd
import os
from utils_logger import logger  # Import the logger to document detailed logging

def fetch_and_save_excel():
    """
    Fetches the mtcars.csv dataset from a URL, saves it as an Excel file, and logs key actions.
    """
    # URL for the mtcars.csv dataset
    url = "https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"
    
    # Output folder and file
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Ensured the output folder exists at {output_folder}.")
    output_file = os.path.join(output_folder, "mtcars.xlsx")
    logger.info(f"Output file path set to {output_file}.")

    try:
        # Fetch the dataset
        logger.info(f"Attempting to fetch dataset from {url}.")
        data = pd.read_csv(url)
        logger.info("Dataset fetched successfully.")

        # Save as Excel
        data.to_excel(output_file, index=False, sheet_name="MTCars")
        logger.info(f"Excel file created and saved successfully at {output_file}.")

        # Log basic metrics about the dataset
        log_excel_metrics(data)
    except Exception as e:
        logger.error(f"Failed to fetch or save Excel file: {e}")

def log_excel_metrics(data):
    """
    This script logs basic metrics for the dataset saved as an Excel file.

    Args:
        data (pd.DataFrame): The dataset to calculate metrics for.

    Returns:
        None
    """
    try:
        # Basic metrics
        row_count = len(data)
        column_count = len(data.columns)
        numeric_summaries = data.describe().to_dict()

        logger.info(f"Excel Metrics:")
        logger.info(f"-----------------------")
        logger.info(f"Total Rows: {row_count}")
        logger.info(f"Total Columns: {column_count}")
        logger.info(f"Numeric Summaries: {numeric_summaries}")

        # Optional: Display metrics in the console
        print("\nExcel File Metrics:")
        print("-----------------------")
        print(f"Total Rows: {row_count}")
        print(f"Total Columns: {column_count}")
        print("Numeric Summaries:")
        for column, stats in numeric_summaries.items():
            print(f"  {column}: {stats}")
    except Exception as e:
        logger.error(f"An error occurred while logging metrics: {e}")

if __name__ == "__main__":
    logger.info("Starting fetch_and_save_excel script.")
    fetch_and_save_excel()
    logger.info("fetch_and_save_excel script completed.")



