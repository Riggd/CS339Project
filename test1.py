import re

with open('test1.txt') as infile:
	INlist = []
	lines = infile.readlines()
	print lines
	for line in lines:
		INlist.append(re.search("Indiana"))

print INlist