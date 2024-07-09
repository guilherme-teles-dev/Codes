r = 's'
primeirot = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da sua PA: '))
c = 0
PA = primeirot
while c < 10:
    print(PA + c*razao)
    c += 1
    primeirot = PA + c*razao
r = str(input('Deseja continuar? (S/N) ')).lower()
if r != 'n':
    while r != 'n':
        c = 0
        t = int(input('Desenha saber mais quantos termos? '))
        PA = primeirot
        while c < t:
            print(PA + razao*c)
            c += 1
            primeirot = PA + c*razao
        r = str(input('Deseja continuar? (S/N) ')).lower()
        
