lista = []
r = 's'
elementos = 0
while r != 'n':
    lista.append(int(input('Digite um valor: ')))
    elementos += 1
    r = str(input('Quer continuar? (S/N) ')).lower()
print(f'Você digitou {elementos} elementos! ')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista! ')
else:
    print('O valor 5 faz parte da lista! ')
