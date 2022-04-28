
# Descrição do projeto

Tarefas a serem realizadas pelo programa
Deve 'loopar' uma pasta de entrada "A-Entrada", procurar por arquivos Excel (.xlsm, xlsx ...). Esses arquivos devem ter 3 colunas com preenchimento correto ou incorreto. Sendo essas colunas dos 3 tipos seguintes: [NOME, CEP; CRITÉRIO DE BUSCA; Exemplos
NOME;        CEP;       CRITÉRIO DE BUSCA
AV PAULISTA; 12345678;  Nome
    ;        38400;
    ;        38400322;  CEP

Para cada linha... realizar uma busca pelo endereço, usando NOME ou CEP, no site do Correios (Utilizar raspagem de tela/webscraping, não utilizar de API).
URL de referência: https://www2.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm
    Ativar a opção Pesquisar por palavras semelhantes
    Se for enforçado uma CriterioBuscaPor CEP, usar o CEP;
    Se for enforçado uma CriterioBuscaPor NOME, usar o Nome;
    Se não for informado o CriterioBuscaPor, tentar buscar pelo Nome, se existir, senão pelo CEP;
    Fazer validações! Retornar erro caso o input seja inválido ou impossível!

Consolidar os resultados em uma nova planilha
Somente considerar os resultados retornados na primeira página de cada pesquisa
TODAS as linhas (da planilha de entrada) irão resultar em uma ÚNÍCA planiha de saída

Salvar planilha de saída em uma pasta “B”, nome do arquivo com algum identificador para evitar duplicidade

Mover arquivo de entrada para pasta de histórico/processados “C-Saída”

Loopar: Verificar se uma pasta possui conteúdo/arquivos. Se houver, trabalhar com ele(s).
Geralmente a termologia é “looping”, pois caso não haja arquivos, a ação persiste até que apareça o próximo arquivo.
Neste exercício, pode assumir que houver N arquivos, somente um precisa ser processado por vez.

Os arquivos da entrada devem ser disponibilizados na pasta:
A-Entrada

Os resultados serão disponibilizados na pasta:
C-Saida

# Funcionalidades

Para colocar programa em produção, execute no terminal arquivo main.py disponível em '\Correios\modulos'. O programa irá realizar um loop contínuo, até que uma seja disponibilizada.
Adicione um arquivo excel no diretório '\Correios\A-Entrada'. Este arquivo deve ter o preenchimento entre as A, B e C. Caso queira procurar um endereço que você tem possui a descrição incompleta, siga os seguintes parâmetro:
Na coluna A pode ser adcionado o Nome do endereço. Por exemplo: Avenida Paulista
Na coluna B pode ser adcionado o CEP do endereço. Por exemplo: 15370
Na coluna C pode ser pré-determinado o parâmetro de busca como 'Nome', CEP ou deixar sem preenchimento. Neste último caso, será considerado primeiro o parâmetro Nome e em seguida CEP.

Após o programar obter o dado base para busca, ele irá procurar no site dos Correios e posteriormente irá salvar numa só planilha, todas informações de resultado sobre cada linha preenchida e, irá salvar na pasta C-Saida dentro de uma pasta a ser criada, para ficar no mesmo diretório o arquivo de entrada e o de saída.

# Pré-requisitos 

Python 3.7

Principais pacotes
Numpy
Selenium
Pandas

Package           Version
----------------- ---------
async-generator   1.10
attrs             21.4.0
certifi           2021.10.8
cffi              1.15.0
cryptography      36.0.2
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