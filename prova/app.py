from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Dados iniciais
usuarios = [
    {
        "id": 1, 
        "nome": "Maria"
    },
    {
        "id": 2, 
        "nome": "Laura"
    }
]

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo = request.json
    novo['id'] = len(usuarios) + 1
    usuarios.append(novo)
    return jsonify(novo), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados_atualizados = request.json
    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['nome'] = dados_atualizados.get('nome', usuario['nome'])
            return jsonify(usuario), 200
    
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return jsonify({"mensagem": "Usuário removido com sucesso"}), 200
            
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)