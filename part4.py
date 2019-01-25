#!/usr/bin/env/python3

### 4.7.7 일등시민 : 함수
def sum_args(*args):
	print(type(args))
	return sum(args)

def run_with_positional_args(func, *args):
	print(type(args))
	return func(*args)

a = run_with_positional_args(sum_args, 1,2,3,4,5)

print(a)

### 4.7.8 내부함수

def outer(a,b):
	def inner1(c,d):
		return c+d
	def inner2(e,f):
		return e*f
	return inner1(a,b), inner2(a,b)

print(outer(3,2))
print(type(outer(3,2)))

### 4.7.9 클로져

def knights2(saying):
	def inner2():
		return "saying: '%s'" %saying
	return inner2

a = knights2('Duck')

print(a)
print(type(a))

print(a())

###