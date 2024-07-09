from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)

    }
print('Valores sorteados: ')
for c, v in jogo.items():
    print(f'{c} tirou {v} no dado. ')
    sleep(0.5)
resultado = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Os vencedores foram: ')
for c, v in enumerate(resultado):
    print(f'Na {c+1}° colocação ficou o {v[0]}. ')
    sleep(0.5)
