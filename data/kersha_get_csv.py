import requests
import os
from utils_logger import logger  # Import the logger

def fetch_csv():
    """
    This script fetches the mtcars.csv dataset from a URL and saves it to the example_data folder.

    Logs the status of the fetch operation, including successes and errors.
    """
    # URL for the mtcars.csv dataset
    url = "https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"
    
    # Ensure the output folder exists
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Ensured the output folder exists at {output_folder}.")
    
    # Path to save the file
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
        else:
            logger.error(f"Failed to fetch CSV file. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while fetching the CSV file: {e}")

if __name__ == "__main__":
    logger.info("Starting fetch_csv script.")
    fetch_csv()
    logger.info("fetch_csv script completed.")



