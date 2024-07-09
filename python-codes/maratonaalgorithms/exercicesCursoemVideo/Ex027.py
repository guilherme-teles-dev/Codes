nome = str(input('Qual é o seu nome? '))
corte = nome.split()
primeiro = corte[0]
cortelen = len(corte) - 1
ultimo = corte[cortelen]
print(f'Primeiro nome = {primeiro}')
print(f'Ultimo nome = {ultimo}')
