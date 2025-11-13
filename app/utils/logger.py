import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(f"{LOG_DIR}/{name}.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger
