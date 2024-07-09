frase = str(input('Digite uma frase: '))
frasesemespaco = frase.upper().split()
frasesemespaco = ''.join(frasesemespaco)
cfrase = frasesemespaco[::-1]
if frasesemespaco == cfrase:
    print(f'''A frase:
{frase}
É um palíndromo! ''')
else:
    print(f'''A frase:
{frase}
Não é um palindromo! ''')
