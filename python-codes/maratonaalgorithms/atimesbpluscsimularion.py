a = int(input("Type the first number: "))
b = int(input("Type the second number: "))
c = int(input("Type the tird number: "))

multiplicationresult = 0
sumresult = 0

for tries in range(0, b):
    multiplicationresult += a
    print(multiplicationresult)
    
sumresult = multiplicationresult + c

print(f"The equation result was {sumresult}.")