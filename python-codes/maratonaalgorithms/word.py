input = input()
loweralphabet = "abcdefghijklmnopqrstuvxwyz"
lowerlatters = 0
upperlatters = 0
for c in input:
    if c in loweralphabet:
        lowerlatters += 1
    else:
        upperlatters += 1
if(lowerlatters >= upperlatters):
    print(input.lower())
else:
    print(input.upper())