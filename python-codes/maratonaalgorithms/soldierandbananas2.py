userinput = input().split()
firstbanana = int(userinput[0])
money = int(userinput[1])
numberofbananas = int(userinput[2])
finalmoney = int((((1+numberofbananas)/2)*numberofbananas)*firstbanana-money)
if(finalmoney <= 0):
    print(0)
else:
    print(finalmoney)