import os
import cv2
import numpy as np
from pdf2image import convert_from_path
from PIL import Image

# Diretórios de entrada e saída
pdf_dir = "pdfs_para_extracao"
output_blue = "texto_azul"
output_yellow = "texto_amarelo"

# Cria as pastas de saída se não existirem
os.makedirs(output_blue, exist_ok=True)
os.makedirs(output_yellow, exist_ok=True)

# Define os intervalos de cor em HSV para azul e amarelo
blue_lower = np.array([100, 150, 0])
blue_upper = np.array([140, 255, 255])

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

# Loop para processar todos os arquivos PDF da pasta
for filename in os.listdir(pdf_dir):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        print(f"Processando: {pdf_path}")
        
        # Converte o PDF em imagem (assumindo que cada PDF tem uma única página)
        pages = convert_from_path(pdf_path, dpi=200)
        
        if pages:
            page_image = pages[0]  # Pega a única página
            # Converte a imagem do PIL para formato OpenCV
            open_cv_image = cv2.cvtColor(np.array(page_image), cv2.COLOR_RGB2BGR)
            
            # Converte a imagem para o espaço de cores HSV
            hsv = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2HSV)
            
            # Cria máscaras para as cores azul e amarelo
            mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)
            mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
            
            # Detecta os contornos das regiões azuis
            contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours_blue:
                x, y, w, h = cv2.boundingRect(cnt)
                # Filtra regiões pequenas para evitar ruídos (ajuste o valor se necessário)
                if w * h > 1000:
                    cropped_blue = open_cv_image[y:y+h, x:x+w]
                    # Converte a região recortada para imagem PIL
                    cropped_pil = Image.fromarray(cv2.cvtColor(cropped_blue, cv2.COLOR_BGR2RGB))
                    # Define o caminho do arquivo de saída
                    output_path = os.path.join(output_blue, f"{os.path.splitext(filename)[0]}_blue_{x}_{y}.pdf")
                    cropped_pil.save(output_path, "PDF", resolution=100.0)
                    print(f"Salvo: {output_path}")
            
            # Detecta os contornos das regiões amarelas
            contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours_yellow:
                x, y, w, h = cv2.boundingRect(cnt)
                if w * h > 1000:
                    cropped_yellow = open_cv_image[y:y+h, x:x+w]
                    cropped_pil = Image.fromarray(cv2.cvtColor(cropped_yellow, cv2.COLOR_BGR2RGB))
                    output_path = os.path.join(output_yellow, f"{os.path.splitext(filename)[0]}_yellow_{x}_{y}.pdf")
                    cropped_pil.save(output_path, "PDF", resolution=100.0)
                    print(f"Salvo: {output_path}")
        else:
            print(f"Falha ao converter {pdf_path}")
