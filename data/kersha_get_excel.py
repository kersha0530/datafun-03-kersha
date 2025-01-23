import pandas as pd
import os

def fetch_and_save_excel():
    # URL for the mtcars.csv dataset
    url = "https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"
    
    # Output folder and file
    output_folder = "example_data"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "mtcars.xlsx")
    
    # Fetch the dataset and save as Excel
    try:
        data = pd.read_csv(url)
        data.to_excel(output_file, index=False, sheet_name="MTCars")
        print(f"Excel file created and saved as {output_file}.")
    except Exception as e:
        print(f"Failed to fetch or save Excel file: {e}")

if __name__ == "__main__":
    fetch_and_save_excel()


