import time, logging

def get_door_status(operation_time_file_path: str, relock_interval: int): # 1 for locked, 0 for unlocked
  current_time = time.time_ns()
  last_time = -1

  try:
    with open(operation_time_file_path, 'r') as f:
      last_time = int(f.read())
  except:
    pass

  ret = int(current_time - last_time > relock_interval)

  return ret