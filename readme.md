
# **Pesquisa de endereço por RPA**

## Objetivo do Projeto
O programa tem como objetivo, criar uma planilha em Excel com saída de dados com descrição completa de endereço, para cada planilha com entrada de dados que for inserida como input numa pasta pré-determinada.

### Diretrizes do projeto
- Neste programa, não pode ser utilizada a API dos CORREIOS.
- O programa deve realizar raspagem de teça/webscraping.
- O programa deve permanecer em loop, monitorando se há uma nova planilha Excel (.xlsm, xlsx ...) com dados de entrada.
- A pasta para entrada de dados deve ser '.\A-Entrada'.
- A pasta para saída de dados deve ser '.\C-Saida'.
- URL de referência: https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm (Ativar a opção Pesquisar por palavras semelhantes).
- Somente considerar os resultados retornados na primeira página de cada pesquisa.
- Os arquivos de entrada devem ser movidos para pasta de histórico/processados “C-Saída”

## Como usar a aplicação
Deve ser executado o arquivo main.
    
    python main.py

### Planilha de entrada
Os arquivos de entrada devem ter 3 colunas com preenchimento correto ou incorreto. As colunas são relativas aos campos: NOME | CEP | CRITÉRIO DE BUSCA
Exemplo de preenchimento:

| NOME  | CEP | Critério de busca  |  |
| ------------- |:-------------:||:-------------:|
| AV PAULISTA   | 12345678      | Nome
|               | 38400         | CEP
|               | 38400311      |

- Se for enforçado uma CriterioBuscaPor CEP, usar o CEP;
- Se for enforçado uma CriterioBuscaPor NOME, usar o Nome;
- Se não for informado o CriterioBuscaPor, tentar buscar pelo Nome, se existir, senão pelo CEP;
- Fazer validações! Retornar erro caso o input seja inválido ou impossível!

### Planilha de saída
Os resultados de todas as buscas realizadas sobre uma planilha de entrada serão consolidados em uma nova planilha de saída.


## Pré-requisitos 

Python 3.7

Principais pacotes
- Numpy
- Selenium
- Pandas

Package           Version
----------------- ---------
async-generator   1.10
attrs             21.4.0
certifi           2021.10.8
cffi              1.15.0
et-xmlfile        1.1.0
h11               0.13.0
idna              3.3
numpy             1.21.6
openpyxl          3.0.9
outcome           1.1.0
pandas            1.3.5
pip               22.0.4
pycparser         2.21
pyOpenSSL         22.0.0
PySocks           1.7.1
python-dateutil   2.8.2
pytz              2022.1
selenium          4.1.3
setuptools        40.8.0
six               1.16.0
sniffio           1.2.0
sortedcontainers  2.4.0
trio              0.20.0
trio-websocket    0.9.2
typing_extensions 4.1.1
urllib3           1.26.9
wsproto           1.1.0