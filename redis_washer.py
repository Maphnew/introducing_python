import redis
from datetime import datetime
conn = redis.Redis()
print('Washer is starting')
dishes = ['salad', 'bread', 'entree', 'desert']
for dish in dishes:
	msg = dish.encode('utf-8')
	conn.rpush('dishes', msg)
	print('Washed', dish, ', time: ', datetime.now())
conn.rpush('dishes', 'quit')
print('Washer is done')