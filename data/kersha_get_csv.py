import sys
import os
import requests
import pandas as pd

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("\n".join(sys.path))  # Debugger: Print all paths Python searches for modules

from utils_logger import logger  # Import the logger


def fetch_csv(url="https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"):
    """
    Fetches the mtcars.csv dataset from a URL, saves it to the example_data folder, and logs basic metrics.

    Args:
        url (str): URL of the dataset to fetch.

    Returns:
        None
    """
    # Paths setup
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_dir, "example_data")
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Ensured the output folder exists at {output_folder}.")

    output_file = os.path.join(output_folder, "mtcars.csv")
    logger.info(f"Output file path set to {output_file}.")

    # Fetch the CSV file
    try:
        logger.info(f"Attempting to fetch CSV file from {url}.")
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_file, "wb") as file:
                file.write(response.content)
            logger.info(f"CSV file fetched and saved successfully as {output_file}.")

            # Analyze and log metrics for the fetched CSV file
            analyze_csv(output_file)
        else:
            logger.error(f"Failed to fetch CSV file. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while fetching the CSV file: {e}", exc_info=True)


def analyze_csv(file_path):
    """
    Analyzes the fetched CSV file and logs basic metrics.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        None
    """
    try:
        # Load CSV into a Pandas DataFrame
        data = pd.read_csv(file_path)

        # Check for empty dataset
        if data.empty:
            logger.warning("The dataset is empty. Analysis cannot proceed.")
            return

        # Metrics
        file_size = os.path.getsize(file_path) / 1024  # File size in KB
        row_count = len(data)
        column_count = len(data.columns)
        column_names = data.columns.tolist()
        missing_values = data.isnull().sum().to_dict()
        numeric_stats = data.describe().to_dict()

        # Log metrics
        logger.info("CSV Metrics:")
        logger.info("-----------------------")
        logger.info(f"File Size: {file_size:.2f} KB")
        logger.info(f"Total Rows: {row_count}")
        logger.info(f"Total Columns: {column_count}")
        logger.info(f"Column Names: {column_names}")
        logger.info(f"Missing Values: {missing_values}")
        logger.info(f"Descriptive Statistics: {numeric_stats}")

        # Print metrics to the console
        print("\nCSV File Metrics:")
        print("-----------------------")
        print(f"File Size: {file_size:.2f} KB")
        print(f"Total Rows: {row_count}")
        print(f"Total Columns: {column_count}")
        print(f"Column Names: {column_names}")
        print(f"Missing Values: {missing_values}")
        print("Descriptive Statistics:")
        for column, stats in numeric_stats.items():
            print(f"  {column}: {stats}")
    except Exception as e:
        logger.error(f"An error occurred while analyzing the CSV file: {e}", exc_info=True)


if __name__ == "__main__":
    logger.info("Starting fetch_csv script.")
    try:
        fetch_csv()
        logger.info("fetch_csv script completed successfully.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)





