from flask import Flask, request, jsonify
from flask_cors import CORS
from operacoes_banco import *

app = Flask(__name__)
CORS(app)

#endpoint para obter todos os usuarios existentes
@app.route("/usuariosExistentes", methods=["GET"])
def obter_UsuariosExistentes():
    usuarios = obterUsuariosExistentes()
    return jsonify(usuarios)

app.run()