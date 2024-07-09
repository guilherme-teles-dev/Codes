numeros = 0
soma = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    numeros += 1
    soma += n
print(f'Foram digitados {numeros} numeros. ')
print(f'A soma entre eles é: {soma}')
