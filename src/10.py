a = [1, 11, 21, 1211, 111221]
astr = [str(x) for x in a]
while len(astr) < 31:
    last = astr[-1]
    digits = [x for x in last]
    count = [1]
    numbers = [digits[0]]
    
    for i in range(1, len(digits)):
        if digits[i] == numbers[-1]:
            count[-1] = count[-1] + 1
        else:
            count.append(1)
            numbers.append(digits[i])
    astr.append(''.join([str(x[0]) + x[1] for x in zip(count, numbers)]))

print (len(astr[30]))
