JACCOUNT_USERNAME = 'Amagi_Yukisaki' # Your jAccount username here, for example '[username]@sjtu.edu.cn'
JACCOUNT_PASSWORD64 = b'UEFTU1cwUkQ=' # your base64 encoded jAccount password here, get it by base64.b64encode(b'PASSW0RD')
ROOM_ID = '00112233445566778899aabbccddeeff' # 32 hexadecimal bits, get it by scanning the QR code on your door, copying the url and removing the last 8 bits

REFRESH_SESSION_INTERVAL = int(60 * 60 * 1e9) # refresh every hour
RELOCK_INTERVAL = int(6 * 1e9) # relock after 6 seconds

SESSION_FILE_PATH = 'jLock.session'
SESSION_TIME_FILE_PATH = 'session_refreshed_time.txt'
OPERATION_TIME_FILE_PATH = 'last_unlocked_time.txt'

LOG_LEVEL = 'INFO'