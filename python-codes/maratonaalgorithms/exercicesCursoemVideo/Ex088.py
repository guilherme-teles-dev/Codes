from random import randint
j = int(input('Quantos jogos você quer que eu sorteie: '))
jogos = []
for c in range(0, j):
    i = 0
    num = []
    while i < 6:
        k = randint(1, 60)
        if k not in num:
            num.append(k)
            i += 1
    jogos.append(num)
for c in jogos:
    print(c)
