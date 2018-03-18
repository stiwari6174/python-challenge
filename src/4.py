import urllib as ul
import re

lnk = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
num = '12345'

i = 0
while num and i < 400:
    fp = ul.urlopen(lnk + num)
    src = fp.read()
    print src
    matchList = re.findall('next nothing is [0-9]+', src)
    if matchList == []: 
        # no matches
        if src.find("Divide by two") >= 0:
            num = str(int(num) / 2)
        else:
            # no next number and no directive found. We must be at the end 
            break
    else:
        # next number found
        nxt = matchList[0].split(' ')[-1]
        num = nxt
    i = i + 1