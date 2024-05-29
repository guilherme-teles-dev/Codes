time1 = input().split(":")
time2 = input().split(":")
print(time1)
print(time2)
finalhour = int(time1[0]) + int(time2[0])
finalminute = int(time1[1]) + int(time2[1])
finalsec = int(time1[2]) + int(time2[2])
if(finalsec > 59):
    finalsec -= 60
    finalminute += 1
if(finalminute > 59):
    finalminute -= 60
    finalhour += 1

print(str(finalhour) + ":" + str(finalminute) + ":" + str(finalsec))
