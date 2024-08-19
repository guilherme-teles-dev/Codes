cases = int(input())
for c in range(cases):
    n = int(input())
    integers = list(map(int, input().split()))
    fightorder = []*len(integers)
    for line in range(n):
        x, y = map(int, input().split())
        if x > y:
            aux = x
            x = y
            y = aux
        if fightorder[line]
        