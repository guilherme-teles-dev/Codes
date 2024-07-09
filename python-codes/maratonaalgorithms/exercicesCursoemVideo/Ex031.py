viagem = float(input('Digite a distancia (Km) da sua viagem: '))
if viagem <= 200:
    print(f'O preço da sua passagem será de R${viagem*0.50}! ')
else:
    print(f'O preço da sua passagem será de R${viagem*0.45}! ')
