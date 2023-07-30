#import pandas as pd
from flask import request, jsonify, Flask
import random as rk
import csv

# importa um arquivo csv
# usando a biblioteca nativa csv
# e transforma em um dicionario
# o padrão é separado por vírgula, mas como ele esta separado por ponto e vírgula é necessario informar o delimiter
dicionario=[*csv.DictReader(open('planilha.csv'), delimiter=';')]

# apenas para visualização: vai exibir no console quando executar o dicionario
print(dicionario)

app = Flask(__name__) #cria um app flask com o nome do package

@app.route("/") #define a página inicial do site (home)

# o trecho será interpretado como html na página inicial
def home():
    html = """
    <p> <a href="/input">Visulizar os dados</a> </p>
    <p> <a href="/output">Receber / Enviar</a> </p>
"""
    return html


@app.route("/input") 

def input():
    return jsonify(dicionario) # "d" is the dictionary we defined

@app.route('/output', methods=['GET','POST']) #output page

def output():
    return jsonify(dicionario)

app.run()