import sys
import os
import json
import pandas as pd

# Add the root project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("\n".join(sys.path))  # Debug: Print all paths Python searches for modules


from utils_logger import logger  # Import the logger for detailed logging


def convert_csv_to_json():
    """
    Converts a CSV file to a JSON file containing specific metrics.
    Logs key steps and saves the metrics to the 'example_data' folder.
    """
    # Paths setup
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "example_data", "mtcars.csv")
    output_folder = os.path.join(script_dir, "example_data")
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Ensured the output folder exists at {output_folder}.")
    output_file = os.path.join(output_folder, "mtcars_metrics.json")
    logger.info(f"Output file path set to {output_file}.")

    # Check if the input file exists
    if not os.path.exists(input_file):
        logger.warning(f"The file {input_file} does not exist.")
        return

    try:
        # Read the CSV file
        logger.info(f"Attempting to read CSV file from {input_file}.")
        data = pd.read_csv(input_file)
        logger.info("CSV file read successfully.")

        # Validate required columns
        required_columns = {"mpg", "wt", "hp", "am"}
        if not required_columns.issubset(data.columns):
            logger.error(f"Missing required columns in {input_file}. Expected columns: {required_columns}")
            return

        # Calculate metrics
        logger.info("Calculating metrics for the dataset.")
        average_mpg = data["mpg"].mean()
        median_weight = data["wt"].median()
        max_hp = data["hp"].max()

        transmission_counts = data["am"].value_counts().to_dict()
        manual_transmission = transmission_counts.get(1, 0)  # Manual (1)
        automatic_transmission = transmission_counts.get(0, 0)  # Automatic (0)

        # Save metrics to a JSON structure
        result = pd.DataFrame({
            "Metric": [
                "Average MPG", 
                "Median Weight", 
                "Max Horsepower", 
                "Manual Transmission", 
                "Automatic Transmission"
            ],
            "Value": [
                average_mpg, 
                median_weight, 
                max_hp, 
                manual_transmission, 
                automatic_transmission
            ]
        }).to_dict(orient="records")

        # Save the results to a JSON file
        with open(output_file, "w") as file:
            json.dump(result, file, indent=4)
        logger.info(f"Metrics JSON file created successfully at {output_file}.")

        # Print metrics to the console
        print("\nMetrics Saved to JSON:")
        print("-----------------------")
        for metric in result:
            print(f"{metric['Metric']}: {metric['Value']}")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    logger.info("Starting kersha_get_json script.")
    try:
        convert_csv_to_json()
        logger.info("kersha_get_json script completed successfully.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)




