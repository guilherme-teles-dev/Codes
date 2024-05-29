number = int(input("Type the number: "))

square = number
for c in range(0, 1):
    square *= number

cube = number
for c in range(0, 2):
    cube *= number
    
print(f"{square}, {cube}.")