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

### 4.7.10 익명함수(anonymous function): lambda()
print('4.7.10 익명함수(anonymous function): lambda()')
def edit_story(words, func):
	for word in words:
		print(func(word))

stairs = ['thus', 'meow', 'thud', 'hiss']

def enliven(word):
	return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize()+'!')

### 4.8 제너레이터 generator
print('4.8 제너레이터')

print(sum(range(1,101)))

def my_range(first=0, last=10, step=1):
	number = first
	while number < last:
		yield number
		number += step

print(my_range)
ranger = my_range(1,5,1)
print(ranger)

for x in ranger:
	print(x)

### 4.9 데커레이터 decorator
print('4.9 decorator')

def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function: ', func.__name__)
		print('Positional arguments: ', args)
		print('Keyword arguments: ', kwargs)
		result = func(*args, **kwargs)
		print('Result: ', result)
		return result
	return new_function

def add_ints(a,b):
	return a+b

print(add_ints(3,5))
cooler_add_ints = document_it(add_ints) # 데커레이터를 수동으로 할당
print(cooler_add_ints(3,6))

@document_it
def add_ints(a,b):
	return a+b

print(add_ints(3,5))

def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args, **kwargs)
		return result*result
	return new_function

@document_it
@square_it
def add_ints(a,b):
	return a+b

print(add_ints(2,6))


@square_it
@document_it
def add_ints(a,b):
	return a+b

print(add_ints(2,6))

### 4.10 네임스페이스와 스코프 namespace & scope

animal = 'fruitbat'
def print_global():
	print('inside print_global: ', animal)

print('at the top level: ', animal)
print_global()

def change_and_print_global():
	print('inside change_and_print_global: ', animal)
	animal = 'wombat'
	print('after the change: ', animal)

# print(change_and_print_global())

def change_local():
	animal = 'wombat'
	print('insid change_local: ', animal, id(animal))

change_local()

