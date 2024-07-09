primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = primeiro
for c in range (1, 11):
    print(primeiro+c*razao)
