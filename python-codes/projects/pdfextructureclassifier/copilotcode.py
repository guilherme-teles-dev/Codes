import os
import shutil
from pdf2image import convert_from_path
import cv2
import pytesseract
from PIL import Image

# Configuração do caminho do Tesseract, se necessário
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Diretórios
input_dir = 'pdfs_para_extracao'
output_dir_azul = 'texto_azul'
output_dir_amarelo = 'texto_amarelo'

# Criar diretórios de saída, se não existirem
os.makedirs(output_dir_azul, exist_ok=True)
os.makedirs(output_dir_amarelo, exist_ok=True)

# Loop através de todos os arquivos PDF na pasta de entrada
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(input_dir, filename)

        # Converter primeira página do PDF em imagem
        images = convert_from_path(pdf_path, dpi=300)
        image = images[0]  # Considerando que cada PDF tem uma página

        # Salvar imagem temporariamente
        temp_image_path = 'temp_image.png'
        image.save(temp_image_path, 'PNG')

        # Ler imagem com OpenCV
        img = cv2.imread(temp_image_path)

        # Converter para espaço de cores HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Definir faixas de cores para azul e amarelo (ajuste conforme necessário)
        # Azul
        lower_blue = (100, 150, 0)
        upper_blue = (140, 255, 255)

        # Amarelo
        lower_yellow = (20, 100, 100)
        upper_yellow = (30, 255, 255)

        # Criar máscara para regiões azuis
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        result_blue = cv2.bitwise_and(img, img, mask=mask_blue)

        # Criar máscara para regiões amarelas
        mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
        result_yellow = cv2.bitwise_and(img, img, mask=mask_yellow)

        # Salvar imagens temporárias das regiões extraídas
        blue_region_path = 'temp_blue.png'
        yellow_region_path = 'temp_yellow.png'
        cv2.imwrite(blue_region_path, result_blue)
        cv2.imwrite(yellow_region_path, result_yellow)

        # Realizar OCR nas imagens das regiões
        text_blue = pytesseract.image_to_string(Image.open(blue_region_path), lang='por')
        text_yellow = pytesseract.image_to_string(Image.open(yellow_region_path), lang='por')

        # Se houver texto extraído, salvar em PDF nas pastas correspondentes
        if text_blue.strip():
            output_file_blue = os.path.join(output_dir_azul, f"{os.path.splitext(filename)[0]}_azul.pdf")
            # Salvar texto em PDF (usando Pillow)
            image_blue = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
            cv2.imwrite('temp_text_image.png', cv2.cvtColor(result_blue, cv2.COLOR_BGR2RGB))
            image_blue.paste(Image.open('temp_text_image.png'))
            image_blue.save(output_file_blue, "PDF", resolution=100.0)

        if text_yellow.strip():
            output_file_yellow = os.path.join(output_dir_amarelo, f"{os.path.splitext(filename)[0]}_amarelo.pdf")
            # Salvar texto em PDF (usando Pillow)
            image_yellow = Image.new('RGB', (1000, 1000), color=(255, 255, 255))
            cv2.imwrite('temp_text_image.png', cv2.cvtColor(result_yellow, cv2.COLOR_BGR2RGB))
            image_yellow.paste(Image.open('temp_text_image.png'))
            image_yellow.save(output_file_yellow, "PDF", resolution=100.0)

        # Remover arquivos temporários
        os.remove(temp_image_path)
        os.remove(blue_region_path)
        os.remove(yellow_region_path)
        if os.path.exists('temp_text_image.png'):
            os.remove('temp_text_image.png')

print("Processamento concluído!")
