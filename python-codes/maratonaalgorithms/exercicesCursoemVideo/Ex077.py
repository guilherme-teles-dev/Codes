palavras = ('Jogar', 'Vtuber', 'Programar', 'Vencer', 'Viajar')
for c in palavras:
    print(f'As vogais que aparecem em {c} são: ', end='')
    for a in c:
        if a.lower() in 'aeiou':
            print(a.lower(), end='')
    print()
