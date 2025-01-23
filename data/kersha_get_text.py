"""
Fetches or generates a text file and saves it to the "example_data" folder.

The function creates a sample text file if no URL is provided or fetches a file from the web.
The saved file can then be used for processing with `kersha_process_text.py`.

Args:
    None

Returns:
    None
"""
import pandas as pd
import os

def save_mtcars_as_text():
    # Input and output paths
    input_file = "example_data/mtcars.csv"  # Path to the CSV file
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
    output_file = os.path.join(output_folder, "mtcars.txt")  # Output text file

    try:
        # Read the CSV file
        data = pd.read_csv(input_file)

        # Save as a text file
        with open(output_file, "w") as file:
            file.write(data.to_string(index=False))
        
        print(f"Text file saved successfully at {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    save_mtcars_as_text()



