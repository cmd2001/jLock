import sys
sys.path.append('')

import src.utils.constraints as constraints
import src.core.operation as operation
import src.core.session as session
import src.config as config

import logging
logging.basicConfig(level=config.LOG_LEVEL)

cookies = session.get_cookies(username=config.JACCOUNT_USERNAME, 
                              password64=config.JACCOUNT_PASSWORD64, 
                              refresh_interval=config.REFRESH_SESSION_INTERVAL, 
                              session_file_path=config.SESSION_FILE_PATH, 
                              session_time_file_path=config.SESSION_TIME_FILE_PATH)


operation.unlock_door(room_id=config.ROOM_ID, 
                      user_agent=constraints.REQUESTS_USER_AGENT, 
                      referer=constraints.REQUESTS_REFER_BASEURL.format(config.ROOM_ID), 
                      url=constraints.REQUESTS_URL, 
                      cookies=cookies,
                      operation_time_file_path=config.OPERATION_TIME_FILE_PATH)
