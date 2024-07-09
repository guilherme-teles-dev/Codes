jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
jogador['gols'] = gols
jogador['total'] = 0
for c in range(0, p):
    g = int(input(f'Quantos gols ele marcou na partida {c}? '))
    gols.append(g)
    jogador['total'] += g
print(jogador)
print('-='*30)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}. ')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {p} partidas. ')
for c, v in enumerate(jogador['gols']):
    print(f'{"=>":>8} Na partida {c}, fez {v} gols. ')
print(f'Foi total de {jogador["total"]} gols. ')
