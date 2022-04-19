from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm")
navegador.find_element_by_name('relaxation').send_keys("38400")
button = navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/div[6]/input')
button.click()
html = navegador.page_source
print(html)