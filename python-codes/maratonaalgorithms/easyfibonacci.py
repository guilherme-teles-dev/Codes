n = int(input())
i = 0
n1 = 0
n2 = 1
print(n1)
print(n2)
print(n2+n1)
while(i < n-2):
    aux = n1
    n1 = n2
    n2 = aux+n2
    print(n1+n2)
    i += 1
