from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv

pagina_web = 'link_caminho.csv'
def csv_to_dict(arquivo):
    
    with open(arquivo) as arquivo_csv:
        dados_csv = csv.reader(arquivo_csv, delimiter=',')
        linha_csv = 1
        for x in dados_csv:

            if linha_csv == 1:
                chave = x           
            else:
                valor = x
            for y in x:            
                pass
            linha_csv += 1

    return dict(zip(chave, valor))

#print(csv_to_dict(pagina_web)['url'])

def buscar_endereco_correios(endereco):

    url = csv_to_dict(pagina_web)['url']
    abrir_browser = webdriver.Chrome()
    abrir_browser.get(url)
    
    abrir_browser.find_element_by_name('relaxation').send_keys(endereco)
    xpath = csv_to_dict(pagina_web)['xpath']
    botao_pesquisar = abrir_browser.find_element(By.XPATH, xpath)
    clicar_botao = botao_pesquisar.click()
    tabela_endereco_browser = abrir_browser.find_element_by_tag_name('tbody').text

    lista_dados_endereco = re.split('\n|  ', tabela_endereco_browser)
    lista_dados_endereco.pop(0)
    tabela_endereco = []
    linha_tabela = []
    penultimo_dado_vazio = False

    for i in lista_dados_endereco:
        if i != '':
            if penultimo_dado_vazio == True:
                linha_tabela[-1] = linha_tabela[-1] + ' ' + i
                penultimo_dado_vazio = False
            else:
                linha_tabela.append(i)
                if len(linha_tabela) == 4:
                    tabela_endereco.append(linha_tabela)
                    linha_tabela = []
        else:
            penultimo_dado_vazio = True
    return tabela_endereco

print(buscar_endereco_correios('38400'))  