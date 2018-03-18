from pickle import Unpickler

obj = Unpickler(open('../data/5.dat')).load()
for l in obj:
    chars = ''
    for pair in l:
        chars = chars + pair[0]*pair[1]
    print chars
