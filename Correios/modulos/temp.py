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
       
    #******************** dividir em duas funções *******************

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

palavra = '1 a 10 de 1'
def qtde_resultado_pag1(resultado_retornado):
    "Retorna o número que está entre a letra 'a' e a palavra 'de' no texto."
    
    posicao_a = resultado_retornado.find('a')
    posicao_de = resultado_retornado.find('de')   
    return int(palavra[posicao_a + 2:posicao_de - 1])


def iterar_planilha_endereco():
    return '38400322'

def acessar_site(site):
    url = csv_to_dict(pagina_web)['url']
    abrir_browser = webdriver.Chrome()
    abrir_browser.get(url)
    text_para_buscar = iterar_planilha_endereco()
    site(abrir_browser, text_para_buscar)

@acessar_site
def pesquisar_endereco(abrir_browser, endereco):
    abrir_browser.find_element_by_name('relaxation').send_keys(endereco)
    xpath = csv_to_dict(pagina_web)['xpath']
    botao_pesquisar = abrir_browser.find_element(By.XPATH, xpath)
    clicar_botao = botao_pesquisar.click()
    tabela_endereco_browser = abrir_browser.find_element_by_tag_name('tbody').text

#print(pesquisar_endereco)

def teste1():
    endereco = 'feliz natal'
    url = csv_to_dict(pagina_web)['url']
    abrir_browser = webdriver.Chrome()
    abrir_browser.get(url)

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

    for x in range(qtde_resultado_pag1(palavra)):
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
