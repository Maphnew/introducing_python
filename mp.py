#!
# 10.3.2 프로세스 생성하기: m p
import multiprocessing
import os

# def do_this(what):
# 	whoami(what)

# def whoami(what):
# 	print("Process %s says: %s"%(os.getpid(), what))

# if __name__ == "__main__":
# 	whoami("I'm the main program")
# 	for n in range(4):
# 		p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n,))
# 		p.start()

# 10.3.3 프로세스 죽이기: terminate()
# import time
# def whoami(name):
# 	print("I'm %s, in process %s" % (name, os.getpid()))
# def loopy(name):
# 	whoami(name)
# 	start = 1
# 	stop = 1000000
# 	for num in range(start, stop):
# 		print("\tNumber %s of %s. Honk!" % (num, stop))
# 		time.sleep(1)

# if __name__ == "__main__":
# 	whoami("main")
# 	p = multiprocessing.Process(target=loopy, args=("loopy",))
# 	p.start()
# 	time.sleep(5)
# 	p.terminate()
# 10.4 달력과 시간
# 윤년
import calendar
# print(calendar.isleap(1900))
# print(calendar.isleap(1996))
# print(calendar.isleap(1999))

# 10.4.1 datetime 모듈
from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)

print('iso: ', halloween.isoformat())
# iso는 국제표준화기구(ISO)에서 제정한 날짜와 시간 표현에 대한 국제표준규격 참고

now = date.today()
print(now)

from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now+one_day
print(tomorrow)
print(now+17*one_day)
yesterday = now - one_day
print(yesterday)

from datetime import time 
noon = time(12,0,0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

from datetime import datetime
some_day = datetime(2015, 1, 2, 3, 4, 5, 6)
print(some_day)
print(some_day.isoformat())

now = datetime.now()
nowMsec = str(now)[:-3]
print(nowMsec)

from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)

# 10.4.2 time module
import time
now = time.time()
print(now)
print(time.ctime(now))

print(time.localtime(now))
print(time.gmtime(now))

tm = time.localtime(now)
print(time.mktime(tm))

# 10.4.3 날짜와 시간 읽고 쓰기
import time
fmt = "It's %A, %B, %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t))

from datetime import date 
fmt = "It's %B, %d, %Y, local time %I:%M:%S%p"
some_day = date(2019, 1, 2)
print(some_day.strftime(fmt))

from datetime import time 
some_time = time(10,36)
print(some_time.strftime(fmt))

import time
fmt = "%Y-%m-%d"
print(time.strptime("2019-09-09", fmt))

import locale
from datetime import date
halloween = date(2019, 10, 31)
for lang_country in ['ko_kr', 'en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
	print(locale.setlocale(locale.LC_ALL, lang_country))
	print(halloween.strftime('%A, %B %d'))

print(locale.locale_alias.keys())

# 10.4.4 대체모듈
