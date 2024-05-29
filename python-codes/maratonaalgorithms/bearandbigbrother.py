input = input().split()
a = int(input[0])
b = int(input[1])
count = 0
while(a <= b):
    a *= 3
    b *= 2
    count += 1
print(count)