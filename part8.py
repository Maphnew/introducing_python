# 8 data
# 8.1 in out file
# r 읽기
# w 쓰기 (존재하지 않으면 생성, 존재하면 덮어씀)
# x 쓰기 (존재하지 않을 경우에만 쓰기)
# a 추가하기 (파일의 끝에서 부터 쓴다)

# t: 텍스트 타입
# b: 이진 타입

poem = ''
fin = open('wr.txt', 'rt')
chunk = 100
while True:
	fragment = fin.read(chunk)
	if not fragment:
		break
	poem += fragment
fin.close()
print(poem)

# 8.2

import csv
villains = [
	[1,2],
	[5,67],
	[2,55],
	]

with open('villains', 'wt') as fout:
	csvout = csv.writer(fout)
	csvout.writerows(villains)

with open('villains', 'rt') as fin:
	cin = csv.reader(fin)
	villains = [row for row in cin]

print(villains)

# 8.2.2
# 8.2.4 json
import datetime
import json
now = datetime.datetime.utcnow()
now_str = str(now)
print(json.dumps(now_str))
from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

# 8.2.5 YAML
# 8.2.6 보안노트
# 8.2.7 설정파일

# 8.2.9 pickle
import pickle, datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)
print(now2)
print(type(now2))

# 8.3 구조화된 이진 파일
# 8.3.1 스프레드 시트
# 8.3.2 HDF5

# 8.4.2 DB-API
# connect()
# cursor()
# execute(), executemany()
# fetchone(), fetchmany(), fetchall()

import sqlite3
# conn = sqlite3.connect('enterprise.db')
# curs = conn.cursor()
# curs.execute('''CREATE TABLE zoo
# 	(critter VARCHAR(20) PRIMARY KEY,
# 	count INT,
# 	damages FLOAT)''')
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('INSERT INTO zoo VALUES("duckk", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?,?,?)'
curs.execute(ins,('weasel', 1, 2000.0))
# placeholder는 웹에서 악의적인 sql 명령을 삽입하는 외부공격 sql인젝션으로부터 시스템을 보호한다.
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)
curs.close()
conn.close()

# 8.4.6 SQLAlchemy

# 8.5 NoSQL 데이터 스토어
import dbm
# db = dbm.open('definitions', 'c')

# db['mustard'] = 'yellow'
# print(len(db))
# print(db['mustard'])
# db.close()
db = dbm.open('definitions', 'r')
print(db['mustard'])
# 8.5.2 Memcached
# 8.5.3 Redis

import redis
conn = redis.Redis('localhost', 6379)
print(conn.keys('*'))
#conn.set('secret', 'ni!')
#conn.set('carats', 24)
#print(conn.set('fever', '101.5'))

#print(conn.get('secret'))
#print(conn.get('carats'))
#print(conn.get('fever'))

#print(conn.setnx('secret', 'icky-icky'))
#print(conn.getset('secret', 'icky-icky'))

#print(conn.getrange('secret', -6, -1))
#print(conn.setrange('secret', 0, 'ICKY'))
#print(conn.get('secret'))

#print(conn.mset({'pie':'cherry', 'cordial':'sherry'}))
#print(conn.mget(['fever','carats']))
# print(conn.delete('fever'))
# print(conn.incr('carats'))
# print(conn.incr('carats',10))
# print(conn.decr('carats'))
# print(conn.decr('carats',15))
# print(conn.keys('*'))

# print(conn.set('fever', '101.5'))
# print(conn.incrbyfloat('fever'))
# print(conn.incrbyfloat('fever', 0.5))

#print(conn.incrbyfloat('fever', -2.0))

# 리스트
#print(conn.lpush('zoo','bear'))
#print(conn.lpush('zoo','alligater','duck'))
# print(conn.linsert('zoo','before','bear','beaver'))
# print(conn.linsert('zoo','after','bear','cassowary'))

#print(conn.lset('zoo', 2, 'marmoset'))
#print(conn.rpush('zoo','yak'))

#print(conn.lindex('zoo',3))
#print(conn.lrange('zoo', 0,2))

#print(conn.ltrim('zoo',1,4))
#print(conn.lrange('zoo', 0,-1))

# 해시
