# app.py
# Flask + API de Cotação do Dólar
# Autor: Seu Nome
# Data: 2025-04-14

from flask import Flask, render_template
import requests
import os

# Caminho do diretório onde está o index.html
app_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=app_dir)

def obter_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        
        cotacao_atual = float(dados["USDBRL"]["bid"])
        variacao = float(dados["USDBRL"]["pctChange"])

        return {
            "cotacao": cotacao_atual,
            "variacao": variacao
        }
    
    except Exception as e:
        return {
            "erro": str(e)
        }

@app.route('/')
def index():
    dados = obter_cotacao()
    return render_template('index.html', dados=dados)

if __name__ == "__main__":
    app.run(debug=True)
