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
import requests

def get_text_file():
    # Input: URL for text file or None to generate a sample
    url = None  # Example: "https://example.com/sample.txt"

    # Output path
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "sample.txt")

    try:
        if url:
            # Fetch text file from the URL
            response = requests.get(url)
            if response.status_code == 200:
                with open(output_file, "w") as file:
                    file.write(response.text)
                print(f"Text file fetched successfully and saved at {output_file}.")
            else:
                print(f"Failed to fetch text file. HTTP Status Code: {response.status_code}")
        else:
            # Generate a sample text file
            sample_text = """The quick brown fox jumps over the lazy dog.
Python is fun and powerful for data processing.
This is a sample text file for processing."""
            with open(output_file, "w") as file:
                file.write(sample_text)
            print(f"Sample text file generated and saved at {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_text_file()


