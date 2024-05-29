input1 = input().lower()
input2 = input().lower()
f1 = 0
f2 = 0
for c in range(0, len(input1)):
    f1 += ord(input1[c]) - 96
    f2 += ord(input2[c]) - 96
    if(f1 != f2):
        break
if(f1 > f2):
    print(1)
elif(f2 > f1):
    print(-1)
elif(f1 == f2):
    print(0)