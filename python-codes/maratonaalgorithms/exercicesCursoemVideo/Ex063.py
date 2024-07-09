n = int(input('Digite quantos numeros deseja saber da sequência Fibonacci: '))
c = 0

n1 = 0
n2 = 0
n3 = 1
print('0')
while c < n-1:
    print(n3)
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    c += 1
