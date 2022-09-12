import requests, logging, time

def unlock_door(room_id: str, user_agent: str, referer: str, url: str, cookies: dict, operation_time_file_path: str):
  params = { 'roomid': room_id }
  headers = {
    'User-Agent': user_agent,
    'Referer': referer,
  }

  logging.info('Opening Door with ID {}'.format(room_id))
  requests.get(url, params=params, cookies=cookies, headers=headers)
  logging.info('Door should be Opened')

  logging.info('Writing Operation Record')
  current_time = time.time_ns()
  with open(operation_time_file_path, 'w') as f:
    f.write(str(current_time))