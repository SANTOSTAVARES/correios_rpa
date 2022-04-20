from cgitb import html
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from html.parser import HTMLParser
import re
"""
navegador = webdriver.Chrome()
navegador.get("https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm")
navegador.find_element_by_name('relaxation').send_keys("38400")
button = navegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/div[6]/input')
button.click()
ab = navegador.find_element_by_tag_name('tbody')
a1 = ab.text
print(re.split('\n|  ', a1))

""" 
print('começoooooou')
url = "https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm"
abrir_browser = webdriver.Chrome()
abrir_browser.get(url)
dado_para_buscar = '38400322'
abrir_browser.find_element_by_name('relaxation').send_keys("38400")
xpath = '//*[@id="Geral"]/div/div/div[6]/input'
botao_pesquisar = abrir_browser.find_element(By.XPATH, xpath)
clicar_botao = botao_pesquisar.click()
tabela_endereco_browser = abrir_browser.find_element_by_tag_name('tbody').text
lista_dados_endereco = re.split('\n|  ', tabela_endereco_browser)
lista_dados_endereco.pop(0)
print(lista_dados_endereco[0])

tabela_endereco = []
linha_tabela = ['', '', '', '']
coluna = 0
for i in lista_enderecos:
    if coluna == 1 and  i == '':
        continue
    elif coluna == 2 and linha_tabela[1] == '':
        linha_tabela[1] = i
        continue
    elif coluna == 3:
        linha_tabela[]
    else:
        coluna += 1
    linha_tabela[coluna] = i

print('finalizooooou')    
#html1 = navegador.page_source
#print(type(navegador))
#print(type(html1))
#HTMLParser.handle_starttag(html, <head>, <body>)
#a = html1.find('<a>')
#a = html1.find('div')
#b = html1
#print(html1[6600: 7000])
#b = html1.find('div')
#print(b)


