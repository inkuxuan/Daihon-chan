import logging
import os
from pathlib import Path

appname = 'daihon_chan'

# Define the path for the log file
def get_log_path():
    log_dir = Path.home().joinpath('.config', appname, 'logs')
    log_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists
    return log_dir.joinpath('app.log')

# Setup logger
def setup_logger():
    log_path = get_log_path()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()  # If you also want to print the logs to the console.
        ]
    )

# Example usage
def main():
    setup_logger()
    logging.info("Logger test")

if __name__ == "__main__":
    main()
