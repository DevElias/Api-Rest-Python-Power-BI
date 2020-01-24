# Biblioteca que cria as APIs e Rotas
from flask import Flask, jsonify
# Biblioteca do Json simples para objetos com varios tipos de elementos (decimal, string, inteiro, etc)
import simplejson as json
# Código Fonte que respode na Rota Default /
from Controller import home
# Código Fonte que respode na Rota Clientes
from Controller import clientes
# Código Fonte que respode na Rota Receitas
from Controller import receita
# Biblioteca que imprime na tela os resultados melhor organizados
from pprint import pprint

app = Flask(__name__)

# Cria a Rota Home
@app.route('/', methods=['GET'])
def index():
    response = home.home()
    return response,200

# Cria Rota CLientes
@app.route('/clientes', methods=['GET'])
def ListaCliente():
    # Busca os CLientes do ERPFlex
    response = clientes.getClientes()
    # Converte o Objeto em Json
    return jsonify(response),200

# Cria Rota das Receitas
@app.route('/receitas', methods=['GET'])
def ListaReceitas():
    # Busca as Receitas no ERPFlex
    response = receita.getReceita()
    # Converte o Objeto em Json
    return jsonify(response),200

# Roda o Server
if __name__ == '__main__':
    app.run(debug=True)