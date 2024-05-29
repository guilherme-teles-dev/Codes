binary = input()
team0 = 0
team1 = 0
dangerous = 0
for c in binary:
    if c == '1':
        team1 += 1
        team0 = 0
        if team1 == 7:
            dangerous = 1
    else:
        team0 += 1
        team1 = 0
        if team0  == 7:
            dangerous = 1
if dangerous == 1:
    print("YES")
else:
    print("NO")