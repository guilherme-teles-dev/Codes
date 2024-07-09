from random import randint
from time import sleep
p = 0
jogador = 0
computador = 1
while jogador != computador:
    print('O computador está pensando em um numero', end='')
    for c in range(0, 3):
        sleep(1)
        print('.', end='')
    print('')
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    if jogador != computador:
        print(f'O computador pensou no numero {computador}! Você perdeu! ')
        p += 1
    elif jogador == computador:
        print(f'O computador pensou no numero {computador}! Você ganhou! ')
print(f'Você ganhou na {p} tentativa! ')
