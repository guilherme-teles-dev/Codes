from math import ceil #Import a command to round to next necessarynumber
a, b, c = map(int, input().split()) #Input the necessary variables
necessarycoffee = (c/1000)*a #Measure how much coffee the students will drink
doescoffee = ceil(necessarycoffee/b)
doescoffee *= b
print(doescoffee) 
