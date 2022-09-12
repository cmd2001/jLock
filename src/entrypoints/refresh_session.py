import sys
sys.path.append('')

import src.core.session as session
import src.config as config

import logging
logging.basicConfig(level=config.LOG_LEVEL)

session.refresh_session(username=config.JACCOUNT_USERNAME, 
                              password64=config.JACCOUNT_PASSWORD64, 
                              refresh_interval=config.REFRESH_SESSION_INTERVAL, 
                              session_file_path=config.SESSION_FILE_PATH, 
                              session_time_file_path=config.SESSION_TIME_FILE_PATH,
                              force_refresh=True)
