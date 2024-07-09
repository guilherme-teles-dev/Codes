precos = ('Pyke Projeto', 20, 'Pyke PsyOps', 25, 'Pyke Lua Sangrenta', 30,
       'Pyke Espectro das Areias', 35)

for c in range(0, len(precos)):
    if c % 2 == 0:
        print(f'{precos[c]:.<30}', end='')
    elif c % 2 == 1:
        print(f'R${precos[c]}')
