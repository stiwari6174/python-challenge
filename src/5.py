import pickle

f = open('../data/5.dat', 'rb')
obj = pickle.load(f)
for l in obj:
    chars = ''
    for pair in l:
        chars = chars + pair[0]*pair[1]
    print(chars)
