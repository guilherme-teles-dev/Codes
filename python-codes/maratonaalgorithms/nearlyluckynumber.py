n = input()
answer = ''
for c in n:
    if len(n) == 1:
        answer = 'NO'
        break
    elif c != "4" and c!="7":
        answer = 'NO'
        break
    else:
        answer = 'YES'
print(answer)