from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Configuração do navegador
download_path = os.path.join(os.getcwd(), "concursomining/editais")  # Define o diretório para salvar os editais
os.makedirs(download_path, exist_ok=True)  # Cria o diretório, se não existir

options = Options()
prefs = {"download.default_directory": download_path}
options.add_experimental_option("prefs", prefs)

# Inicialização do WebDriver com o WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Acessa a página de concursos e seleções
    url = "https://www.in.gov.br/acesso-a-informacao/institucional/concursos-e-selecoes"
    driver.get(url)

    # Aguarda o carregamento da página
    time.sleep(5)

    # Localiza os links dos editais
    editais = driver.find_elements(By.XPATH, "//a[contains(@href, '/web/dou/-/')]")
    links = [edital.get_attribute("href") for edital in editais]

    if not links:
        print("Nenhum edital encontrado.")
    else:
        print(f"Encontrados {len(links)} editais. Iniciando download...")

    # Faz o download dos editais
    for i, link in enumerate(links, start=1):
        driver.get(link)
        time.sleep(3)  # Ajuste o tempo conforme necessário
        print(f"Edital {i} baixado: {link}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    driver.quit()
    print(f"Editais salvos em: {download_path}")
