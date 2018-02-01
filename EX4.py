import re

# templates
access_template = ['switchport mode access', 'switchport access vlan {}', 'switchport nonegotiate', 'spanning-tree portfast',
'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan {}']

f = open("Int-Type.txt", "r")
# input check

# make a list of file's lines, every line is an acceptable input
li = []
[li.append(line) for line in f]
f.close()
li_new = ''.join(li)
li_new = li_new.split('\n')

# check interface mode and vlan number
while True:

        mode = input("Enter interface mode (access/trunk):")
        if mode == 'access':
            try:
                vlan_number = int(input("Enter VLAN number:"))
                break
            except ValueError:
                print("Vlan number must be integer")
        elif mode == 'trunk':
            try:
                allowed_vlans = int(input("Enter allowed VLANs:"))
                break
            except ValueError:
                print("Number of allowed vlans must be integer")
        else:
            print("Mode has to be either 'access' or 'trunk'")
            continue

# check interface type and number
while True:

    print("Enter interface type and number in this form: fa0/1")
    type_number = input("Enter interface type and number:")
    if type_number not in li_new:
        print("Not acceptable interface or interface number.\nAcceptable type of interfaces are: 'fa','gi'.\n"
              "Acceptable numbers are 1-24 for 'fa' and 0,1 for 'gi'\n")
        continue
    else:
        break


# replace {} with vlan number or allowed vlans number
if mode == 'access':
    access_template[1] = access_template[1].replace('{}',str(vlan_number))
else:
    trunk_template[2] = trunk_template[2].replace('{}',str(allowed_vlans))

# convert list into string
trunk_template = '\n'.join(trunk_template)
access_template = '\n'.join(access_template)

# print output
print("--------------------------------------")
if mode == 'access':
    print("Interface {:s}".format(type_number))
    print(access_template)

else:
    print("Interface {:s}".format(type_number))
    print(trunk_template)

