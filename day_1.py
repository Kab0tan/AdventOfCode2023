import re

#------------part 1------------
f = open("day_1_input.txt",'r')
lines=f.read().split()
s =0
for line in lines:
    tmp = re.findall("[0-9]", line)
    s += int(''.join(tmp[0] + tmp[-1])) 
print(s)

#---------part 2--------------
m = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

f = open("day_1_input_bis.txt",'r')
lines=f.read().split()
s =0
for line in lines:
    tmp = re.findall('(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
    tmp = [tmp[0]] + [tmp[-1]]
    tmp = [m[x] for x in tmp if x in m]
    s += int(''.join(tmp)) 
print(s)