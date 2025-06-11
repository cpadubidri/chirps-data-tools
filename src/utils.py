import logging
import os
from datetime import datetime


def logger(log_dir=None, log_filename="training.log", log_level=logging.INFO):
    """
    Args:
        log_dir (str, optional): Directory where logs will be saved. If None, logs will not be saved to a file.
        log_filename (str): Name of the log file.
        log_level (int): Logging level. Defaults to logging.INFO.

    Returns:
        logger (logging.Logger): Configured logger instance.
    """
    logger = logging.getLogger()
    logger.setLevel(log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, log_filename)

        file_handler = logging.FileHandler(log_file_path, mode="a")
        file_handler.setLevel(log_level)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger