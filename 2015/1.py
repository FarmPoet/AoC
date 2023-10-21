from itertools import takewhile

acc = 0
x = list(map(lambda y: 1 if y == '(' else -1, open('1.txt').read()[:]))
for p2, i in enumerate(takewhile(lambda x: acc != -1, x)): acc += i

sum(x), p2 + 1