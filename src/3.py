import re

fp = open('../data/3.dat', 'r')
s = fp.read()

expr = '[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]'
print ''.join([x[4] for x in re.findall(expr, s)])

fp.close()
