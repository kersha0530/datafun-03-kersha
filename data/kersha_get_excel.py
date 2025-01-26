import sys
import os
import pandas as pd

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("\n".join(sys.path))  # Debugger: Print all paths Python searches for modules


from utils_logger import logger  # Import the logger for detailed logging


def fetch_and_save_excel(url="https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"):
    """
    Fetches the mtcars.csv dataset from a URL, saves it as an Excel file, and logs key actions.

    Args:
        url (str): The URL to fetch the dataset from.

    Returns:
        None
    """
    # Paths setup
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "example_data")
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Ensured the output folder exists at {output_folder}.")
    output_file = os.path.join(output_folder, "mtcars.xlsx")
    logger.info(f"Output file path set to {output_file}.")

    try:
        # Fetch the dataset
        logger.info(f"Attempting to fetch dataset from {url}.")
        data = pd.read_csv(url)
        if data.empty:
            logger.warning("Fetched dataset is empty. Exiting script.")
            return
        logger.info("Dataset fetched successfully.")

        # Save as Excel
        data.to_excel(output_file, index=False, sheet_name="MTCars")
        logger.info(f"Excel file created and saved successfully at {output_file}.")

        # Log basic metrics about the dataset
        log_excel_metrics(data)
    except Exception as e:
        logger.error(f"Failed to fetch or save Excel file: {e}", exc_info=True)


def log_excel_metrics(data):
    """
    Logs basic metrics for the dataset saved as an Excel file.

    Args:
        data (pd.DataFrame): The dataset to calculate metrics for.

    Returns:
        None
    """
    try:
        # Check if the dataset is empty
        if data.empty:
            logger.warning("Cannot log metrics for an empty dataset.")
            return

        # Basic metrics
        row_count = len(data)
        column_count = len(data.columns)
        numeric_summaries = data.describe().to_dict()

        logger.info(f"Excel Metrics:")
        logger.info(f"-----------------------")
        logger.info(f"Total Rows: {row_count}")
        logger.info(f"Total Columns: {column_count}")
        logger.info(f"Numeric Summaries: {numeric_summaries}")

        # Display metrics in the console
        print("\nExcel File Metrics:")
        print("-----------------------")
        print(f"Total Rows: {row_count}")
        print(f"Total Columns: {column_count}")
        print("Numeric Summaries:")
        for column, stats in numeric_summaries.items():
            print(f"  {column}: {stats}")
    except Exception as e:
        logger.error(f"An error occurred while logging metrics: {e}", exc_info=True)


if __name__ == "__main__":
    logger.info("Starting fetch_and_save_excel script.")
    try:
        fetch_and_save_excel()
        logger.info("fetch_and_save_excel script completed successfully.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)





