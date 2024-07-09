r = 's'
soma = 0
divisão = 0
maior = 0
menor = 0
while r != 'n':
    n = int(input('Digite um numero: '))
    if soma == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
    divisão += 1
    r = str(input('Quer continuar? (S/N) ')).lower()
print(f'O maior valor digitado foi {maior}! ')
print(f'O menor valor digitado foi {menor}! ')
print(f'A medida entre todos eles é de {soma/divisão}! ')
    
