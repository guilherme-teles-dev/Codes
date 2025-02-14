# Instale a biblioteca
# pip install pdfplumber

import pdfplumber

def extract_text_with_pdfplumber(pdf_path, output_txt="texto_extraido.txt"):
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        
        with open(output_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
        
        return "Texto extraído com sucesso!"
    
    except Exception as e:
        return f"Erro: {str(e)}"

# Uso
result = extract_text_with_pdfplumber("/home/guilherme/Documents/Apostilas Gran Cursos/Computação na Nuvem, Containeres e Devops/Infraestrutura como código.pdf")
print(result)