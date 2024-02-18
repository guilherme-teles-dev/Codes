##Say if the number can be a result for a sum of two even number.##
number = int(input()) #Here i'm taking the number from user
#Here i'm starting a coditioning block to verify the type of number.
if(number % 2 == 1): #Here i'm asking to the code to verify if the number can be a odd number.
    print('NO') 
elif(number == 2):#Here i'm asking to the code to verify if the number can be a number two, cuse the number two is only one number who can made by odd number.
    print('NO')
else: #If the number doesn't match with neither questions before, it's a valid number so can be made only by even numbers.
    print('YES')