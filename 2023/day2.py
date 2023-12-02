import re

br = 12
bg = 13
bb = 14

d = open("i2.txt").read().split("\n")[:-1]
game = 0
p1 = 0
p2 = 0

for l in d:
    game += 1
    r = int(max(list(map(int, re.findall("(\d+) r", l))), default = 0))
    g = int(max(list(map(int, re.findall("(\d+) g", l))), default = 0))
    b = int(max(list(map(int, re.findall("(\d+) b", l))), default = 0))
    if r <= br and g <= bg and b <= bb: p1 += game
    p2 += r * g * b

p1, p2
