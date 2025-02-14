from selenium import webdriver

# Configuração do WebDriver
driver = webdriver.Chrome()

# Acessar uma página de exemplo
driver.get("https://www.google.com")

print(driver.title)

driver.quit()
