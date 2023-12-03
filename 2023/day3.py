import re

gears = {}
bl = ["." * 140]; d = bl + open("i3.txt").read().split("\n") + bl; p = [0, 0]; l = len(d[0])
for i in range(1, len(d) - 1):
    try: 
        for j in [m.start() for m in re.finditer('\*', d[i])]: gears[i*1000 + j] = []
    except: pass
for i in range(1, len(d) - 1):
    x = [(int(m.group(0)), m.start(0), m.end(0)) for m in re.finditer("(\d+)", d[i])]
    for e in x:
        srt = max(0, e[1] - 1); end = min(l - 1, e[2] + 1)
        for j in range(-1, 2):
            try: gears[(i + j) * 1000 + srt + d[i + j][srt:end].index('*')].append(e[0])
            except: pass
        neighbors = d[i - 1][srt:end] + d[i][srt:end] + d[i + 1][srt:end]
        if(any([(c in '*-/#@&+=$%') for c in neighbors])): p[0] += e[0]
for g in gears.values():
    if(len(g) == 2): p[1] += g[0] * g[1]

p
