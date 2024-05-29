#Input the number valors.
x = int(input())
y = int(input())
z = int(input())

#Create an auxiliar variable to help us swtich the number positions
aux = 0
#If x be bigger than y, switch x with y.
if x > y:
    aux = x
    x = y
    y = aux
#If y be bigger than z, switch y with z
if y > z:
    aux = y
    y = z
    z = aux
#Check the comparation between x and y. 
if x > y:
    aux = x
    x = y
    y = aux
    
#Output
print(x, y, z)