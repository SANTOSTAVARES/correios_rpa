from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv

pagina_web = 'link_caminho.csv'
def csv_to_dict(arquivo):
    ''' Converte para dicionário, dados de um arquivo CSV que contenham duas linhas.
        Sendo que a linha 1 (cabeçalho) é tida como chave e a linha 2 como valor.'''
        
    with open(arquivo) as arquivo_csv:
        dados_csv = csv.reader(arquivo_csv, delimiter=',')
        linha_csv = 1
        
        for x in dados_csv:
            if linha_csv == 1:
                chave = x           
            else:
                valor = x
            linha_csv += 1

    return dict(zip(chave, valor))

url = csv_to_dict(pagina_web)['url']
abrir_browser = webdriver.Chrome()
abrir_browser.get(url)

endereco = 'feliz natal'
linha = 6
coluna = 4

abrir_browser.find_element_by_name('relaxation').send_keys(endereco)
xpath = csv_to_dict(pagina_web)['xpath']
botao_pesquisar = abrir_browser.find_element(By.XPATH, xpath)
clicar_botao = botao_pesquisar.click()
#tabela_endereco_browser = abrir_browser.find_element_by_tag_name('tbody').text
element = abrir_browser.find_elements_by_xpath(f"/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{linha}]/td[{coluna}]")

for value in element:
    print('>')
    print(value.text)

#/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/th[1]
#/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]



