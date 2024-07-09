alunos = []
while True:
    aluno = []
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno)
    r = str(input('Deseja continuar? (S/N) '))
    while r not in 'SsnN':
        r = str(input('Opção invalida, digite uma opção valida: (S/N) '))
    if r in 'Nn':
        break
print(f'{"No.":<4}{"Nome":<10}{"MÉDIA":>8}')
for c, v in enumerate(alunos):
    print(f'{c:<4} {v[0]:<10} {(v[1]+v[2])/2:>5}')
while True:
    n = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    else:
        print(f'As notas do aluno {alunos[n][0]} são {alunos[n][1]} e {alunos[n][2]}')
