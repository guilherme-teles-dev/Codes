n = int(input())
second_line = [3]
second_line = list(map(int, input().split()))
y = second_line[0]
x = second_line[1]
z = second_line[2]
if(y >= n and x >= n and z >= n):
    print("S")
else:
    print("N")
