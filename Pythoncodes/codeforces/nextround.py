#The fist step to resolve this problem, like anyone, is to take the input from the user.
input1 = input().split() #Here, at same time we take an input and split the input in an array divide by the spaces.
#Here we will divide the input in variables to help us work with they separately
n = int(input1[0]) #We are putting the first number of the input in the variable n
k = int(input1[1]) #And the second one in the variable k
input2 = input().split() #Here we will do the same thing as the input1, recive and split at same time to gain time.
passed = 0 # We will start this variable to stroage the number of peoples who passes to the next round.
#Here we will run around the array who contain the points of the peoples and apply the exercice parameters to choose them.
for item in input2: #I said, for every item in input2(An array contaning the input of peoples points) do:
    if int(item) >= int(input2[k-1]) and int(item) != 0: #Here i use a condidional block to choose the peoples, i said: The peoples who passes is the peoples who have point equal or grater than the people in the k°position, and it point is diferent from 0
        passed += 1 #Here i increase the count of number of people who passes to the next round
print(passed) #Here i'm only write the answer and send a output.