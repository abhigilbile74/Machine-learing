import os
from datetime import datetime
import logging

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
))

# Console handler (optional, for printing logs while running)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
))

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
