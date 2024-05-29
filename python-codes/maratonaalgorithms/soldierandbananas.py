input = input().split()
costofirst = int(input[0])
initialnumberofdolar = int(input[1])
banananumbers = int(input[2])
totalprice = 0
for c in range(1, banananumbers+1):
    totalprice += c*costofirst
finalprice = totalprice-initialnumberofdolar
if(finalprice <= 0):
    print(0)
else:
    print(finalprice)