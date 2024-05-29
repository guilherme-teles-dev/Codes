numberoflines = int(input())
matrix = [[],[],[]]
numbers = input().split(" ")
matrix[0].append(int(numbers[0]))
matrix[1].append(int(numbers[1]))
matrix[2].append(int(numbers[2]))
if(numberoflines > 1):
    for c in range(1, numberoflines):
        numbers = input().split(" ")
        matrix[0].append(matrix[0][c-1] + int(numbers[0]))
        matrix[1].append(matrix[1][c-1] + int(numbers[1]))
        matrix[2].append(matrix[2][c-1] + int(numbers[2]))
if(matrix[0][numberoflines-1] == 0 and matrix[1][numberoflines-1] == 0 and matrix[2][numberoflines-1] == 0):
    print("YES")
else:
    print("NO")