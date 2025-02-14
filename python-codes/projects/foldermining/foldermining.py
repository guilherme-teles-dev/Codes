import os
from pathlib import Path

def simplificar_estrutura(caminho_pasta, arquivo_saida, ignorar=[], max_profundidade=6):
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for raiz, dirs, arquivos in os.walk(caminho_pasta):
            # Filtra diretórios e arquivos a ignorar
            dirs[:] = [d for d in dirs if d not in ignorar]
            arquivos = [a for a in arquivos if a not in ignorar]
            
            caminho_rel = Path(raiz).relative_to(caminho_pasta)
            partes = caminho_rel.parts
            
            if len(partes) > max_profundidade:
                continue
                
            indentacao = '│   ' * (len(partes) - 1)
            
            if partes:
                f.write(f'{indentacao}├── {partes[-1]}/\n')
            else:
                f.write(f'.\n')
            
            for idx, arquivo in enumerate(arquivos):
                ultimo = idx == len(arquivos) - 1
                ramificacao = '└── ' if ultimo else '├── '
                f.write(f'{indentacao}{ramificacao}{arquivo}\n')

if __name__ == "__main__":
    pasta = "/home/guilherme/Documentos/projects/dipemax"
    saida = 'estrutura_simplificada.txt'
    
    pastas_ignorar = {
        'node_modules', '.git', '.next', 'dist', 'build',
        '__pycache__', '.idea', 'venv', 'cache', 'logs'
    }
    
    simplificar_estrutura(
        caminho_pasta=pasta,
        arquivo_saida=saida,
        ignorar=pastas_ignorar,
        max_profundidade=8
    )
    
    print(f'Estrutura simplificada salva em {saida}')