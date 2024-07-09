cidade = str(input('Digite o nome da cidade: '))
corte = cidade.upper().split()
comeco = "SANTO" in corte[0]
print(f'A cidade começa com Santo: {comeco} ')
