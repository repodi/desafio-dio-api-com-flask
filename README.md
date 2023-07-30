# Api com flask

Desafio DIO da Formação Python Developer que tem por objetivo a criação de uma web api utilizando o Flask.

## Objetivo

Criar uma api em Flask que consuma os dados de uma planilha que foi convertida para JSON.  

## Utilizando o ambiente Python

Para utilização no ambiente do próprio Python é necessário a instalação da biblioteca Flask no Python.

### Instalação do flask
Para checar se a biblioteca esta instalada: 

Executar o comando `pip list` no terminal de comandos.

Após executar o comando será exibido uma lista de bibliotecas instaladas. Caso o **Flask** não esteja nesta lista ele deverá ser instalado com o seguinte comando `pip install flask`. 

*Observação: Além do flask serão instaladas outras bibliotecas das quais o flask é dependente*

### Instruções para execução
Para execução do projeto utilizar o arquivo: 
api-importa-planilha-flask.py

O código irá ler o arquivo csv dentro da pasta utilizando a biblioteca nativa **csv**. 
Este arquivo deve estar no formato csv e não no formato do Microsoft Excel(R).
Para salvar um arquivo em csv no excel 

Para a leitura da planilha a planilha tem que estar no formato json. 
Para criar uma planilha no formato JSON no Microsoft Excel(R), quando clicar em salvar embaixo do campo *Nome do arquivo* em *Tipo* selecionar a opção *CSV UTF-8 (Delimitado por vírgulas)*.

O código aponta pro arquivo local na pasta diretamente. 