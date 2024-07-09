l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if l3 < l2 + l1 and l2 < l3 + l1 and l1 < l3 + l2:
    if l3 == l2 and l2 == l1 and l1 == l3:
        print('Triangulo Equilatero! ')
    elif l3 != l2 and l2 != l1 and l1 != l3:
        print('Triangulo Escaleno! ')
    else:
        print('Triangulo Isóceles! ')
else:
    print('Não é um triangulo! ')
