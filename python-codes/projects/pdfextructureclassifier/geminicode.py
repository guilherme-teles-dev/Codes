import os
from pdfminer.high_level import extract_pages
from pdfminer.image import Image as PDFImage
from pdfminer.layout import LTTextContainer, LTChar
from PIL import Image
import cv2
import numpy as np

def separar_pdf_por_cor(pasta_pdfs, pasta_output_raiz):
    """
    Processa PDFs em uma pasta, detecta cores e separa o texto por cor em pastas diferentes.

    Args:
        pasta_pdfs (str): Caminho para a pasta contendo os arquivos PDF.
        pasta_output_raiz (str): Caminho para a pasta raiz onde as pastas de saída serão criadas.
    """

    cores_detectadas = set()  # Para rastrear as cores detectadas e criar pastas dinamicamente

    # 1. Criar pasta de output raiz se não existir
    if not os.path.exists(pasta_output_raiz):
        os.makedirs(pasta_output_raiz)

    for nome_arquivo in os.listdir(pasta_pdfs):
        if nome_arquivo.lower().endswith(".pdf"):
            caminho_pdf = os.path.join(pasta_pdfs, nome_arquivo)
            print(f"Processando arquivo: {nome_arquivo}")

            # 2. Converter primeira página do PDF para imagem usando pdfminer e Pillow
            for page_layout in extract_pages(caminho_pdf, maxpages=1): # Processa apenas a primeira página para exemplo
                for element in page_layout:
                    if isinstance(element, PDFImage):
                        try:
                            image_data = element.stream.get_rawdata()
                            if element.name.lower().endswith(('.jpg', '.jpeg')):
                                image = Image.open(io.BytesIO(image_data))
                            elif element.name.lower().endswith('.png'):
                                image = Image.open(io.BytesIO(image_data))
                            else:
                                continue # Ignora outros tipos de imagem por simplicidade

                            imagem_np = np.array(image)
                            imagem_cv = cv2.cvtColor(imagem_np, cv2.COLOR_RGB2BGR) # Converte para BGR para OpenCV

                        except Exception as e:
                            print(f"Erro ao processar imagem dentro do PDF: {e}")
                            continue
                        break # Processa a primeira imagem encontrada e sai do loop de elementos da página
                else: # Se o loop for page_layout terminar sem 'break', significa que não achou imagem na primeira página
                    print(f"Nenhuma imagem vetorial encontrada na primeira página de {nome_arquivo}, pulando detecção de cores.")
                    continue # Pula para o próximo PDF se não houver imagem vetorial na primeira página

                if imagem_cv is None: # Verifica se imagem_cv foi carregada corretamente
                    print(f"Falha ao carregar imagem para detecção de cores em {nome_arquivo}, pulando detecção de cores.")
                    continue


                # 3. Detecção de cores na imagem usando OpenCV
                # *** Defina aqui as faixas de cor HSV que você deseja detectar ***
                limites_cores = {
                    "azul": ([100, 50, 50], [130, 255, 255]),  # Exemplo de faixa HSV para azul
                    "amarelo": ([20, 100, 100], [40, 255, 255]), # Exemplo de faixa HSV para amarelo
                    "vermelho": ([0, 100, 100], [10, 255, 255]), # Exemplo de faixa HSV para vermelho (tom baixo)
                    "vermelho2": ([170, 100, 100], [180, 255, 255]), # Exemplo de faixa HSV para vermelho (tom alto - para cobrir a faixa circular do HSV)
                    "verde": ([40, 40, 40], [80, 255, 255]),     # Exemplo de faixa HSV para verde
                    "roxo": ([130, 50, 50], [170, 255, 255])    # Exemplo de faixa HSV para roxo
                    # Adicione mais faixas de cores conforme necessário
                }

                hsv_imagem = cv2.cvtColor(imagem_cv, cv2.COLOR_BGR2HSV)

                textos_por_cor = {} # Dicionário para armazenar texto por cor

                for cor_nome, (limite_inferior_hsv, limite_superior_hsv) in limites_cores.items():
                    limite_inferior = np.array(limite_inferior_hsv, dtype=np.uint8)
                    limite_superior = np.array(limite_superior_hsv, dtype=np.uint8)

                    mascara_cor = cv2.inRange(hsv_imagem, limite_inferior, limite_superior)
                    # mascara_cor agora é uma imagem binária onde branco são os pixels na faixa de cor

                    # *** Extração de texto da região colorida (simplificado) ***
                    # Aqui, para simplificar, vamos assumir que *todo* o texto da página
                    # pertence à cor detectada se *algum* pixel da imagem da página
                    # estiver dentro da máscara de cor.
                    # Em um cenário real, você precisaria de uma lógica mais precisa para
                    # associar regiões de cor *específicas* a blocos de texto *correspondentes* no PDF.

                    if cv2.countNonZero(mascara_cor) > 0: # Se encontrou pixels da cor
                        cores_detectadas.add(cor_nome)
                        textos_por_cor[cor_nome] = "" # Inicializa para acumular texto (se fosse extrair texto de verdade)
                        print(f"  Cor '{cor_nome}' detectada em {nome_arquivo}.")


                # 4. Extrair texto do PDF (usando pdfminer novamente, mas agora para *extrair o texto todo* - simplificado)
                texto_completo_pdf = ""
                for page_layout in extract_pages(caminho_pdf):
                    for element in page_layout:
                        if isinstance(element, LTTextContainer):
                            texto_completo_pdf += element.get_text()


                # 5. Salvar texto em pastas separadas por cor (simplificado - salva o PDF inteiro em cada pasta de cor detectada)
                for cor_nome in textos_por_cor.keys(): # Itera sobre as cores que foram *detectadas* no PDF
                    pasta_cor = os.path.join(pasta_output_raiz, f"texto_{cor_nome}")
                    if not os.path.exists(pasta_cor):
                        os.makedirs(pasta_cor)
                    caminho_output_pdf = os.path.join(pasta_cor, f"{nome_arquivo}")

                    # *** Aqui, em vez de salvar *apenas o texto da cor*, vamos salvar
                    #     uma *cópia do PDF inteiro* em cada pasta de cor detectada,
                    #     já que a extração de texto *segmentado por cor* é mais complexa
                    #     e está simplificada neste exemplo. ***
                    try:
                        with open(caminho_pdf, 'rb') as f_pdf_original, open(caminho_output_pdf, 'wb') as f_pdf_output:
                            f_pdf_output.write(f_pdf_original.read())
                        print(f"  PDF copiado para pasta '{pasta_cor}'.")
                    except Exception as e:
                        print(f"  Erro ao copiar PDF para '{pasta_cor}': {e}")


    print("\nProcessamento completo.")
    print("Cores detectadas em todos os PDFs processados:", cores_detectadas)
    print("Pastas de saída criadas em:", pasta_output_raiz)


# *** Defina os caminhos das pastas aqui: ***
pasta_pdfs_input = "pdfs_para_extracao" # Pasta onde seus PDFs de entrada estão
pasta_output_raiz_principal = "pdfs_processados_por_cor" # Pasta raiz para as pastas de saída coloridas

# *** Certifique-se de que a pasta de entrada 'pdfs_para_extracao' exista e contenha seus PDFs ***
if not os.path.exists(pasta_pdfs_input):
    print(f"Erro: Pasta de entrada '{pasta_pdfs_input}' não encontrada. Crie a pasta e coloque os PDFs lá.")
else:
    separar_pdf_por_cor(pasta_pdfs_input, pasta_output_raiz_principal)