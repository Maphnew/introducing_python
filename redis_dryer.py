#!
import redis
from datetime import datetime
conn = redis.Redis()
print('Dryer is starting')
while True:
	msg = conn.blpop('dishes')
	if not msg:
		break
	val = msg[1].decode('utf-8')
	if val == 'quit':
		break
	print('Dried', val, ', time: ', datetime.now())
print('Dishes are dried')