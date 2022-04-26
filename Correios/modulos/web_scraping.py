from ast import Continue
from lib2to3.pgen2 import driver
from numpy import append
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv
import pandas as pd
from os import listdir, mkdir
from os.path import isfile
import shutil

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

def criar_pasta():
    mkdir(csv_to_dict(pagina_web)['pasta_saida'] + 'Pasta_teste')
    return 'Diretório criado com sucesso.'

def mover_arquivo():
    shutil.move('..\A-Entrada\modelo.xlsx', '..\C-Saida')

pagina_web = 'link_caminho.csv'


def qtde_resultado_pag1():
    """ Retorna o texto se o dados foram encontrados com sucesso.
    E retorna o número que está entre a letra 'a' e a palavra 'de' no texto."""
    
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
  
def buscar_endereco(endereco_planilha):
    """ Acessa a url informada no arquivo link_caminhos.csv e realiza a busca de endereço. """

    url = csv_to_dict(pagina_web)['url']
    global abrir_browser
    abrir_browser = webdriver.Chrome()
    abrir_browser.get(url)

    abrir_browser.find_element_by_name('relaxation').send_keys(endereco_planilha)
    xpath = csv_to_dict(pagina_web)['xpath']
    botao_pesquisar = abrir_browser.find_element(By.XPATH, xpath)
    clicar_botao = botao_pesquisar.click()
    
def retorna_resultado_pesquisa(endereco_planilha):
    """ Cria a tabela com o resultado da pesquisa realizada no site. """
    
    buscar_endereco(endereco_planilha)

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


def identificar_entrada():
    """ Retorna o nome de um arquivo que está na pasta. """

    try:
        listdir(csv_to_dict(pagina_web)['pasta_entrada'])[0]
    except IndexError:
        print('A pasta está vazia.')
        return None
    else:
        return listdir(csv_to_dict(pagina_web)['pasta_entrada'])[0]

def planilha_to_list(nome_planilha_entrada):
    """ Converte para lista do Python, dados de um arquivo excel. """

    arquivo_entrada = pd.read_excel(csv_to_dict(pagina_web)['pasta_entrada'] + nome_planilha_entrada, header=None)
    return arquivo_entrada.values.tolist()

def teste():
    
    if identificar_entrada() is None:
        Continue
    else:
        linha_entrada = 1
        tabela_saida = []
        linha_saida = []
        for x in planilha_to_list(identificar_entrada()):
            
        #if x[2] == 'CEP':
            if len(str(x[1])) < 3:
                linha_saida.append(linha_entrada)
                linha_saida.append('Texto de endereço é insuficiente, por ser menor que 3 digitos')
            
            else:   
                for y in retorna_resultado_pesquisa(x[1]):
                    linha_saida.append(linha_entrada)
                    linha_saida.append('CEP')
                    linha_saida.append(x[1])
                    linha_saida.append(y[0])
                    linha_saida.append(y[1])
                    linha_saida.append(y[2])
                    linha_saida.append(y[3])
                    tabela_saida.append(linha_saida)
                    linha_saida = []
            tabela_saida.append(linha_saida)
            linha_entrada += 1
            linha_saida = []

        return tabela_saida

            
            


print(teste())