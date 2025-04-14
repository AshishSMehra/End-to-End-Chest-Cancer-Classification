import os
import sys
import logging

# Logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Log directory and file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Create and configure logger
logger = logging.getLogger("cnnClassifierLogger")
logger.setLevel(logging.INFO)
logger.propagate = False  # Avoid duplicate logs in some environments

# Check if handlers already exist to avoid duplicate logs
if not logger.handlers:
    # File Handler
    file_handler = logging.FileHandler(log_filepath)
    file_handler.setFormatter(logging.Formatter(logging_str))

    # Stream Handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter(logging_str))

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
