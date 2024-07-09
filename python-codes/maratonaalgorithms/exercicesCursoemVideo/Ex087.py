valoresp = 0
valor3c = 0
maior2l = 0
matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if n % 2 == 0:
            valoresp += n
        if c == 2:
            valor3c += n
        if l == 1:
            if c == 0:
                maior2l = n
            else:
                if n > maior2l:
                    maior2l = n
        matriz[l].append(n)
for l in matriz:
    for c in l:
        print(f'[{c:^5}]', end='')
    print()
print(f'A soma de todos os valores pares da matriz é {valoresp}. ')
print(f'A soma de todos os valores da terceira coluna é {valor3c}. ')
print(f'O maior valor da segunda linha é {maior2l}')
