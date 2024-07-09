maioridade = 0
for c in range (0, 7):
    idade = int(input('Digite a idade : '))
    if idade >= 21:
        maioridade += 1
print(f'O numero de pessoas que atingiram a maioridade são de {maioridade}! ')
