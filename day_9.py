f = open('day_9_input.txt','r')
lines = f.readlines()

lines = [list(map(int, x.split())) for x in lines]

def full_zeroes(L):
    return all([x == 0 for x in L])

#-----------part 1--------------------------------------


s1 = 0
for L in lines:
    last_int = []
    while not full_zeroes(L):
        last_int.append(L[-1])
        L = [L[i+1] - L[i] for i in range(len(L)-1)]
    s1 += sum(last_int)

print(s1)

#-----------part 2--------------------------------------

s2 = 0
for L in lines:
    i = 0
    while not full_zeroes(L):
        s2 += L[0]*(-1)**i
        L = [L[i+1] - L[i] for i in range(len(L)-1)]
        i += 1

print(s2)