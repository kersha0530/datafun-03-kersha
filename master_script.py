import os
import subprocess
from utils_logger import logger  # Import the Loguru logger

# Paths to your scripts
fetch_scripts = [
    r"C:\44608 projects spring 2025\datafun-03-projects\data\kersha_get_csv.py",
    r"C:\44608 projects spring 2025\datafun-03-projects\data\kersha_get_excel.py",
    r"C:\44608 projects spring 2025\datafun-03-projects\data\kersha_get_json.py",
    r"C:\44608 projects spring 2025\datafun-03-projects\data\kersha_get_text.py",
]

process_scripts = [
    r"C:\44608 projects spring 2025\datafun-03-projects\data_processed\kersha_process_csv.py",
    r"C:\44608 projects spring 2025\datafun-03-projects\data_processed\kersha_process_excel.py",
    r"C:\44608 projects spring 2025\datafun-03-projects\data_processed\kersha_process_json.py",
    r"C:\44608 projects spring 2025\datafun-03-projects\data_processed\kersha_process_text.py",
]

def run_script(script_path):
    """
    Executes a Python script as a subprocess and logs its output.
    """
    try:
        logger.info(f"Running script: {script_path}")
        result = subprocess.run(
            ["python", script_path],  # It's "python" or "py" depending on your environment
            capture_output=True,
            text=True
        )
        # Log stdout and stderr
        logger.info(f"Output from {script_path}:\n{result.stdout}")
        if result.stderr:
            logger.error(f"Error output from {script_path}:\n{result.stderr}")
        logger.info(f"Completed script: {script_path}")
    except Exception as e:
        logger.error(f"Error running script {script_path}: {e}")

if __name__ == "__main__":
    logger.info("Starting fetch scripts...")
    for script in fetch_scripts:
        run_script(script)

    logger.info("Starting process scripts...")
    for script in process_scripts:
        run_script(script)

    logger.info("All scripts completed successfully.")



