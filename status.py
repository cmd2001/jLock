import time
import config

import logging
logging.basicConfig(level=config.LOG_LEVEL)

current_time = time.time_ns()
last_time = -1

try:
  with open('last_operation.txt', 'r') as f:
    last_time = int(f.read())
except:
  pass

ret = int(current_time - last_time > config.RELOCK_PERIOD)
print(current_time, last_time, last_time+config.RELOCK_PERIOD)

logging.info(ret)
exit(ret)