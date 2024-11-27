import math

f = open("day_2_input.txt",'r')
lines=f.read().split('\n')

dict = {
    "red":12,
    "green":13,
    "blue":14
}

s=0
for line in lines:
    tmp = line.split(': ')
    L = tmp[1]
    id = int(tmp[0].split(' ')[1])
    for set in L.split('; '):
        for balls in set.split(', '):
            nb,color = balls.split(" ")
            if int(nb) > dict[color]:
                id = 0
    s+=id
print(s)


#--------part 2-----------------
s=0
for line in lines:
    tmp = line.split(': ')
    L = tmp[1]
    dict_2 = {
        "red":0,
        "green":0,
        "blue":0
    }
    for set in L.split('; '):
        for balls in set.split(', '):
            nb,color = balls.split(" ")
            dict_2[color] = max(int(nb),dict_2[color])
    power = math.prod(dict_2.values())
    print(dict_2)
    s+=power
print(s)
