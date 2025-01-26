import os

def process_text():
    # Input and output file paths
    input_file = "example_data/mtcars.txt"  # Correct the path if necessary
    output_folder = "data_processed"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists
    output_file = os.path.join(output_folder, "processed_sample.txt")

    try:
        # Read the input text file
        with open(input_file, "r") as file:
            content = file.readlines()

        # Example processing: Count lines, words, and characters
        total_lines = len(content)
        total_words = sum(len(line.split()) for line in content)
        total_characters = sum(len(line) for line in content)

        # Write the metrics to the output file
        with open(output_file, "w") as file:
            file.write(f"Processed Text Metrics:\n")
            file.write(f"-----------------------\n")
            file.write(f"Total Lines: {total_lines}\n")
            file.write(f"Total Words: {total_words}\n")
            file.write(f"Total Characters: {total_characters}\n")

        print(f"Processed text file saved successfully at {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    process_text()


