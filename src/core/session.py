from struct import pack
from time import time
import time, logging, base64
from xmlrpc.client import boolean
import pysjtu

def refresh_session(username: str, password64: bytes, refresh_interval: int, session_file_path: str, session_time_file_path: str, force_refresh: boolean = False):
  password = str(base64.b64decode(password64), encoding='utf-8')
  current_time = time.time_ns()
  logging.info('Current time is {} (unixNano)'.format(current_time))
  last_time = -1
  try:
    with open(session_time_file_path, 'r') as f:
      last_time = int(f.read())
  except:
    pass
  logging.info('Last Session Was Created At {} (unixNano)'.format(last_time))

  session = pysjtu.Session()
  if force_refresh or current_time - last_time >= refresh_interval:
    logging.info('{}, Creating New Session'.format('Force Refresh' if force_refresh else 'Last Session Expired'))
    logging.info('Logging in JAccount with username {}'.format(username))
    session.login(username=username, password=password)
    logging.info('Log in Successfully!')
    session.get('https://door.sjtu.edu.cn')
    logging.info('Dumping Current Session')
    session.dump(session_file_path)
    with open(session_time_file_path, 'w') as f:
      f.write(str(current_time))
  else:
    logging.info('Loading Last Session')
    session.load(session_file_path)
  return session


def get_cookies(username: str, password64: bytes, refresh_interval: int, session_file_path: str, session_time_file_path: str):
  session = refresh_session(username=username, password64=password64, refresh_interval=refresh_interval, session_file_path=session_file_path, session_time_file_path=session_time_file_path)

  logging.info('Collecting Cookies')
  cookies = {}
  for cookie in session.cookies.jar:
    if cookie.domain == 'door.sjtu.edu.cn':
      cookies[cookie.name] = cookie.value
  logging.info('Cookies Coollected Successfully!')

  return cookies
