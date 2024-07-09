valor = float(input('Digite o valor do produto: '))
pagamento = int(input('''Digite a forma de pagamento.
[1] - À vista. (10% de desconto).
[2] - Debito. (5% de desconto). 
[3] - Em até 2X no cartão.
[4] - 3X ou mais no cartão. (20% de juros).
Operação: '''))
if pagamento == 1:
    print(f'O valor do produto a ser pago à vista no dinheiro será de R${valor-(valor*10/100)}. ')
elif pagamento == 2:
    print(f'O valor do produto a ser pago à vista no cartão será de R%{valor-(valor*5/100)}. ')
elif pagamento == 3:
    parcela = int(input('Digite em quantas vezes deseja parcelar (1 ou 2): '))
    print(f'O valor de seu produto ficara em R${valor} e suas parcelas seram de R${valor/parcela}. ')
elif pagamento == 4:
    parcela = int(input('Digite em quantas vezes deseja parcelar: '))
    print(f'O valor de seu produto ficara em R${valor+(valor*20/100)} e suas parcelas seram de R${valor+(valor*20/100)/parcela}. ')
