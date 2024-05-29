tables = int(input())
color = input()
neighboors = 0
for c in range(1, tables):
    if color[c] == color[c-1]:
        neighboors += 1
print(neighboors)