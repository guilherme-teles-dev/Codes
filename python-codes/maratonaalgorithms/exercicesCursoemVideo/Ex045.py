from random import choice
jogador = str(input('O que deseja jogar? (PEDRA, PAPEL, TESOURA ) ')).upper()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)
if computador != jogador:
    print(f'{computador}! Você perdeu! ')
elif computador == jogador:
    print(f'{computador}! Deu empate! ')
else:
    print(f'{computador}! Você ganhou! ')
