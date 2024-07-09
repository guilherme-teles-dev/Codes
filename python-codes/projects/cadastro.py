#Sistema de matrícula com persistência de arquivo
def Cadastrar(entidade, nome):
def Editar(entidade, edicao):
def Remover(entidade, nome):
def Listar(entidade):
def Matricular(aluno, disciplina):
def Relatorio(disciplina):
def Sair():

continuar = True
while continuar:
    print('-'*10)
    comando = int(input("""Seja bem vindo ao siscad, selecione a operação que deseja efetuar:
    1 - Cadastrar Aluno/Disciplina;
    2 - Editar Dados;
    3 - Remover Dados;
    4 - Listar Dados Armazenados;
    5 - Matricular Aluno;
    6 - Relatório de Disciplina
    7 - Sair
    Comando: """,end=''))
    if comando == 7:
        continuar == False
