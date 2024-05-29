#Function to compare two string and return the lower.
def lowweightword(word1, word2): #Input a string as a parameter
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    weight1 = 0
    weight2 = 0
    for c in range(len(word1)):
        if(word1[c] != word2[c]):
            weight1 = alphabet.index(word1[c])+1
            weight2 = alphabet.index(word2[c])+1
            break
    if(weight1 > weight2):
        return word2
    else:
        return word1
#Number of cases who will be input
numberoftestescases = int(input())
cases = []
#Looping to recibe the cases
for case in range(numberoftestescases):
    #Input the case parameters
    firstline = input().split() #Invite to firstline variable an input splited from keyboard.
    #Split the cases in n and m variables
    n = int(firstline[0]) #n variable will be the number of processable itens. 
    m = int(firstline[1]) #m number will be the number of B characters
    #Input the case process material
    secondline = input().split() #Here will be inputed the number who's we will use to replace the B characters by A.
    #Case process
    momentcase1 = [] #Here we will create an array to stroage our output case.
    momentcase2 = []
    for item in range(m): #Looping to input all the B latters in the moment case
        momentcase1.append('B') #Input B characters in the moment case type 1
        momentcase2.append('B') #Input B characters in the moment case type 2
    item = 0 #Check if item it's 0
    for item in secondline: #Start a looping to edit both cases types
        momentcase1[int(item)-1] = 'A'
        momentcase2[m+1-int(item)-1] = 'A'
    #Case output
    momentcase1 = ''.join(momentcase1) #Join the latters in this case
    momentcase2 = ''.join(momentcase2) #Join the latters in this case
    cases.append(lowweightword(momentcase1, momentcase2))
for thing in cases:
    print(thing)
