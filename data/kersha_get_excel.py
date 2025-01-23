import requests
import zipfile
import os

def fetch_excel():
    url = "https://www.contextures.com/SampleData.zip"
    response = requests.get(url)
    if response.status_code == 200:
        zip_path = "data/SampleData.zip"
        with open(zip_path, "wb") as file:
            file.write(response.content)
        # Unzip the file
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall("data/")
        print("Excel file fetched and extracted to the data folder.")
        os.remove(zip_path)  # Cleanup zip file
    else:
        print("Failed to fetch Excel file.")

if __name__ == "__main__":
    fetch_excel()
