from hashlib import md5

i = 'yzbqklnj'
c = 0
p1 = p2 = 0
while(1):
    x = md5(bytes(i + str(c), 'ascii'))
    if x.hexdigest()[:6] == '000000': p2 = c
    if not p1 and x.hexdigest()[:5] == '00000': p1 = c
    if p1 and p2: break
    c += 1

p1, p2
