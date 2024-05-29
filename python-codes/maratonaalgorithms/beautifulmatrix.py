from math import fabs
matrix = []
positionnumber = []
for line in range(0, 5):
    l = input().split()
    if '1' in l:
        positionnumber.append(line+1)
        positionnumber.append(l.index('1')+1) 
    matrix.append(l)
moves = fabs(positionnumber[0]-3)+fabs(positionnumber[1]-3)
print(int(moves))
