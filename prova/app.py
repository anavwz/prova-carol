from flask import Flask, jsonify
import os

app = Flask(__name__)

usuarios = [
    {
    "id": 1, 
    "nome": "Maria"
    },

    {
    "id": 2, 
    "nome": "Laura"
    },
    
    {
    "id": 3, 
    "nome": "Alice"
    },

    {
    "id": 4, 
    "nome": "Paulo"
    }
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Usuarios - Acesse /usuarios"})

@app.route("/", methods=["GET"])
def listar_usuario():
    return jsonify(usuarios)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)