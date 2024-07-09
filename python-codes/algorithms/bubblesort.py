#Algoritmo de ordenação com tempo de execução n² que atua comparando termos adjacentes.
def bubbleSort(array): #Define uma função para ordenação pelo método bubble.
    
    tamanho_do_vetor = len(array) #Cria uma variável com o tamanho do vetor que irá ser ordenado.

    for navegador in range(tamanho_do_vetor): #Cria um looping que irá repetir pelo tamanho do vetor.
        x = tamanho_do_vetor - navegador - 1
        for j in range(0, x): #Cria outro looping que irá repetir por um tempo que decrescerá com um passo de i
            proximo_vetor = j+1
            if arr[j] > arr[proximo_vetor]: #Cria uma condicional que verifica se arr na posição j 
                arr[j], arr[proximo_vetor] = arr[proximo_vetor], arr[j]

array = list(map(int, input().split()))
bubbleSort(array)

print("Sorted array is:")
for navegador in range(len(array)):
    print("%d" % arr[navegador])
