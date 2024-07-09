from random import randint
a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)

n = (a, b, c, d, e)

print(f'Os numeros gerados foram: ', end='')
for c in n:
    print(c, end=' ')
print()
print(f'O menor valor gerado foi {sorted(n)[0]}! ')
print(f'O maior valor gerado foi {sorted(n)[4]}')
