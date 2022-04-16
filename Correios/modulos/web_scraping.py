from selenium import webdriver
import selenium
""" 
navegador = webdriver.Chrome()
navegador.get("https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm")
navegador.find_element_by_name('//*[@id="Geral"]/div/div/span[2]/label/input').send_keys('38400322') 
 """

navegador = webdriver.Chrome()
navegador.get("https://www.google.com.br")
navegador.find_element_by_name('q').send_keys("gabriel tavares")
#navegador.find_element_by_name('btnK').click()
navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')

