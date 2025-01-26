import sys
import os
import pandas as pd

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("\n".join(sys.path))  # Debugger: Print all paths Python searches for modules


from utils_logger import logger  # Import the logger for detailed logging


def save_mtcars_as_text():
    """
    Fetches or generates a text file and saves it to the "example_data" folder.
    Also calculates and displays metrics for the saved text file.
    """
    # Paths setup
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "example_data", "mtcars.csv")  # Path to the CSV file
    output_folder = os.path.join(script_dir, "example_data")
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
    logger.info(f"Ensured the output folder exists at {output_folder}.")
    output_file = os.path.join(output_folder, "mtcars.txt")  # Output text file
    logger.info(f"Output file path set to {output_file}.")

    if not os.path.exists(input_file):
        logger.warning(f"The file {input_file} does not exist.")
        return

    try:
        # Read the CSV file
        logger.info(f"Attempting to read CSV file from {input_file}.")
        data = pd.read_csv(input_file)
        logger.info("CSV file read successfully.")

        # Save as a text file
        with open(output_file, "w") as file:
            file.write(data.to_string(index=False))
        logger.info(f"Text file saved successfully at {output_file}.")

        # Calculate and display text metrics
        calculate_text_metrics(output_file)
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)


def calculate_text_metrics(file_path):
    """
    This script calculates and logs metrics for a given text file.

    Args:
        file_path (str): Path to the text file.
    """
    try:
        # Read the text file
        with open(file_path, "r") as file:
            content = file.readlines()

        # Calculate metrics
        total_lines = len(content)
        total_words = sum(len(line.split()) for line in content)
        total_characters = sum(len(line) for line in content)

        # Log and display the metrics
        logger.info(f"Processed Text Metrics for {file_path}:")
        logger.info(f"-----------------------")
        logger.info(f"Total Lines: {total_lines}")
        logger.info(f"Total Words: {total_words}")
        logger.info(f"Total Characters: {total_characters}")

        print("\nProcessed Text Metrics:")
        print("-----------------------")
        print(f"Total Lines: {total_lines}")
        print(f"Total Words: {total_words}")
        print(f"Total Characters: {total_characters}")
    except Exception as e:
        logger.error(f"An error occurred while processing the text file: {e}", exc_info=True)


if __name__ == "__main__":
    logger.info("Starting save_mtcars_as_text script.")
    try:
        save_mtcars_as_text()
        logger.info("save_mtcars_as_text script completed successfully.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
