times = int(input())
a = 0
b = 0
for time in range(times):
    a, b = map(int, input().split())
    if a%b == 0:
        print(0)
    else:
        if a > b:
            print(b-(a%b))
        elif b > a:
             print(b-a)
