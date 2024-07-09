numeros = [[], []]
for c in range(0, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares digitados são ', end='')
for c in numeros[0]:
    print(c, end=' ')
print()
print(f'Os numeros impares digitados são ', end='')
for c in numeros[1]:
    print(c, end='
          ')
