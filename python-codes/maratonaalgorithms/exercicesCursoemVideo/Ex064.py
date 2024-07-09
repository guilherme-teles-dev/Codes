numeros = 0
total = 0
n = 0
while n != 999:
    n = int(input('Digite um numero: (999 para parar: )'))
    if n < 999:
        total += n
        numeros += 1
    elif n > 999:
        total += n
        numeros += 1
print(f'Foram digitados {numeros} numeros! ')
print(f'A soma entre eles é {total}! ')
