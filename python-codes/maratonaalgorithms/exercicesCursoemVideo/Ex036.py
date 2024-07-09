casa = float(input('Quanto custa a casa? '))
salario = float(input('Qual é sua renda mensal? '))
anos = int(input('Em quantos anos você deseja pagar a casa? '))
if casa/anos/12 <= salario*30/100:
    print(f'A prestação mensal será de {casa/anos/12}. Emprestimo aprovado! ')
else:
    print(f'A prestação mensal será de {casa/anos/12}. Emprestimo recusado! ')
