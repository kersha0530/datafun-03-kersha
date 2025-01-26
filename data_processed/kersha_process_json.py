
"""
Processes a JSON file containing car data and generates various metrics about the data.

The function reads a JSON file containing car data, converts it to a Pandas DataFrame, and calculates the following metrics:
- Average MPG
- Median weight
- Maximum horsepower
- Count of manual and automatic transmissions

The calculated metrics are then saved to a new JSON file in the "data_processed" directory.

Args:
    None

Returns:
    None
"""
import json
import os
import pandas as pd


def process_json():
    # Input and output paths
    input_file = "example_data/mtcars.json"
    output_folder = "data_processed"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "processed_mtcars.json")

    try:
        # Load the JSON data
        with open(input_file, "r") as file:
            data_json = json.load(file)

        # Convert JSON to a DataFrame for processing
        data = pd.DataFrame(data_json)

        # Metrics
        average_mpg = data["mpg"].mean()  # Average MPG
        median_weight = data["wt"].median()  # Median weight
        max_hp = data["hp"].max()  # Maximum horsepower

        # Transmission counts
        transmission_counts = data["am"].value_counts().to_dict()  # Count of transmission types
        manual_transmission = transmission_counts.get(1, 0)  # Manual (1)
        automatic_transmission = transmission_counts.get(0, 0)  # Automatic (0)

        # Save all metrics
        # Convert to JSON-serializable types
        processed_data = [
            {"Metric": "Average MPG", "Value": float(average_mpg)},
            {"Metric": "Median Weight", "Value": float(median_weight)},
            {"Metric": "Max Horsepower", "Value": int(max_hp)},
            {"Metric": "Manual Transmission Count", "Value": int(manual_transmission)},
            {"Metric": "Automatic Transmission Count", "Value": int(automatic_transmission)},
        ]

        # Save the results to a JSON file
        with open(output_file, "w") as file:
            json.dump(processed_data, file, indent=4)

        print(f"Processed data saved successfully at {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_json()



