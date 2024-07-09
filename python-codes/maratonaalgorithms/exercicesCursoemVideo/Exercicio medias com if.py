n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+ n2)/2
print(f'A sua media foi de {m:.1f}')
if m < 7:
    print('Que nota baixa você tirou. ')
else:
    print('Que boa nota você tirou! ')
