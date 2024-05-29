cases = int(input()) #Vai contar quanto tempo temos para nos movimentar
line1 = input().split() #Vai servir de referencia de distância do quarto das crianças
line2 = input().split() #Vai servir para definir a prioridade das crianças
outputed = 0 #Vai servir para contar quanto tempo passou
ultima_crianca = 0 #Vai servir para guardar qual foi a ultima criança atendida
proxima_crianca = 0 #Vai servir para guardar qual é a proxima criança que vai ser atendida
while(outputed < cases): #Vai fazer o tempo passar
    proxima_crianca = line1.index(line2[ultima_crianca])+1 #Vai nos devolver o objetivo do momento.
    distancia_entre_criancas = abs(proxima_crianca-ultima_crianca)#Vai nos devolver a distância do objetivo que temos no momento e a distância atual.
    tempo_de_objetivo = (line2[outputed]+' ')*distancia_entre_criancas #Vai montar o quantas crianças conseguimos atender nesse momento.
    print(tempo_de_objetivo) #Vai imprimir o que foi feito no determinado segundo
    ultima_crianca = proxima_crianca#Vai listas a criança como atendendida
    outputed += distancia_entre_criancas-1 #Vai contar a passagem de tempo para atender a criança
    proxima_crianca += 1 #Vai trocar o objetivo.

