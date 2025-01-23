# datafun-03-project
CC3.1: Create a Local Project Virtual Environment


## Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell

py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt

```

## Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push -u origin main
```
# Rename repo

```shell
git add .
git commit -m "change repo name to datafun-03-project/remove kersha" 
git push -u origin main


# Update readme to document changes
```shell
git add .
git commit -m "update read me with name change" 
git push -u origin main

# Data Processing Project

This project demonstrates the fetching, processing, and analysis of the mtcars dataset, which has been converted into various formats, including CSV, Excel, JSON and text files The results are stored in structured formats for further use.

---

## Fetcher Scripts

The fetcher scripts are designed to retrieve or generate data files. These files are saved in the `data` folder.

| Script                  | Description                                                                                       | Execution Command                     |
|-------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------|
| `kersha_get_csv.py`     | Fetches a CSV file (`mtcars.csv`) and saves it to the `example_data` folder.                      | `python data/kersha_get_csv.py`       |
| `kersha_get_excel.py`   | Fetches or converts a dataset into an Excel file (`mtcars.xlsx`) and saves it to `example_data`.  | `python data/kersha_get_excel.py`     |
| `kersha_get_json.py`    | Converts `mtcars.csv` into a JSON file (`mtcars.json`) and saves it to the `example_data` folder. | `python data/kersha_get_json.py`      |
| `kersha_get_text.py`    | Fetches or generates a text file (`sample.txt`) and saves it to the `example_data` folder.        | `python data/kersha_get_text.py`      |

---

## Processor Scripts

The processor scripts are designed to calculate metrics or perform analysis on the fetched data. The processed files are saved in the `data_processed` folder.

| Script                  | Description                                                                                       | Execution Command                     |
|-------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------|
| `kersha_process_csv.py` | Processes `mtcars.csv` to calculate metrics (e.g., Average MPG) and saves `processed_mtcars.csv`. | `python data_processed/kersha_process_csv.py` |
| `kersha_process_excel.py` | Processes `mtcars.xlsx` to calculate metrics and saves `processed_mtcars.xlsx`.                 | `python data_processed/kersha_process_excel.py` |
| `kersha_process_json.py` | Processes `mtcars.json` to calculate metrics (e.g., Median Weight) and saves `processed_mtcars.json`. | `python data_processed/kersha_process_json.py` |
| `kersha_process_text.py` | Processes `sample.txt` to calculate text metrics (e.g., line count, word count) and saves `processed_sample.txt`. | `python data_processed/kersha_process_text.py` |

---

## Execution Commands

### Fetchers
Run the following commands to generate or fetch the raw data:
```bash
# Fetch CSV file
python data/kersha_get_csv.py

# Fetch Excel file
python data/kersha_get_excel.py

# Fetch JSON file
python data/kersha_get_json.py

# Fetch or generate a text file
python data/kersha_get_text.py

# Processors
Run the following commands to process the fetched data and generate metrics:
# Process CSV file
python data_processed/kersha_process_csv.py

# Process Excel file
python data_processed/kersha_process_excel.py

# Process JSON file
python data_processed/kersha_process_json.py

# Process Text file
python data_processed/kersha_process_text.py

# Project Structure

C:\44608 projects spring 2025\datafun-03-projects
    ├── example_data
    │   ├── mtcars.csv
    │   ├── mtcars.json
    │   ├── mtcars.xlsx
    │   ├── sample.txt
    ├── data_processed
    │   ├── processed_mtcars.csv
    │   ├── processed_mtcars.json
    │   ├── processed_mtcars.xlsx
    │   ├── processed_sample.txt
    ├── data
    │   ├── kersha_get_csv.py
    │   ├── kersha_get_excel.py
    │   ├── kersha_get_json.py
    │   ├── kersha_get_text.py
    ├── data_processed
    │   ├── kersha_process_csv.py
    │   ├── kersha_process_excel.py
    │   ├── kersha_process_json.py
    │   ├── kersha_process_text.py
    ├── README.md

