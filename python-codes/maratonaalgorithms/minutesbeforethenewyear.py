teste_cases = int(input())
for c in range(teste_cases):
    h, m = map(int, input().split())
    day = 24*60
    dayed = (h*60)+m
    finalminutes = day-dayed
    print(finalminutes)
