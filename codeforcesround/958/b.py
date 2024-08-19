cases = int(input())
for c in range(cases):
    #Input de values
    ninterger = int(input())
    sequencea = input()
    #Filter the information
    zerogroups = []
    zerogroup = []
    for item in sequencea:
        if item == '0':
            zerogroup.append(0)
        elif item == '1':
            if len(zerogroup) != 0:
                zerogroups.append(zerogroup)
    if len(zerogroups) >= sequencea.count("1"):
        print("No")
    else:
        print("Yes")
    