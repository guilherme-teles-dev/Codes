times = ('Bragantino', 'Bahia', 'Ceará SC', 'Fortaleza', 'Athletico-PR', 'Flamengo',
         'Atlético-GO', 'Sport Recife', 'Juventude', 'Cuiabá', 'Internacional',
         'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG',
         'Palmeiras', 'Corinthians', 'Chapecoense', 'Santos')
print(f'Os times são: {times}')
print(f'Os 5 primeiros são {times[:5]}')
print(f'Os 4 ultimos são {times[16:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f"O time Chapecoense está em {times.index('Chapecoense')+1}°")
