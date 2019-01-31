#!

# object & class

# 6.1 object
# object(data, code)
# object(variable, function)
# object(attribute, method)

# 6.2 class
class Person():
	def __init__(self, name):
		self.name = name

hunter = Person('Elmer Fudd')
print(hunter.name)

# 6.3 inheritance
class Car():
	def exclaim(self):
		print("I'm a Car!")

class Yugo(Car):
	def exclaim(self):
		print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
	def need_a_push(self):
		print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()

# 6.4 overide

# 6.5 add method

# 6.6 super

class EmailPerson(Person):
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email

bob = EmailPerson('Bob Frapples', 'bob@Frapples.com')

print(bob.name)
print(bob.email)

# 6.7 self
car = Car()
car.exclaim()

Car.exclaim(car)

# 6.8 get set property
class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name
	def get_name(self):
		print('inside the getter')
		return self.hidden_name
	def set_name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name
	name = property(get_name, set_name)

fowl = Duck('Howard')
print(fowl.name)
print(fowl.get_name())
fowl.name = 'Daffy'
print(fowl.name)

fowl.set_name('Daffiersue')
print(fowl.name)

class Duckk():
	def __init__(self, input_name):
		self.hidden_name = input_name
	@property
	def name(self):
		print('inside the getter')
		return self.hidden_name
	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name

fowl = Duckk('Howardd')
print(fowl.name)
fowl.name = 'Donaldo'
print(fowl.name)

class Circle():
	def __init__(self, radius):
		self.radius = radius
	@property
	def diameter(self):
		return 2*self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 8
print(c.diameter)

# 6.9 private name mangling

class Duck():
	def __init__(self,input_name):
		self.__name = input_name
	@property
	def name(self):
		print('inside the getter')
		return self.__name
	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donaldo'
print(fowl.name)

print(fowl._Duck__name)

# 6.10 method type

class A():
	count = 0
	def __init__(self):
		A.count +=1
	def exclaim(self):
		print("I'm an A!")
	@classmethod
	def kids(cls):
		print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

class CoyoteWeapon():
	@staticmethod
	def commercial():
		print('This CoyoteWeapon has been...')

CoyoteWeapon.commercial()

# 6.11 duck typing
class Quote():
	def __init__(self, person, words):
		self.person = person
		self.words = words
	def who(self):
		return self.person
	def says(self):
		return self.words + '.'

class QuestionQuote(Quote):
	def says(self):
		return self.words + '?'

class ExclamationQuote(Quote):
	def says(self):
		return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daff Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

class BabblingBrook():
	def who(self):
		return 'Brook'
	def says(self):
		return 'Babble'

brook = BabblingBrook()
def who_says(obj):
	print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

# 6.12 특수 method

# 6.13 composition

# 6.14 when

# 6.14.1 named tuple

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {'bill':'111', 'tail':'222'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail = 'trtt',bill='aaaaaaaaaa')
print(duck3)

# 6.15 practice

class thing():
	pass

print(thing())

t = thing()
print(t)

class Thing2():
	letters = 'abc'

print(Thing2.letters)

class Thing3():
	letters = 'xyz'
t3 = Thing3()
print(t3.letters)

class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number

e = Element('Hy', 'H', 1)
print(e.name)

# practice 6.5 ?
el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen.name)

hydrogen = Element(**el_dict)
print(hydrogen.name)

# 6.6
class Element:
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
	# def dump(self):
	# 	print(self.name, self.symbol, self.number)
	def __str__(self):
		print('name=%s, symbol=%s, number=%s'%(self.name, self.symbol, self.number))

# hydrogen = Element(**el_dict)
# hydrogen.dump()

# 6.7
# print(hydrogen)
hydrogen = Element(**el_dict)
# print(hydrogen)
#6.8
class Element:
	def __init__(self, name, symbol, number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number
	@property
	def name(self):
		return self.__name
	@property
	def symbol(self):
		return self.__symbol
	@property
	def number(self):
		return self.__number

hydrogen = Element('hydrogen','h',1)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

#6.9

class Bear:
	def eats(self):
		return 'berries'
class Rabbit:
	def eats(self):
		return 'clover'
class Octothorpe:
	def eats(self):
		return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()

print(b.eats())
print(r.eats())
print(o.eats())

# 6.10
class Laser:
	def does(self):
		return 'disintegrate'
class Claw:
	def does(self):
		return 'crush'
class SmartPhone:
	def does(self):
		return 'ring'
class Robot:
	def __init__(self):
		self.laser = Laser()
		self.claw = Claw()
		self.smartphone = SmartPhone()
	def does(self):
		return '''I have many attachments:
		My laser, to %s.
		My claw, to %s.
		My smartphone, to %s.'''%(
			self.laser.does(),
			self.claw.does(),
			self.smartphone.does())
robbie = Robot()
print(robbie.does())