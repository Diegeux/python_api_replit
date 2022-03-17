import pandas as pd
from flask import Flask, jsonify

api = Flask(__name__)
table = pd.read_csv("dataset.csv")

@api.route('/')
def homepage():
  return "Seja bem vindo(a) a API do Diego Oliveira."
  
@api.route('/dados_vendas')
def vendas():
  total_tv = table['TV'].sum()
  total_radio = table['Radio'].sum()
  total_ventilador = table['Ventilador'].sum()
  total_geladeira = table['Geladeira'].sum()
  
  resposta = {'Total_tv': total_tv,
              'Total_radio': total_radio,
              'Total_ventilador': total_ventilador,
              'Total_geladeira': total_geladeira}

  return jsonify(resposta)
  
api.run(host='0.0.0.0')