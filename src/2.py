fp = open('../data/2.dat', 'r')

s = fp.read()

print ''.join([c for c in s if c.isalnum() == True])

fp.close()
