import sys
sys.path.append('')

import src.core.status as status
import src.config as config

import logging
logging.basicConfig(level=config.LOG_LEVEL)

door_status = status.get_door_status(operation_time_file_path=config.OPERATION_TIME_FILE_PATH, 
                                     relock_interval=config.RELOCK_INTERVAL)
exit(door_status)