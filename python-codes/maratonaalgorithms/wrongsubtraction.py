numbers = input().split()
n = int(numbers[0])
k = int(numbers[1])
for c in range(0, k):
    if int(numbers[0][len(numbers[0])-1]) != 0:
        n -= 1
        numbers[0] = str(n)
    else:
        n = int(n/10)
        numbers[0] = str(n)
print(n)