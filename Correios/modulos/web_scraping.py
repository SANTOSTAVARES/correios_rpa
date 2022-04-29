from ast import Continue
from lib2to3.pgen2 import driver
from operator import index
from time import time
from numpy import append
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import csv
import pandas as pd
from os import listdir, mkdir
from os.path import isfile
import shutil
from datetime import datetime
import time

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

pagina_web = 'link_caminho.csv'

def criar_pasta():
    
    nome_pasta = str(datetime.now())[:-7].replace(':', '.')
    mkdir(csv_to_dict(pagina_web)['pasta_saida'] + nome_pasta)
    print('Diretório criado com sucesso.')
    return nome_pasta

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
    arquivo_entrada = arquivo_entrada.values.tolist()
    de_para = []
    for i in arquivo_entrada:
        if len(i) == 2: #Este If foi adicionado só para evitar um Idexerror caso o usuário disponibilize uma planilha sem nenhum preenchimento na coluna c.
            i.append('')

        if i[2] == 'Nome':
            de_para.append(['Nome', i[0]])
        elif i[2] == 'CEP':
            de_para.append(['CEP', i[1]])
        elif i[2] == '' and i[0] != '':
            de_para.append(['Nome', i[0]])
        else:
            de_para.append(['CEP', i[1]])
    
    return de_para

def rotina_buscar_endereco():
    """ Realiza o loop contínuo sobre as planilhas de entrada e, as tranfere para um novo destino
    junto com a planilha com os resultados das buscas. """
    
    while True:
        linha_entrada = 1
        tabela_saida = []
        linha_saida = []

        def menor_3_digitos():
            linha_saida = []
            print(f'A palavra abaixo contém menos de 3 digitos:\n{x[1]}')
            linha_saida.append(linha_entrada)
            linha_saida.append('Texto de endereço é insuficiente, por ser menor que 3 digitos')
            linha_saida.append(x[1])
            for _ in range(4):
                linha_saida.append('')
            tabela_saida.append(linha_saida)
            linha_saida = []

        def resultado_none():
            linha_saida = []
            linha_saida.append(linha_entrada)
            linha_saida.append('Texto de endereço não encontrou nenhum resultado na pesquisa')
            linha_saida.append(x[1])
            for _ in range(4):
                linha_saida.append('')
            tabela_saida.append(linha_saida)
            linha_saida = []
        
        def preencher_resultado():
            linha_saida.append(linha_entrada)
            linha_saida.append(x[0])
            linha_saida.append(x[1]) 
            for z in range(4):
                linha_saida.append(y[z])
        
        def mover_arquivo_destino():
        
            shutil.move(csv_to_dict(pagina_web)['pasta_entrada'] + planilha_entrada, endereco_pasta_destino)
        
        try:
            if identificar_entrada() is None:
                loop_sem_entrada = True
                Continue
            else:   
                planilha_entrada = identificar_entrada()
                for x in planilha_to_list(identificar_entrada()):
                    if len(x[1]) < 3:
                        menor_3_digitos()
                    else:
                            tabela_resultado_pesquisa = retorna_resultado_pesquisa(x[1])
                            if tabela_resultado_pesquisa is None:
                                resultado_none()
                            else:
                                for y in tabela_resultado_pesquisa:
                                    preencher_resultado()
                                    tabela_saida.append(linha_saida)
                                    linha_saida = []
                    linha_entrada += 1
                loop_sem_entrada = False
        except Exception as erro:
            print(f'Ao executar a busca por endereços, ocorreu o seguinte erro: {erro}.')
        else:
            if loop_sem_entrada == True:
                print('Não há entrada para execução de tarefa.')
            else:
                tabela_saida = pd.DataFrame(tabela_saida, columns=['Linha Excel Entrada', 'Critério Busca Utilizado', 'Parâmetro de busca utilizado', 'Logradouro/Nome:', 'Bairro/Distrito:', 'Localidade/UF:', 'CEP:'])
                pasta_destino = criar_pasta()
                endereco_pasta_destino = f"{csv_to_dict(pagina_web)['pasta_saida']}{pasta_destino}"
                mover_arquivo_destino()
                tabela_saida.to_excel(f"{endereco_pasta_destino}\\resultado-{planilha_entrada}", index=False)
        finally:
            print(f'Loop finalizado. A rotina será executado novamente em 10 segundos.')
            time.sleep(10)