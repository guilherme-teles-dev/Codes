frase = str(input('Digite uma frase: '))
print(f'Aparecem {frase.upper().count("A")} vezes a letra A nessa frase. ')
print(f'A letra A aparece pela primeira vez na posição {frase.upper().find("A") + 1}. ')
print(f'A letra A aparece pela ultima vez na posição {frase.upper().rfind("A") + 1}. ')
