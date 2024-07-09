parent = 0
exp = str(input('Digite uma expressão: '))
for c in exp:
    if c == '(':
        parent += 1
    elif c == ')':
        parent -= 1
    if parent == -1:
        print('Expressão invalida! ')
        break
if parent == 0:
    print('Expressão valida! ')
elif parent >= 1:
    print('Expressão invalida! ')
