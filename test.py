# test1 = 'This is a test of the emergency text system'
# fout = open('test.txt', 'wt')
# fout.write(test1)
# fout.close()

# fin = open('test.txt', 'rt')
# test1 = fin.read()
# print(test1)
# fin.close()

import csv
# a = [
# 	['author','book'],
# 	['J R R TYolek','The hobiut'],
# 	['Luyn tus','Eats, hoors & fjias'],
# 	]

# with open('aaa', 'wt') as fout:
# 	csvout = csv.writer(fout)
# 	csvout.writerows(a)

with open('aaa', 'rt') as fin:
	cin = csv.DictReader(fin, fieldnames=['first', 'last'])
	aaa= [row for row in cin]

print(aaa)