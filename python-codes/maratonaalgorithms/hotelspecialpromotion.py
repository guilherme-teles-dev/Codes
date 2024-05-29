apartamentos = int(input())
diaria = float(input())
valorarrecadado = apartamentos*diaria*0.75
valordadiaria = diaria*0.75
print("Valor promocional da diária é: "+str(valordadiaria))
print("Valor total arrecadado para ocupação de 100%: "+str(valorarrecadado))
print("Valor arrecadado para ocupação de 70%: "+str(valorarrecadado*0.70))
print("Valor que foi descontado na ocupação 100%: "+str(apartamentos*diaria*0.25))