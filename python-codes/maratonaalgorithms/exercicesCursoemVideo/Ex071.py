valor = int(input('Digite o valor que deseja sacar: '))
n50 = valor// 50
n20 = (valor%50) // 20
n10 = ((valor%50)%20) // 10
n1 = (((valor%50)%20)%10) // 1

print(f'''As cedulas a serem entreges serão:
{n50} cedulas de 50.
{n20} cedulas de 20.
{n10} cedulas de 10.
{n1} cedulas de 1. ''')
