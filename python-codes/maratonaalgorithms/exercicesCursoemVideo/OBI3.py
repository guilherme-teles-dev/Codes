from random import randint
erup = str(input())
t = int(erup.split()[0])
f = int(erup.split()[1])
q = []
s = 0
for l in range(0, t):
    for c in range(0, t):
        q.append(randint(1, 9))
for l in range(0, t):
    for c in range(0, t):
        if l == 0 and q[s] < f:
            q.insert(q[s], '*')
            q.pop(s+1)
            print(q[s], end='')
        elif q[s-t] == '*' and q[s] < f or q[s-1] == '*' and q[s] < f or q[s+1] == '*' and q[s] < f:
            q.insert(q[s], '*')
            q.pop(s+1)
            print(q[s], end='')
        else:
            print(q[s], end='')
        s += 1
    print()
        
