#!
import unicodedata
# chapter 7 data
def unicode_test(value):
	import unicodedata
	name = unicodedata.name(value)
	value2 = unicodedata.lookup(name)
	print('value="%s", name="%s", value2="%s"'% (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u2603')
unicode_test('e')

print(unicodedata.name('\u00e9'))
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

place = 'caf\u00e9'
print(place)

print(len('$'))
print(len('\U0001f47b'))

snowman = '\u2603'
print('len(snowman): ', len(snowman))
ds = snowman.encode('utf-8')
print(len(ds))
print(ds)
ds = snowman.encode('ascii', 'ignore')
print(ds)
ds = snowman.encode('ascii', 'replace')
print(ds)
ds = snowman.encode('ascii', 'backslashreplace')
print(ds)
ds = snowman.encode('ascii', 'xmlcharrefreplace')
print(ds)

# decoding

place = 'caf\u00e9'
print(place)
print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

# place3 = place_bytes.decode('ascii')
place4 = place_bytes.decode('latin-1')
print(place4)
place5 = place_bytes.decode('windows-1252')
print(place5)

# 7.1.2 format

print('{2} {1} {0}'.format('asdasd','21312124','tjhtfhht'))

# 7.1.3 정규표현식
import string
printable = string.printable
print(len(printable))

import re

print(re.findall('\d', printable))
print(re.findall('\w', printable))
print(re.findall('\s', printable))

# 7.2 이진데이터
blist = [1,2,3,255]
the_bytes = bytes(blist)
print(the_bytes)