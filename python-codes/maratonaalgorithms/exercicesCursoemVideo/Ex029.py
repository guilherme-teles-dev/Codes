v = float(input('Digite a velocidade do carro: '))
if v > 80:
    multa = (v-80)*7
    print(f'Você está a {v} Km. Você exedeu o limite de velocidade! sua multa foi de R${multa}! ')
else:
    print(f'Você está a {v} Km. Está dentro do limite! Parabens!')
