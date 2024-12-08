# Teste usando Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurando o WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
wait = WebDriverWait(navegador, 10)

try:
    # Acessando a página
    navegador.get('https://app.plugestoque.com.br/auth')

    # Interagindo com os campos de e-mail e senha
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-auth/div/div/form/div[1]/input-default/div/input')))
    email_input.send_keys('lekantatransportes@hotmail.com')

    senha_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-auth/div/div/form/div[2]/input-default/div/input')))
    senha_input.send_keys('1234')

    # Clicando no botão de login
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-auth/div/div/form/button-spinner/button')))
    login_button.click()

    # Interagindo com o menu após login
    menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/layout-base/nav/div/div[1]/button')))
    menu_button.click()

    menu_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="drawer-navigation"]/div/ul/li[5]/a')))
    menu_option.click()

    # Mantendo o navegador aberto
    input("Pressione Enter para fechar o navegador...")

finally:
    # Encerrando o navegador
    navegador.quit()
    print("Navegador encerrado.")

