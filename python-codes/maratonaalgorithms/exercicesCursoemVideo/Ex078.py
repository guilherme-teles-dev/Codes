lista = []
menor = 0
maior = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] < menor:
            menor = lista[c]
        elif lista[c] > maior:
            maior = lista[c]
print(f'Os valores digitados foram: {lista}')
print(f'O menor valor foi {menor}! Encontrado nas posições: ', end='')
for c, v in enumerate(lista):
    if v == menor:
        print(c, '...')
print(f'O maior valor foi {maior}! ', end='')
for c, v in enumerate(lista):
    if v == maior:
        print(c, '...')
