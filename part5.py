#!/usr/bin/env/python3
# chapter5
# module, package, program

# 5.1 stand alone program
# 5.2 command line argument
import sys
print('Program arguments: ', sys.argv)
# 5.3 module & import
for place in sys.path:
	print(place)
# 5.4 package
# 5.5 python library
# 5.5.3 OrderedDict()
from collections import OrderedDict
quotes = OrderedDict([
	('Moe', 3),
	('Larry',[1,2,3,4,5]),
	('Curly','Nyuk nyuk!'),
	])

for stooge, sss in quotes.items():
	print(stooge, sss)
# 5.5.4 deque = stack + queue
# 5.5.6 pprint()
from pprint import pprint
pprint(quotes)

# 5.6 battery

# 5.7 practice
# 1
def hours():
	return 'Open 9-5 daily'

plain = {'a':1, 'b':2, 'c':3}
print(plain)

from collections import OrderedDict
fancy = OrderedDict([('a',1),('b',2),('c',3)])

for l, n in fancy.items():
	print(l,n)

from collections import defaultdict
a = defaultdict(int)

a['a'] = 1
print(a['b'])
print(a)

dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists)