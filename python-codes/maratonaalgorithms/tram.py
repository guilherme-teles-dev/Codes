tramstop = int(input())
traincapacity = 0
peoplesintrain = 0
for count in range(tramstop): #Each loop is a train stop information
    station = input()
    number1 = int(station.split()[0])
    number2 = int(station.split()[1])
    peoplesintrain -= number1
    peoplesintrain += number2
    if peoplesintrain > traincapacity:
        traincapacity = peoplesintrain
print(traincapacity)
