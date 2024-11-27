import re

f = open('day_5_input.txt','r')
# lines = [line.strip() for line in f if line.strip()]
input = f.read().split('\n\n')
lines = [line.split('\n') for line in input]
seed = lines[0][0].split(": ")[1].split(' ')


#---------------part 1----------------
# new = seed.copy()
# old = seed.copy()
nb = len(seed)
# # print(lines)
# # print(seed)
# # print()

# for j in range(nb):
#     for i in range(1,len(lines)):
#         for t in range(1,len(lines[i])):
#             range_ = lines[i][t].split(' ')
#             source = int(range_[1])
#             dest = int(range_[0])
#             range_ = int(range_[2])
#             if source <= int(old[j]) <= source+range_:
#                 new[j] = int(old[j]) + (dest - source)
#                 old = new
#                 break
            # print(old)
            # print(new)
# print(min(new))


#-----------part 2--------------------------------------

modified_seed = seed.copy()
seed_pairs = []
for t in range(0,nb,2):
    modified_seed[t+1] = str(int(seed[t]) + int(seed[t+1])-1)
    seed_pairs.append([int(modified_seed[t]),int(modified_seed[t+1])])
# print(seed_pairs)

nb2 = len(seed_pairs)
m = float('inf')
# print(lines)

#on parcourt toutes les ranges de seed
for pair in seed_pairs:
    print(pair)
    #on parcourt chaque seed individuellement
    for seed in range(pair[0], pair[1], 1):
        cpy_seed = seed
        #pour chaque seed on lui applique son mapping jusqu'à location
        for i in range(1,len(lines)):
            for j in range(1,len(lines[i])):
                range_ = lines[i][j].split(' ')
                source = int(range_[1])
                dest = int(range_[0])
                range_ = int(range_[2])
                if source <= cpy_seed <= source+range_:
                    cpy_seed = cpy_seed + (dest - source)
                    break
        #qd on arrive à la ligne location, on a notre seed final transformée en location
        #on ne garde que le location le plus petit par rapport à toutes les anciennes seed transformées
        m = min(m, cpy_seed)
print(m)


#IDEA : compare range intersectiob and add the new range from mapping in a list of ranges