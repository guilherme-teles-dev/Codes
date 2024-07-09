time = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    partidas.clear()
    jogador.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:<2} tem o valor {v["nome"]}')
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        print('Volte sempre! ')
        break
    for c, v in enumerate(time[busca]['gols']):
        print(f'    No jogo {c+1} fez {v} gols')
