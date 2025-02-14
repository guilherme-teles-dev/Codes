import json

# Nome do arquivo JSON de entrada
input_file = "competicoes_com_metadados.json"

# Nome do arquivo JSON de saída
output_file = "competicoes_com_metadados_modificado.json"

# Abrir e carregar o JSON de entrada
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Adicionar o campo "item_numero" a cada objeto
for index, item in enumerate(data, start=1):
    item["item_numero"] = f"item numero {index:04d}"

# Salvar o JSON modificado em um novo arquivo
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Arquivo '{output_file}' gerado com sucesso!")