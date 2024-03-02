import os
import logging
from datetime import datetime
from from_root import from_root

log_dir = 'logs'
date_subdir = datetime.now().strftime('%Y_%m_%d')
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(from_root(), log_dir, date_subdir, LOG_FILE)

os.makedirs(os.path.join(from_root(), log_dir, date_subdir), exist_ok=True)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
