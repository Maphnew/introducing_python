# 10.5 연습문제

#1
from datetime import date
from datetime import datetime 
now = date.today()
now_str = now.isoformat()
print(now_str)
with open('today.txt', 'wt') as output:
	print(now_str, file=output)
	# output.write(now_str)

#2
with open('today.txt', 'rt') as input:
	today_string = input.read()
print('2: ', today_string)

#3
fmt = '%Y-%m-%d\n'
print(datetime.strptime(today_string, fmt))

#4
import os
print(os.listdir('.'))

#5
print(os.listdir('..'))

#6
# import multiprocessing

# def now(seconds):
# 	from datetime import datetime
# 	from time import sleep
# 	sleep(seconds)
# 	print('wait', seconds,'seconds, time is', datetime.utcnow())

# if __name__ == '__main__':
# 	import random
# 	for n in range(3):
# 		seconds = random.random()
# 		proc = multiprocessing.Process(target=now, args=(seconds,))
# 		proc.start()

#7
my_day = date(1987, 2, 15)
print(my_day)

#8
print(my_day.weekday())
print(my_day.isoweekday())
#    weekday(): 0 월 1 화 2 수 3 목 4 금 5 토 6 일
# isoweekday(): 1 월 2 화         ---        7 일

#9
from datetime import timedelta
party_day = my_day + timedelta(days=11675)
print(party_day)

now = date.today()
print(now - my_day)