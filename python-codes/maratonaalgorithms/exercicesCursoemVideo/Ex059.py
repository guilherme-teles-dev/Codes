resposta = 0
while resposta != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('''Digite:
[ 1 ] - Para somar.
[ 2 ] - Para multiplicar.
[ 3 ] - Para ver qual é o maior.
[ 4 ] - Para inserir novos numeros.
[ 5 ] - Para sair do programa. ''')
    resposta = int(input('Digite o numero da operação: '))
    if resposta == 1:
        print(f'A soma entre {n1} e {n2} é igual a: {n1+n2} ')
    elif resposta == 2:
        print(f'O produto da multiplicação entre {n1} e {n2} é igual a: {n1*n2} ')
    elif resposta == 3:
        if n1 > n2:
            print(f'O maior numero entre {n1} e {n2} é igual a: {n1} ')
        else:
            print(f'O maior numero entre {n1} e {n2} é igual a: {n2} ')
