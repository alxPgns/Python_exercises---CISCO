import re

f = open("commands.txt", "r")  # open txt file
li = []

# take only "good commands"
for line in f:
    if "switchport trunk allowed vlan" in line:
        li.append(line)
f.close()
print(li)
List_1 = []
List_2 = []

# convert list into string, to apply regex
li_new = ''.join(li)
print(li_new)

# regex for finding numbers only
a = re.findall(r"(\d.+)", li_new, re.MULTILINE)
print(a)

# every single vlan number is a string value
b = ','.join(a)
b = b.split(',')
print(b)

# find common good vlans
List_1 = list((set([x for x in b if b.count(x) == len(li)])))
List_1_int = [int(x) for x in List_1]
print(sorted(List_1_int))

# find unique good vlans
List_2 = list((set([x for x in b if b.count(x) == 1])))
List_2_int = [int(x) for x in List_2]
print(sorted(List_2_int))