#The propose of this problem is make a algorithm who can calculate how many dominos with size 2x1 can be placed in maximum in a square mxn.
input = input().split() #Like ever, starts take the input from the user and split them in a array
#After, we can divide this array in two variables and inform the nature integer.
m = int(input[0])
n = int(input[1])
#Here we can show the output finding the square area and divide them by the dominos's area, the result we can transform in integer (That's come in decimal number) and with this, we ignore the fraction part.
print(int((m*n)/2))