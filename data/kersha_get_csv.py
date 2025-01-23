import requests
import os

def fetch_csv():
    # URL for the mtcars.csv dataset
    url = "https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"
    
    # Ensure the output folder exists
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)
    
    # Path to save the file
    output_file = os.path.join(output_folder, "mtcars.csv")
    
    # Fetch the CSV file
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, "wb") as file:
            file.write(response.content)
        print(f"CSV file fetched and saved as {output_file}.")
    else:
        print("Failed to fetch CSV file. Please check the URL or your internet connection.")

if __name__ == "__main__":
    fetch_csv()


