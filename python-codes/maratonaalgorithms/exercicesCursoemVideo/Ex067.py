while True:
    n = int(input('Digite o numero que deseja saber a tabuada: '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{c*n}')
        c += 1
