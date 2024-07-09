n = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
     'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
     'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito',
     'Dezenove', 'Vinte')
numero = int(input('Digite o numero que deseja saber por extenso: '))
while numero > 20 or numero < 0:
    numero = int(input('Numero invalido, tente novamente: '))
print(f'Você digitou o numero {n[numero]}')
