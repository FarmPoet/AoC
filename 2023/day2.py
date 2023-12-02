import re

bag = [12, 13, 14]
d = open("i2.txt").read().split("\n")[:-1]
p = [0, 0, 0]

for l in d:
    p[0] += 1
    r = int(max(list(map(int, re.findall("(\d+) r", l))), default = 0))
    g = int(max(list(map(int, re.findall("(\d+) g", l))), default = 0))
    b = int(max(list(map(int, re.findall("(\d+) b", l))), default = 0))
    if r <= bag[0] and g <= bag[1] and b <= bag[2]: p[1] += p[0]
    p[2] += r * g * b

p[1:]
