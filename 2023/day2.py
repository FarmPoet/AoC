import re
d = open("i2.txt").read().split("\n")[:-1]; p = [0, 0]
for i in range(len(d)):
    z = (lambda l, col: [int(max(list(map(int, re.findall("(\d+) " + col[i], l))))) for i in range(3)])(d[i], ['r', 'g', 'b'])
    if all(x <= y for x, y in zip(z, [12, 13, 14])): p[0] += i + 1
    p[1] += (lambda r, g, b: r * g * b)(*z)
p
