s = 0
num = int(input('Digite o numero: '))
for c in range (1, num+1):
    if num % c == 0:
        s += c
if s != num+1:
    print(f'O numero {num} é par! ')
else:
    print(f'O numero {num} é impar! ')
