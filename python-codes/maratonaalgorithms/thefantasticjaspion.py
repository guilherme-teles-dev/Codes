traductioncount = int(input()) #input the wanted translate time.
for tries in range(traductioncount): #repete for the wanted times
    traduction, queries = map(int, input().split()) #input the time config
    dba = [traduction] #create a vector to save the word and the meaning in sequence.
    for meaning in range(traduction): #run the inputing of words and meanings.
        dba.append(input())
        dba.append(input())
    for c in range(queries):
        phrase = input().split()
        for translation in phrase:
            if translation in dba:
                print(dba[dba.index(translation)-1], end=' ')
            else:
                print(translation, end=" ")
        print()

