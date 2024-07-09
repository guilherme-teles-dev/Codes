media_idade = 0
homem_mais_velho = ['', 0]
mulheres_menos_20anos = 0
for c in range(0, 4):
    nome = str(input('Qual é o nome da pessoa: '))
    idade = int(input('Quantos anos a pessoa tem: '))
    sexo = str(input('Qual é o seru sexo: (M/F) ')).upper()
    media_idade += idade
    if idade > homem_mais_velho[1] and sexo == 'M':
        homem_mais_velho[0] = nome
        homem_mais_velho[1] = idade
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20anos += 1
print(f'A media de idade entre as pessoas digitadas é {media_idade/4}! ')
print(f'O nome do homem mais velho é {homem_mais_velho[0]}! ')
print(f'Existem {mulheres_menos_20anos} mulheres com menos de 20 anos! ')
