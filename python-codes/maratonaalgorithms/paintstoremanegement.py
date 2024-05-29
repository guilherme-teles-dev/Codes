from math import ceil
paintingarea = float(input("Digite o tamanho da área que será pintada: "))
#1 litro pinta 3 metros quadrados.
#Existem latas de 18 litro(80) e de 3,6litros(25)
latas = ceil(paintingarea/18)
precolatas = latas*80
galoes = ceil(paintingarea/3.6)
precogaloes = galoes*25
latas = str(latas)
precolatas = str(precolatas)
galoes = str(galoes)
precogaloes= str(precogaloes)
print("Você precisaria de "+latas+" latas de tinta. E ficaria R$"+precolatas+" reais.")
print("Você precisaria de "+galoes+" galões de tinta. E ficaria R$"+precogaloes+" reais.")
latas = paintingarea//18
galoes = ceil((paintingarea%18)/3.6)
precototal = str((latas*80)+(galoes*25))
latas = str(latas)
galoes = str(galoes)
print("Caso comprar queira comprar tanto galões quanto latas dará "+precototal+" e você precisará de "+latas+" latas e "+galoes+" galões.")