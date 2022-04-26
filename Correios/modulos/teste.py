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

def teste1():
    
    url = csv_to_dict(pagina_web)['url']
    abrir_browser = webdriver.Chrome()
    abrir_browser.get(url)

    endereco = 'feliz natal'
    abrir_browser.find_element_by_name('relaxation').send_keys(endereco)
    xpath = csv_to_dict(pagina_web)['xpath']
    botao_pesquisar = abrir_browser.find_element(By.XPATH, xpath)
    clicar_botao = botao_pesquisar.click()

    xpath_celula_parte1 = csv_to_dict(pagina_web)['xpath_celula_1']
    xpath_celula_parte2 = csv_to_dict(pagina_web)['xpath_celula_2']
    xpath_celula_parte3 = csv_to_dict(pagina_web)['xpath_celula_3']
    tabela_endereco = []
    colunas_por_linha = []
    linha = 1
    coluna = 1

    for x in range(12):
        linha += 1
        for y in range(4):
            celula = abrir_browser.find_elements_by_xpath(xpath_celula_parte1 + str(linha) + xpath_celula_parte2 + str(coluna) + xpath_celula_parte3)
            for z in celula:
                colunas_por_linha.append(z.text)
            coluna += 1
        tabela_endereco.append(colunas_por_linha)
        colunas_por_linha = []
        coluna = 1
    return tabela_endereco
print(teste1())
""" 
/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{linha}]/td[{coluna}]
linha = 1
coluna = 1
xpath_celula_parte1 = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{'
xpath_celula_parte2 = '}]/td[{'
xpath_celula_parte3 = '}]'
/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{,}]/td[{,}]
print(xpath_celula_parte1 + str(linha) + xpath_celula_parte2 + str(coluna) + xpath_celula_parte3)


[['Rua Feliz Natal ', 'Doutor Fábio Leite ', 'Cuiabá/MT ', '78052-125'], 
['Rua Feliz Natal ', 'Novos Campos ', 'Sorriso/MT ', '78898-139'], 
['Rua Feliz Natal (Lot Jd Alá) ', 'Mapim ', 'Várzea Grande/MT ', '78142-889'], 
['Rua Feliz Natal (Lot Jd Eldorado) ', 'Santa Isabel ', 'Várzea Grande/MT ', '78150-790'], 
['Rua Dionizio Cerqueira, 259 Lote N\n\nAC Feliz Natal ', 'Centro ', 'Feliz Natal/MT ', '78885-970'], 
['Rua Dionizio Cerqueira, 259 Lote N Clique e Retire Correios\n\nAC Feliz Natal Clique e Retire ', 'Centro ', 'Feliz Natal/MT ', '78885-959'], 
[' ', ' ', 'Feliz Natal/MT ', '78885-000'], ['Rua Natal Feliz ', 'Guajuviras ', 'Canoas/RS ', '92440-282'], 
['Rua Natália Tassignon Ferraz ', 'Palmital ', 'Porto Feliz/SP ', '18547-304'], 
['Avenida Felizardo Firmino Moura ', 'Nordeste ', 'Natal/RN ', '59042-200'], 
['Rua General Felizardo Brito ', 'Capim Macio ', 'Natal/RN ', '59078-410'], 
['Vila Felizardo Moura ', 'Nordeste ', 'Natal/RN ', '59042-203']]
"""