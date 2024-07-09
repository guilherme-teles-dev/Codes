n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Reprovado! ')
elif media < 7 and media >= 5:
    print('Em Recuperação! ')
else:
    print('Aprovado! ')
