num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter pata Binario.
[ 2 ] converter para Octal.
[ 3 ] converter para Hexadecimal. ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para binario é igual a {bin(num)[2:]}. ')
elif opcao == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}. ')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}. ')
else:
    print(f'{opcao} não é uma opção valida! Tente novamente. ')
