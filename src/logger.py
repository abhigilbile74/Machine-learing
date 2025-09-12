
import os
from datetime import datetime
from src.logger import logging

# Create logs directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Log file with timestamp
log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,   # Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
)




