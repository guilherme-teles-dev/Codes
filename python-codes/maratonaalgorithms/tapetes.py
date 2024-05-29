tubesize, matcount = map(int, input().split())
#the output will be the bigger area possible
final = tubesize + 1
final = final - matcount
final = final*final
final = final + matcount-1
print(final)
