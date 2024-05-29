productprice = float(input())
if(productprice <= 50):
    productprice *= 1.05
elif(productprice > 50 and productprice < 100):
    productprice *= 1.1
else:
    productprice *= 1.15

print(productprice, end=" ")
if(productprice <= 80):
    print("Barato.")
elif(productprice > 80 and productprice <= 120):
    print("Normal.")
elif(productprice < 120 and productprice <= 200):
    print("Caro.")
else:
    print("Muito caro.")