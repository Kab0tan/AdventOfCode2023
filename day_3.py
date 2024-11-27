from itertools import groupby
import re
import numpy as np
import math

def spe_split(s):
    #true si on a que des int dans le substring, false si possède 1+ char spécial
    result = re.findall(r'\d+', s)
    return result == [s], result

def splitWithIndices(s, delimiter):
    start = 0
    for key, group in groupby(s, lambda x:x==delimiter):
        g = list(group)
        end = start + sum(1 for i in g)
        if not key:
            yield start, end, ''.join(g)
        start = end

def check_substring(row,sub, store):
    clean, res = spe_split(sub[2])
    if not clean and res:
        for nb in res:
            tmp = (sub[0], sub[1], nb)
            if tmp not in store:
                store.add(tmp+ (row,))



def neigh(row,s,store):
    #check même ligne à gauche et droite
    if s[0]>0:
        if re.search(r'[^a-zA-Z0-9.]', lines[row][s[0]-1]):
            store.add(s+ (row,))
    if s[1]<len(lines[0]):
        if re.search(r'[^a-zA-Z0-9.]', lines[row][s[1]]):
            store.add(s+ (row,))
    #check ligne du dessus
    if row>0:
        if re.search(r'[^a-zA-Z0-9.]', lines[row-1][s[0]:s[1]]):
                store.add(s+ (row,))
        if s[0]>0:
            if re.search(r'[^a-zA-Z0-9.]', lines[row-1][s[0]-1]):
                store.add(s+ (row,))
        if s[1]<len(lines[0]):
            if re.search(r'[^a-zA-Z0-9.]', lines[row-1][s[1]]):
                store.add(s+ (row,))
    #check ligne du bas
    if row<len(lines)-1:
        if re.search(r'[^a-zA-Z0-9.]', lines[row+1][s[0]:s[1]]):
                store.add(s+ (row,))
        if s[0]>0:
            if re.search(r'[^a-zA-Z0-9.]', lines[row+1][s[0]-1]):
                store.add(s+ (row,))
        if s[1]<len(lines[0]):
            if re.search(r'[^a-zA-Z0-9.]', lines[row+1][s[1]]):
                store.add(s+ (row,))
    



f = open("day_3_input.txt",'r')
lines=f.read().split()

store = set()
for i in range(len(lines)):
    l1 = list(splitWithIndices(lines[i], '.'))
    for substring1 in l1:
        check_substring(i, substring1, store)
        if substring1 not in store and substring1[2].isnumeric():
            neigh(i,substring1,store)

s=0
for item in store:
    s += int(item[2]) 
print(s)



#-----------part 2---------------

#on isole * dans un subarray à part
def subarray(i, j, x, y, arr):
    start_row = max(0, i-x)
    end_row = min(n_row, i+x)
    start_col = max(0, j-y)
    end_col = min(n_col, j+y)
    new_i = i - start_row
    new_j = j - start_col
    return np.array([row[start_col:end_col+1] for row in arr[start_row:end_row+1]]), new_i,new_j

def splitWithNumericValues(s, delimiter):
    start = 0
    for key, group in groupby(s, lambda x: x.isnumeric()):
        g = list(group)
        end = start + sum(1 for i in g)
        if key:
            numeric_value = ''.join(char for char in g)
            yield start, end, numeric_value
        start = end

input = np.array([list(line.strip()) for line in lines])
s=0
n_row = input.shape[0]
n_col = input.shape[1]

for i in range(n_row):
    for j in range(n_col):
        if input[i,j] == '*':
            array,new_i,new_j = subarray(i, j, 1, 3, input)
            neigh = [max(0,new_j-1),new_j,min(n_col,new_j+1)]
            tmp = []
            b = 1
            left = ""
            right = ""
            #on check les nombres au dessus et en dessous
            if i not in [0,n_row-1]:
                split_row1 = list(splitWithNumericValues(array[0], '.'))
                for pair in split_row1:
                    if pair[2].isnumeric() and (int(pair[0]) in neigh or int(pair[1])-1 in neigh):
                        tmp.append(int(pair[2]))
                split_row3 = list(splitWithNumericValues(array[2], '.'))
                for pair in split_row3:
                    if pair[2].isnumeric() and (int(pair[0]) in neigh or int(pair[1])-1 in neigh):
                        tmp.append(int(pair[2]))
                
                
            elif i == 0:
                split_row3 = list(splitWithNumericValues(array[1], '.')) 
                for pair in split_row3:
                    if pair[2].isnumeric() and (int(pair[0]) in neigh or int(pair[1])-1 in neigh):
                        tmp.append(int(pair[2]))
                b=0

            elif i == n_row-1:
                split_row1 = list(splitWithNumericValues(array[0], '.'))
                for pair in split_row1:
                    if pair[2].isnumeric() and (int(pair[0]) in neigh or int(pair[1])-1 in neigh):
                        tmp.append(int(pair[2]))
            #on check les nombres à gauche et droite
            l =new_j
            while l-1 >= 0 and array[b][l-1].isnumeric() :
                left += array[b][l-1]
                l -= 1
            r =new_j
            while r+1 < 7 and array[b][r+1].isnumeric()  :
                right += array[b][r+1]
                r += 1
            if left.isnumeric():
                tmp.append(int(left[::-1]))
            if right.isnumeric():
                tmp.append(int(right))
            if len(tmp) == 2:
                s+= math.prod(tmp)

print(s)

