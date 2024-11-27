

f = open("day_4_input.txt",'r')
lines=f.read().split("\n")
lines = [ line.split(":") for line in lines]


#-------------part 1-------------
L = []
M = []
for line in lines:
    have = line[1].split('|')[1].split()
    wins = line[1].split('|')[0].split()
    s = 0
    for win in wins:
        if win in have:
            s+=1
    if s>0:
        L.append(2**(s-1))
    M.append(s)
print(sum(L))


#-------------part 2-------------

dict = {}
for line in lines:
    if line[0] not in dict:
        dict[line[0]] = 1

for index, el in enumerate(M):
    if el != 0:
        for j in range(1,dict[f'Card {index+1}']+1):
            for i in range(1,el+1):
                dict[f'Card {index+1+i}'] += 1
print(sum(dict.values()))