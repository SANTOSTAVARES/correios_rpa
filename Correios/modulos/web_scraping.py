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

    try:
        msg_qtde_resultado = texto[73:]
        posicao_a = msg_qtde_resultado.find('a')
        posicao_de = msg_qtde_resultado.find('de')
        msg_qtde_resultado = int(msg_qtde_resultado[posicao_a + 2:posicao_de - 1])
    except ValueError as erro:
        print(f'Foi encontrado o erro abaixo:\n{erro}' )
        msg_qtde_resultado = None
    else:
        print('A pesquisa encontrou dados com sucesso')
    finally:
        return msg_qtde_resultado
  
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

    if qtde_resultado_pag1() is None:
        tabela_endereco = None
    else:
        for x in range(qtde_resultado_pag1()):
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
    arquivo_entrada = arquivo_entrada.fillna('')
    arquivo_entrada[[0, 1]] = arquivo_entrada[[0, 1]].astype(str)
    arquivo_entrada[1] = arquivo_entrada[1].apply(lambda x: x.replace('.0', ''))
    return arquivo_entrada.values.tolist()

def teste():
    
    if identificar_entrada() is None:
        Continue
    else:
        linha_entrada = 1
        tabela_saida = []
        linha_saida = []
        for x in planilha_to_list(identificar_entrada()):
            
            if len(str(x[1])) < 3:
                print(f'A palavra abaixo contém menos de 3 digitos:\n{x[1]}')
                linha_saida.append(linha_entrada)
                linha_saida.append('Texto de endereço é insuficiente, por ser menor que 3 digitos')
                linha_saida.append(x[1])
                tabela_saida.append(linha_saida)
                linha_saida = []
            else:   
                if retorna_resultado_pesquisa(x[1]) is None:
                    linha_saida.append(linha_entrada)
                    linha_saida.append('Texto de endereço não encontrou nenhum resultado na pesquisa')
                    linha_saida.append(x[1])
                    tabela_saida.append(linha_saida)
                    linha_saida = []
                else: 
                    for y in retorna_resultado_pesquisa(x[1]):
                        linha_saida.append(linha_entrada)
                        linha_saida.append('CEP')
                        linha_saida.append(x[1]) 
                        for z in range(4):
                            linha_saida.append(y[z])
                        
                        tabela_saida.append(linha_saida)
                        linha_saida = []
                        
            linha_entrada += 1
            

        return tabela_saida

def teste2():
    
    linha_entrada = 1
    tabela_saida = []
    linha_saida = []
    coluna_referencia = ''

    def menor_3_digitos():
        linha_saida = []
        print(f'A palavra abaixo contém menos de 3 digitos:\n{x[coluna_referencia]}')
        linha_saida.append(linha_entrada)
        linha_saida.append('Texto de endereço é insuficiente, por ser menor que 3 digitos')
        linha_saida.append(x[coluna_referencia])
        tabela_saida.append(linha_saida)
        linha_saida = []

    def resultado_none():
        linha_saida = []
        linha_saida.append(linha_entrada)
        linha_saida.append('Texto de endereço não encontrou nenhum resultado na pesquisa')
        linha_saida.append(x[coluna_referencia])
        tabela_saida.append(linha_saida)
        linha_saida = []
    
    def preencher_resultado():
        linha_saida.append(linha_entrada)
        if coluna_referencia == 0:
            linha_saida.append('Nome')
            linha_saida.append(x[0]) 
        else:
            linha_saida.append('CEP')
            linha_saida.append(x[1]) 
        for z in range(4):
            linha_saida.append(y[z])
    
    if identificar_entrada() is None:
        Continue
    else:    
        for x in planilha_to_list(identificar_entrada()):
            try:
                if x[2] == 'Nome':
                    coluna_referencia = 0
                elif x[2] == 'Cep':
                    coluna_referencia = 1 
                else:
                    if x[0] != '':
                        coluna_referencia = 0
                    else:
                        coluna_referencia = 1

            except IndexError as erro:
                print(f'Ao buscar os dados a seguir:\n{x}\nOcorreu o seguinte erro:\n{erro}')

            else:
                if len(str(x[coluna_referencia])) < 3:
                    menor_3_digitos()
                else:
                    if retorna_resultado_pesquisa(x[coluna_referencia]) is None:
                        resultado_none()
                    else:
                        for y in retorna_resultado_pesquisa(x[coluna_referencia]):
                            preencher_resultado()
                            tabela_saida.append(linha_saida)
                            linha_saida = []
                
            linha_entrada += 1
    
    tabela_saida = pd.DataFrame(tabela_saida, columns=['Linha Excel Entrada', 'Critério Busca Utilizado', 'Parâmetro de busca utilizado', 'Logradouro/Nome:', 'Bairro/Distrito:', 'Localidade/UF:', 'CEP:'])
    tabela_saida.to_excel('saida.xlsx')
    return tabela_saida
        

print(teste2())