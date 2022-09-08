from urllib.request import proxy_bypass
import pysjtu
import requests
import config, constraints
import logging
import time
logging.basicConfig(level=config.LOG_LEVEL)

current_time = time.time_ns()
logging.info('Current time is {} (unixNano)'.format(current_time))
last_time = -1
try:
  with open('last_session_time.txt', 'r') as f:
    last_time = int(f.read())
except:
  pass
logging.info('Last Session Was Created At {} (unixNano)'.format(last_time))

session = pysjtu.Session(proxies=None)  # force disable proxy on some systems as httpx does NOT support socks proxy
if current_time - last_time >= config.REFRESH_SESSION_PERIOD:
  logging.info('Last Session Expired, Creating New Session')
  logging.info('Logging in JAccount with username {}'.format(config.JACCOUNT_USERNAME))
  session.login(username=config.JACCOUNT_USERNAME, password=config.JACCOUNT_PASSWORD)
  logging.info('Log in Successfully!')
  session.get('https://door.sjtu.edu.cn')
  logging.info('Dumping Current Session')
  session.dump('last_session.session')
  with open('last_session_time.txt', 'w') as f:
    f.write(str(current_time))
else:
  logging.info('Loading Last Session')
  session.load('last_session.session')

logging.info('Collecting Cookies')

cookies = {}
for cookie in session.cookies.jar:
  if cookie.domain == 'door.sjtu.edu.cn':
    cookies[cookie.name] = cookie.value
logging.info('Cookies Coollected Successfully!')

cookies.update(constraints.REQUESTS_COOKIE_DEFAULT)
params = { 'roomid': config.ROOM_ID }
headers = {
  'User-Agent': constraints.REQUESTS_USER_AGENT,
  'Referer':constraints.REQUESTS_REFER_BASEURL.format(config.ROOM_ID)
}

logging.info('Opening Door with ID {}'.format(config.ROOM_ID))
requests.get(constraints.REQUESTS_URL, params=params, cookies=cookies, headers=headers)
logging.info('Door should be Opened')

logging.info('Writing Operation Record')
current_time = time.time_ns()
with open('last_operation.txt', 'w') as f:
  f.write(str(current_time))