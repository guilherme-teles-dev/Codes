from math import sqrt
cop = float(input('Digite o cateto oposto: '))
cad = float(input('Digite o cateto adjacente: '))
h = sqrt(cop**2+cad**2)
print(f'A hipotenusa entre os catetos {cop} e {cad} é {h}. ')
