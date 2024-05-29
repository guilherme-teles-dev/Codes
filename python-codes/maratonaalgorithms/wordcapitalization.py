input = input()
capitalized = []
capitalized.append(input.capitalize()[0])
for c in range(1, len(input)):
    capitalized.append(input[c])
separador = ''
capitalized = separador.join(capitalized)
print(capitalized)