"""
Processes a text file containing car data or other structured data and generates metrics.

The function reads a plain text file, processes the data to extract meaningful information,
and calculates metrics such as word counts, line counts, and character counts.

The results are then saved to a new text file in the "data_processed" directory.

Args:
    None

Returns:
    None
"""
import os

def process_text():
    # Input and output paths
    input_file = "example_data/sample.txt"  # Adjust this path to your text file
    output_folder = "data_processed"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists
    output_file = os.path.join(output_folder, "processed_sample.txt")

    try:
        # Read the text file
        with open(input_file, "r") as file:
            lines = file.readlines()

        # Metrics
        line_count = len(lines)  # Total number of lines
        word_count = sum(len(line.split()) for line in lines)  # Total number of words
        char_count = sum(len(line) for line in lines)  # Total number of characters

        # Prepare the processed data
        processed_data = (
            f"Processed Text Metrics:\n"
            f"-----------------------\n"
            f"Total Lines: {line_count}\n"
            f"Total Words: {word_count}\n"
            f"Total Characters: {char_count}\n"
        )

        # Save the results to a text file
        with open(output_file, "w") as file:
            file.write(processed_data)

        print(f"Processed text file saved successfully at {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_text()

