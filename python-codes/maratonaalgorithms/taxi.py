#Receber as variáveis
n = int(input())
groups = input().split()
childrens = []
#Declaração das variáveis de contagem de carros e lugares nos carros
cars = 0
carsit = 0
#Conversor da entrada para inteiros
for group in groups:
    childrens.append(int(group))
#Ordenação dos grupos do menor para o maior
childrens.sort()
childrens.append(0)
print(childrens)
#Processamento
for c in range(0, len(childrens)-1): #Looping para percorrer os índices de childrens
    print(c)
    carsit += childrens[c] #Alocar as crianças nos bancos dos carros
    print("Crianças no carro: ", carsit)
    print("Carros usados: ", cars)
    #Abertura do bloco condicional
    if(carsit + childrens[c+1] > 4): #Se couber não mais um grupo
        cars += 1 #Conte um carro
        carsit = 0 #Tire as crianças do carro
print(cars)