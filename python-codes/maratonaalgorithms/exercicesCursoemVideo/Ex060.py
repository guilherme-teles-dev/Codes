n = int(input('Digite o numero que deseja saber o fatorial: '))
c = n
fatorial = 1
print(f'{n}! = ', end='')
while c != 0:
    fatorial = c*fatorial
    if c > 1:
        print(c, 'x ', end='')
    else:
        print(c, end='')
    c += -1
print(f' = {fatorial}')
