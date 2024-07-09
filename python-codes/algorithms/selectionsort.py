array = list(map(int, input().split()))
novo_vetor = []
numero_atual = 0
while numero_atual < len(array):
    navegador = numero_atual
    menor_valor = ''
    while navegador < len(array):
        if navegador == numero_atual:
            menor_valor = array[navegador]
        else:
            if menor_valor > array[navegador]:
                aux = 0
                aux = menor_valor
                menor_valor = array[navegador]
                array[navegador] = aux
        navegador += 1
    numero_atual += 1
    novo_vetor.append(menor_valor)
print(novo_vetor)
