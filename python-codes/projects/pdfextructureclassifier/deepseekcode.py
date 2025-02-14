import fitz  # PyMuPDF
import cv2
import numpy as np
import os
import shutil
from PIL import Image

# Configurações
input_folder = "pdfs_para_extracao"
output_folders = {
    "azul": "texto_azul",
    "amarelo": "texto_amarelo"
}

# Cria pastas de saída
for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

# Limiares de cores em HSV (ajuste conforme necessário)
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Renderizar página como imagem
        pix = page.get_pixmap(dpi=200)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_np = np.array(img)
        hsv = cv2.cvtColor(img_np, cv2.COLOR_RGB2HSV)
        
        # Detectar regiões azuis e amarelas
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        # Encontrar contornos das regiões
        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Extrair texto das regiões
        for color, contours in [("azul", contours_blue), ("amarelo", contours_yellow)]:
            output_folder = output_folders[color]
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                # Converter coordenadas da imagem para o sistema do PDF
                scale_x = page.rect.width / pix.width
                scale_y = page.rect.height / pix.height
                pdf_rect = fitz.Rect(
                    x * scale_x,
                    (pix.height - y - h) * scale_y,  # Inverter eixo Y
                    (x + w) * scale_x,
                    (pix.height - y) * scale_y
                )
                # Extrair texto dentro da região
                texto = page.get_text("text", clip=pdf_rect)
                if texto.strip():
                    # Salvar em novo PDF
                    new_doc = fitz.open()
                    new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)
                    new_page.insert_text((10, 10), texto)  # Posição fixa (ajuste conforme necessário)
                    output_path = os.path.join(
                        output_folder,
                        f"{os.path.splitext(os.path.basename(pdf_path))[0]}_pag{page_num}_{color}.pdf"
                    )
                    new_doc.save(output_path)
                    new_doc.close()

# Processar todos os PDFs na pasta
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        process_pdf(os.path.join(input_folder, filename))

print("Processamento concluído!")