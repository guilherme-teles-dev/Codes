n1 = int(input('Digite o primeiro numero: '))
men = n1
mn = n1
n2 = int(input('Digite o segundo numero: '))
if n2 > mn:
    mn = n2
if n2 < men:
    men = n2
n3 = int(input('Digite o terceiro numero: '))
if n3 > mn:
    mn = n3
if n3 < men:
    men = n3
print(f'O menor valor é {men}! ')
print(f'O maior valor é {mn}! ')
