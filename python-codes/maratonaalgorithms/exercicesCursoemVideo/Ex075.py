a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
d = int(input('Digite o quarto numero: '))
numeros = (a, b, c, d)
print(f'O numero 9 foi digitado {numeros.count(9)} vezes! ')
if numeros.count(3) > 0:
    print(f'A primeira posição em que o numero 3 foi digitado é {numeros.index(3)+1}! ')
else:
    print('O valor 3 não foi digitado! ')
print(f'Os numeros pares digitados são: ', end='')
for a in numeros:
    if a % 2 == 0:
        print(a, end=' ')
