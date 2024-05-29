n = int(input())
coordinates = []
for item in range(n):
    x = int(input())
    y = int(input())
    coordinates.append([x, y])
print(coordinates)
for item in range(n):
    coordinates[item]