import pysjtu
import requests
import config, constraints
import logging
logging.basicConfig(level=config.LOG_LEVEL)

session = pysjtu.Session(proxies={})  # force disable proxy on some systems as httpx does NOT support socks proxy
logging.info('Logging in JAccount with username {}'.format(config.JACCOUNT_USERNAME))
session.login(username=config.JACCOUNT_USERNAME, password=config.JACCOUNT_PASSWORD)
logging.info('Log in Successfully!')
session.get('https://door.sjtu.edu.cn')
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