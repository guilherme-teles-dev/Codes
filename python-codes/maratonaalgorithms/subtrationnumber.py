#Program expected input:
#Program expected output: "The subtraction 73-14 was 59."
#How we didn't expected any input, it's not necessary an input command.
#To start the program we need to create two variable to retain both 73 and 14.
number73 = "73"
number14 = "14"

dezena73 = int(number73[0])
unit73 = int(number73[1])
dezena14 = int(number14[0])
unit14 = int(number14[1])

resultunit = 0
resultdezena = 0

unit73 += 10
dezena73 -= 1

resultunit = unit73-unit14
resultdezena = dezena73-dezena14

print(f"The subtration result between 73 and 14 was {resultdezena}{resultunit}.")
    