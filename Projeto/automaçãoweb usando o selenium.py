# Teste usando Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# teste do git

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

wait =  WebDriverWait(navegador,10)
# Entrada na pag
navegador.get('https://app.plugestoque.com.br/auth')
# colocando o Login e senha
navegador.find_element('xpath','/html/body/app-root/app-auth/div/div/form/div[1]/input-default/div/input').send_keys('lekantatransportes@hotmail.com')

navegador.find_element('xpath','/html/body/app-root/app-auth/div/div/form/div[2]/input-default/div/input').send_keys('1234')
# clicando no botão
c=wait.until(navegador.find_element('xpath','/html/body/app-root/app-auth/div/div/form/button-spinner/button').click())

navegador.find_element('xpath','/html/body/app-root/layout-base/nav/div/div[1]/button').click()

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-auth/div/div/form/button-spinner/button')))
login_button.click() 

navegador.find_element('xpath','//*[@id="drawer-navigation"]/div/ul/li[5]/a').click()
try:
    input("Pressione Enter para fechar o navegador...")
finally:
    navegador.quit()
    print("Navegador encerrado.")
    
