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

def iterar_planilha_endereco():
    return 'feliz natal'

#print(iterar_planilha_endereco())

def qtde_resultado_pag1():
    "Retorna o número que está entre a letra 'a' e a palavra 'de' no texto."
    
    xpath_qtde_resultado = csv_to_dict(pagina_web)['quantidade_resultado']
    texto_resultado = abrir_browser.find_elements_by_xpath(xpath_qtde_resultado)
    for i in texto_resultado:
        texto = i.text

    msg_dados_encontrados = texto[0:30]
    msg_qtde_resultado = texto[73:]
    posicao_a = msg_qtde_resultado.find('a')
    posicao_de = msg_qtde_resultado.find('de')
    msg_qtde_resultado = int(msg_qtde_resultado[posicao_a + 2:posicao_de - 1])
    
    return(msg_dados_encontrados, msg_qtde_resultado)
    
def resultado_pesquisa():

    url = csv_to_dict(pagina_web)['url']
    global abrir_browser
    abrir_browser = webdriver.Chrome()
    abrir_browser.get(url)
    texto_para_buscar = iterar_planilha_endereco()
    abrir_browser.find_element_by_name('relaxation').send_keys(texto_para_buscar)
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

    for x in range(qtde_resultado_pag1()[1]):
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

#print(resultado_pesquisa())
#print(csv_to_dict(pagina_web)['quantidade_resultado'])

def a1():
    url = csv_to_dict(pagina_web)['url']
    global abrir_browser
    abrir_browser = webdriver.Chrome()
    abrir_browser.get(url)
    texto_para_buscar = iterar_planilha_endereco()
    abrir_browser.find_element_by_name('relaxation').send_keys(texto_para_buscar)
    xpath = csv_to_dict(pagina_web)['xpath']
    botao_pesquisar = abrir_browser.find_element(By.XPATH, xpath)
    clicar_botao = botao_pesquisar.click()

def a2():
    a1()
    xpath_celula_parte1 = csv_to_dict(pagina_web)['xpath_celula_1']
    xpath_celula_parte2 = csv_to_dict(pagina_web)['xpath_celula_2']
    xpath_celula_parte3 = csv_to_dict(pagina_web)['xpath_celula_3']
    tabela_endereco = []
    colunas_por_linha = []
    linha = 1
    coluna = 1

    for x in range(qtde_resultado_pag1()[1]):
        linha += 1
        for y in range(4):
            celula = abrir_browser.find_elements_by_xpath(xpath_celula_parte1 + str(linha) + xpath_celula_parte2 + str(coluna) + xpath_celula_parte3)
            for z in celula:
                colunas_por_linha.append(z.text)
            coluna += 1
        tabela_endereco.append(colunas_por_linha)
        colunas_por_linha = []
        coluna = 1
    abrir_browser.close()
    
    return tabela_endereco

print(a2())