##Software who can abreviate the long words.##
##The rule is, if the word is bigger than 10 characteres, put the first letter, a number o letters between the first and last, and the last latter.##
words = int(input()) #Here we are catching from the user the number of words where he want to write.
array = [] #Here we are declaring the array who will recive the words.
for c in range(words): #We start a loop to input multiples letters in the array.
    word = input() #In there we are asking to the user to an input.
    array.append(word) #Here we are putting this input in out array.
#After catch all the words from the user we starts a looping to run by the array and excecute the operarion of write and abreviate.
for word in array: #The looping config why we choose is this, with this we can do a looping item by item and operate him once a one.
    if len(word) <= 10: #Starting a conditional block we can verify if the word's letters is bigger than 10.
        print(word) #If is not, we can print
    else: #If is, we abreviate.
        print(f'{word[0]}{len(word)-2}{word[len(word)-1]}')