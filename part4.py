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

print(animal)
print(id(animal))

animal = 'fruitbat'
def change_and_print_global():
	global animal
	animal_before = animal
	animal = 'wombat'
	print('inside change_and_print_global: ', animal_before,' -> ',animal)

print(animal)
change_and_print_global()
print(animal)

animal = 'fruitbat'
def change_local():
	animal = 'wombat' # local variable
	print('locals: ', locals())

print(animal)
change_local()

print('globals: ', globals())
print(animal)

### 4.10.1 이름에 _와 __ 사용
# function.__name__
# function.__doc__

def amazing():
	'''This is the amazing function.
	Want to see it again?'''
	print('This function is named: ', amazing.__name__)
	print('And its docstring is: ', amazing.__doc__)

amazing()

### 4.11 error 처리하기: try, except

short_list = [1,2,3]
position = 5
try:
	short_list[position]
except:
	print('Need a position between 0 and ', len(short_list)-1, ' but got ',
		 position)

# short_list = [1,2,3]
# while True:
# 	value = input('Position [q to quit]? ')
# 	if value == 'q':
# 		break
# 	try:
# 		position = int(value)
# 		print(short_list[position])
# 	except IndexError as err:
# 		print('Bad index: ', position)
# 	except Exception as other:
# 		print('Something else broke: ', other)

### 4.12 예외 만들기 

# class UppercaseException(Exception):
# 	pass
class OopsException(Exception):
	pass

# words = ['eeenie', 'meenie', 'miny', 'MO']
# for word in words:
# 	if word.isupper():
# 		raise UppercaseException(word)

try:
	raise OopsException('panic')
except OopsException as exc:
	print(exc)

### 4.13 연습문제
# 4.1
guess_me = 7
if guess_me < 7:
	print('too low')
elif guess_me > 7:
	print('too high')
else:
	print('just right')

# 4.2
guess_me = 7
start = 1
while True:
	if guess_me < start:
		print('too low')
	elif guess_me == start:
		print('found it!')
		break
	elif guess_me > start:
		print('oops')
	start += 1

# 4.3
a_list = []
for i in range(4):
	a_list.append(3-i)
print(a_list)

# 4.4
b_list = [a for a in range(10) if a%2==0]
print(b_list)
# 4.5
squares = {a:a*a for a in range(10)}
print(squares)
# 4.6
set_a = {a for a in range(10) if a%2!=0}
print(type(set_a))
print(set_a)

# 4.7
got = (a for a in range(10))
print('Got ', list(got))

got = (a for a in range(10))
for i in got:
	print('Got ', i)

for n in ('Got!!! %s' % number for number in range(10)):
	print(n)

# 4.8
def good():
	list_a = ['Harry','Ron','Hermione']
	return list_a

print(good())

# 4.9
def get_odds(first=0, last=10, step=2):
	number = first+1
	while number < last:
		yield number
		number += step

go = get_odds(0,10)
print(go)

for x in go:
	print(x)

def get_odds2():
	for number in range(1,10,2):
		yield number

for count, number in enumerate(get_odds2(), 1):
	if count == 3:
		print("The third odd number is ", number)
		break

my_list = ['a', 'b', 'c']
counter_list = list(enumerate(my_list,1))
print(counter_list)
print(type(counter_list[0]))

# 4.10
def test(func):
	def new_func(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
		return result
	return new_func

@test
def greeting():
	print("Greetings, Eathling")

greeting()

# 4.11 
class OopsException(Exception):
	pass

try:
	raise OopsException('panic')
except OopsException as exp:
	print('Caught an oops! ', exp)

# 4.12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunt yarn shop']

dic = {t:p for t,p in zip(titles,plots)}
print(dic)

movies = dict(zip(titles,plots))
print(movies)