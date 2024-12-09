# Teste usando Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#sempre atualizar os drives do navegador 
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
#espera para garantir que o navegador funcione
wait =  WebDriverWait(navegador,10)
# Entrada na pag
navegador.get('https://app.plugestoque.com.br/auth')
# colocando o Login e senha
wait.until(EC.presence_of_element_locate((By.xpath,'/html/body/app-root/app-auth/div/div/form/div[1]/input-default/div/input')))
navegador.find_element(By.xpath,'/html/body/app-root/app-auth/div/div/form/div[1]/input-default/div/input').send_keys('lekanatrasnportes@hotmail.com')
# senha do individo
wait
navegador.find_element('by.xpath','/html/body/app-root/app-auth/div/div/form/div[2]/input-default/div/input').send_keys('1234')

# clicando no botão
navegador.find_element('by.xpath','/html/body/app-root/app-auth/div/div/form/button-spinner/button').click()
input()