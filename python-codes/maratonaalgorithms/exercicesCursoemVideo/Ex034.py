salario = float(input('Qual é o seu salário? '))
if salario > 1250:
    print(f'Seu salario sofrera um aumento de 10%, seu novo salario é R${(salario*10/100)+salario}! ')
else:
    print(f'Seu salario sofrera um aumento de 15%, seu novo salario é R${(salario*15/100)+salario}! ')
