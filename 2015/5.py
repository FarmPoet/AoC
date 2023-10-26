vowels = 'aeiou'
naughty = ['ab', 'cd', 'pq', 'xy']

data = open('5.txt').read().split()
p1 = p2 = 0

for i in data:
    # part1
    numVowels = len(list(filter(lambda x: x >= 0, sum([[y.find(x) for y in i] for x in vowels], []))))
    dups = [(j+k) for j,k in zip(i[0::1], i[1::1])]
    p1Dups = len(list(filter(lambda x: x[0] == x[1], dups)))
    isNaughty = True in [x in i for x in naughty]
    if numVowels > 2 and p1Dups and not isNaughty: p1 += 1
    
    # part2
    p2Dups = sum([i.count(x) for x in dups]) > len(i)
    triDups = len(list(filter(lambda x: x[0] == x[2], [(j+k+l) for j,k,l in zip(i[0::1], i[1::1], i[2::1])])))
    if p2Dups and triDups: p2 += 1
        
p1, p2
