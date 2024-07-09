lista = []
pares = []
impares = []
r = 's'
while r not in 'Nn':
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? (S/N) '))
print(f'A lista completa é {lista} ')
print(f'A lista de pares é {pares} ')
print(f'A lista de ímpares é {impares} ')
