from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os
from dotenv import load_dotenv

#Carrega as variáveis de ambiente para o programa
load_dotenv(override=True)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Caminho retornado pelo comando 'which geckodriver'
geckodriver_path = "/snap/bin/geckodriver"

# Cria o serviço para o geckodriver
service = Service(geckodriver_path)

# Inicializa o driver do Firefox utilizando o serviço
driver = webdriver.Firefox(service=service)

# Abre o site
url = "https://aluno.grancursosonline.com.br/graduacao/curso/qlK7xerB192XVzrgM3Ld43RWpGgMawZy?a=7odG"
driver.get(url)

# ---------------------- Parte de Autenticação Mantida ----------------------
# Aguarde a página carregar completamente
wait = WebDriverWait(driver, 20)

# Ajuste os seletores de acordo com os IDs ou outros atributos dos campos do site
user_field = wait.until(EC.presence_of_element_located((By.ID, "login-email-site")))
pass_field = driver.find_element(By.ID, "login-senha-site")
login_button = driver.find_element(By.ID, "login-entrar-site")

user_field.send_keys(username)
print("Username:", username)
pass_field.send_keys(password)

time.sleep(5)

login_button.click()

wait = WebDriverWait(driver, 20)
# ---------------------- Fim da Parte de Autenticação Mantida ----------------------

# ---------------------- Nova Parte para clicar nos botões pela classe ----------------------
classe_desejada = "btn btn-sm bg-color-light-200 hover:color-accent-600 hover:border-accent-400 color-mid-600 d-flex align-items-center justify-content-center width-32 height-32"

try:
    # Aguarde até que os botões com a classe desejada estejam presentes na página
    buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, classe_desejada)))
    print(f"Encontrados {len(buttons)} botões com a classe '{classe_desejada}'.")

    # Clique em cada botão encontrado
    for button in buttons:
        ActionChains(driver).move_to_element(button).perform() # Garante que o botão esteja visível, se necessário
        button.click()
        print("Botão clicado.")
        time.sleep(1) # Delay entre os cliques

except Exception as e:
    print(f"Erro ao clicar nos botões com a classe '{classe_desejada}': {e}")
# ---------------------- Fim da Nova Parte para clicar nos botões pela classe ----------------------

# Feche o navegador após a automação
time.sleep(5) # Aguarde um tempo para garantir que os downloads iniciem, se aplicável
driver.quit()