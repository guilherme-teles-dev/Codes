#binary search
#math
#*1300
for t in range(int(input())): #here is inputed an range at same time the looping structure declaration
    a, b = map(int, input().split()) #here is inputed the instance variables at same time.
    if a > b: #here we organize the variables by size
        a, b = b, a
    print ("YES" if(((a+b)%3)==0 and a * 2 >= b) else "NO") #our output are make around an coditional structure to optimize the code.
