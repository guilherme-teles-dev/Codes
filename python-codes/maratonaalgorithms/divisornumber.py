number = int(input())
if(number%10==0):
    print("The number can be divide by 10")
if(number%5==0):
    print("The number can be divide by 5")
if(number%2==0):
    print("The number can be divide by 2")
if(number%2!=0 and number%5!=0 and number%10!=0):
    print("The number can't be divide by any number")