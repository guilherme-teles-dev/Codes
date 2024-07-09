matriz = [[], [], []]
for c in range(0, 3):
    for v in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {v}]: '))
        matriz[c].append(n)
for c in matriz:
    for v in c:
        print(f'[{v:^5}]', end='')
    print()
