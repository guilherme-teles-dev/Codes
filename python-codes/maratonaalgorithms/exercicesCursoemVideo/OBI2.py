premiados = int(input())
camisetas = str(input())
p = int(input())
m = int(input())
np = camisetas.count('1')
nm = camisetas.count('2')
if np >= p and nm >= m:
    print('S')
else:
    print('N')
