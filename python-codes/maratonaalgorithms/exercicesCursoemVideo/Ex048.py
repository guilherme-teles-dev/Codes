s = 0
for c in range(0, 500):
    if c % 3 == 0 and c % 2 != 0:
        s += c
print(f'A soma entre todos os numeros impares que são multiplos de 3 entre 1 e 500 é: {s}')
