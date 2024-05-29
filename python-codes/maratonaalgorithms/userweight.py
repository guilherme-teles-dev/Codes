userweight = float(input())
userheight = float(input())
imc = userweight/(userheight*userheight)
if(imc <= 20):
    print("Sobrepeso.")
elif(imc > 20 and imc < 25):
    print("Peso normal.")
elif(imc >= 25 and imc < 30):
    print("Sobre peso.")
elif(imc >= 30 and imc < 40):
    print("Obeso.")
else:
    print("Thais Carla.")