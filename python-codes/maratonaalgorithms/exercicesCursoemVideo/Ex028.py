from random import randint
n = int(input('Digite o numero entre 0 e 5: '))
nc = randint(0, 5)
if n != nc:
    print(f'Você errou! o numero escolhido foi {nc}! ')
else:
    print(f'VocÊ acertou! o numero escolhido foi {nc}! ')
