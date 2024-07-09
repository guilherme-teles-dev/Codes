from time import sleep
from random import randint
vitorias = 0
while True:
    print('O computador está pensando em um numero', end='')
    for c in range(0, 3):
        print('.', end='')
        sleep(0.5)
    print()
    jogador = int(input('Digite o numero: '))
    escolha = str(input('Par ou Impar (P/I): ')).upper()
    computador = randint(0, 10)
    if (jogador + computador) % 2 == 0 and escolha == 'P' or (jogador + computador) % 2 == 1 and escolha == 'I':
        print(f'Você ganhou! O computador escolheu {computador}! ')
        vitorias += 1
    else:
        print(f'Você perdeu! O computador escolheu {computador}! ')
        break
print(f'Você teve {vitorias} consecutivas! ')
