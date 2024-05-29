#Algorithm to add or subtrate 1 unit to zero using text.
variable = 0 #For first we declare the variable who will be operating
statements = int(input()) #Second we recive from the user the number of statements who will be inputed
for count in range(0, statements): #Doing a loop to take the inputs of statements
    answer = str(input()) #Take the statements
    if '++' in answer: #Verifying the type of operation (sum the unit or subtract the unit)
        variable += 1 #Sum the unit
    else: #If the statement do not contain ++ the operation means subtraction
        variable -= 1 #Subtract the unit
print(variable) #Show the code's output.