input = input().split('+')
sum = []
for c in range(0, len(input)):
    sum.append(int(input[c]))
sum.sort()
if(len(sum) > 1):
    print(sum[0],end='')
    for c in range(1, len(sum)):
        print(f'+{sum[c]}',end='')
    print()
else:
    print(sum[0])