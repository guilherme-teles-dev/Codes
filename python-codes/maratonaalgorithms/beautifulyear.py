number = input()
number = int(number)+1
number = str(number)
number = [*number]
while len(set(number)) != len(number):
    number = ''.join(number)
    actualnumber = int(number)
    actualnumber += 1
    number = str(actualnumber)
    number = [*number]
number = ''.join(number)
print(number)
