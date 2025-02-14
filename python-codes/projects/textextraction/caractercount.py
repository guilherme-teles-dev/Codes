# Nome do arquivo de texto
input_file = ""

# Abrir o arquivo e contar os caracteres
try:
    with open(input_file, "r", encoding="utf-8") as f:
        conteudo = f.read()  # Lê todo o conteúdo do arquivo
        total_caracteres = len(conteudo)  # Conta o número de caracteres
        print(f"O arquivo '{input_file}' contém {total_caracteres} caracteres (incluindo espaços).")
except FileNotFoundError:
    print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")