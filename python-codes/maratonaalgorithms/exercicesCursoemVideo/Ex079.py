lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso! ')
    elif valor in lista:
        print('Valor existente, não será adicionado! ')
    r = str(input('Deseja continuar? (s/n) ')).upper()
    if r == 'N':
        break
lista.sort()
print(f'Os calores digitados foram: {lista}')
