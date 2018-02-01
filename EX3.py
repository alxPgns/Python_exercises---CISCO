import re

f = open("ShowIpRoute.txt", "r")  # open txt file

# make a list of file's lines
li = []
[li.append(line) for line in f]
f.close()
print(li)

# convert list into string, to apply regex
li_new = ''.join(li)
# print(li_new)

# regex pattern
pattern = re.findall(r"(^\w \w\d |^\w )(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) (\[\d+\/\d+\]) via (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}), (\d.*), (.*)", li_new, re.MULTILINE)
pattern_length = len(pattern)

# output

for line in range(pattern_length):
    if pattern[line][0] == "R ":
        print("Protocol: RIP")
    if pattern[line][0] == "B ":
        print("Protocol: BGP")
    if pattern[line][0] == "E ":
        print("Protocol: EGP")
    elif pattern[line][0] == "D ":
        print("Protocol: EIGRP")
    elif pattern[line][0] == "D EX ":
        print("Protocol: EIGRP external")
    if pattern[line][0] == "O ":
        print("Protocol: OSPF")
    if pattern[line][0] == "O IA ":
        print("Protocol: OSPF inter area")
    elif pattern[line][0] == "O E1 ":
        print("Protocol: OSPF external type 1")
    elif pattern[line][0] == "O E2 ":
        print("Protocol: OSPF external type 2")
    elif pattern[line][0] == "i ":
        print("Protocol: IS-IS")
    elif pattern[line][0] == "i su ":
        print("Protocol: IS-IS summary")
    elif pattern[line][0] == "i L1 ":
        print("Protocol: IS-IS level 1")
    elif pattern[line][0] == "i L2 ":
        print("Protocol: IS-IS level 2")
    elif pattern[line][0] == "ia ":
        print("Protocol: IS-IS inter area")
    elif pattern[line][0] == "H ":
        print("Protocol: OSPF external type NHRP")
    elif pattern[line][0] == "N1 ":
        print("Protocol: OSPF NSSA external type 1")
    elif pattern[line][0] == "N2 ":
        print("Protocol: OSPF NSSA external type 2")
    print("Prefix: ",pattern[line][1])
    print("AD/Metric: ",pattern[line][2].strip('[]'))
    print("Next-Hop: ",pattern[line][3])
    print("Last update: ",pattern[line][4])
    print("Outbound Interface: ",pattern[line][5])