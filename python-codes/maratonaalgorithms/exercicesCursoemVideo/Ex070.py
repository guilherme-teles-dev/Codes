total = 0
pm1000 = 0
pmb = ['', 0]
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    if total == 0:
        pmb[0] = nome
        pmb[1] = preco
    else:
        if pmb[1] > preco:
            pmb[0] = nome
            pmb[1] = preco
    if preco > 1000:
        pm1000 += 1
    total += preco
    r = str(input('Deseja continuar? (S/N) '))
    while r not in 'SsNn':
        r = str(input('Opção invalida! Digite novamente: (S/N) '))
    if r in 'Nn':
        break
print(f'''O gasto total da compra foi R${total}.
Foram registrados {pm1000} produtos que custam mais de R$1000.
O nome do produto mais barato é {pmb[0]} e seu preço é de {pmb[1]}. ''')
