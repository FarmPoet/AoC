# 1

x = list(map(lambda y: 1 if y == '(' else -1, open('1.txt').read()[:]))
acc = 0
for i in range(len(x)):
    acc += x[i]
    if(acc == -1): break
sum(x), i + 1