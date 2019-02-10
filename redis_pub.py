# 11.2 network
# 11.2.1 pattern
# 11.2.2 발행 구독 모델
# breadcast

import redis
import random

conn = redis.Redis()
cats = ['siamese','persian','maine coon','norwegian forest']
hats = ['stovepipe','bowler','tam-o-shanter','fedora']

for msg in range(10):
	cat = random.choice(cats)
	hat = random.choice(hats)
	print('Publish: %s wears a %s' % (cat, hat))
	conn.publish(cat,hat)

