latternumber = int(input())
latters = input()
antoncount = 0
danikcount = 0
for latter in latters:
    if latter == "A":
        antoncount += 1
    else:
        danikcount += 1
if antoncount > danikcount:
    print("Anton")
elif antoncount < danikcount:
    print("Danik")
else:
    print("Friendship")
