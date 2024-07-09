l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 < l2+l3 and l2 < l1 +l3 and l3 < l1+l2:
    print(f'Essas medidas pordem formar um triangulo! ')
else:
    print(f'Essas medidas não podem formar um triangulo! ')
