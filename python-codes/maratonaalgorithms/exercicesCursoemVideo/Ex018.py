from math import sin, tan, cos, radians

angulo = float(input('Digite o angulo: '))
graus = radians(angulo)
seno = sin(graus)
cosseno = cos(graus)
tangente = tan(graus)

print(f'O angulo {angulo} tem o seno de {seno} ')
print(f'O angulo {angulo} tem o cosseno de {cosseno} ')
print(f'O angulo {angulo} tem a tangente de {tangente} ')
