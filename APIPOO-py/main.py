from flask import Flask, jsonify, request
api = Flask(__name__)

from objetos.papel import Papel
from objetos.pedra import Pedra
from objetos.tesoura import Tesoura

lista_objetos = [Papel("vermelho"), Pedra("vermelho"), Tesoura("prata"), Pedra("preta")]




@api.route("/", methods=["GET"])
def get_main():
    return jsonify("funcionando."), 200

@api.route("/cor/<string:coisa>", methods=["GET"])
def get_cores(coisa):
    resultado = []
    
    for item in lista_objetos:
        if (item.get_cor() == coisa):
            resultado.append(item.get_tipo())

    return jsonify(resultado), 200


@api.route("/adicionar", methods=["POST"])
def nova_coisa():
    nova_coisa = request.json

    if "cor" not in nova_coisa or "tipo" not in nova_coisa:
        return jsonify(f"sem cor / tipo"), 400


    match nova_coisa["tipo"]:
        case "tesoura":
            lista_objetos.append(Tesoura(nova_coisa["cor"]))
        case "papel":
            lista_objetos.append(Papel(nova_coisa["cor"]))
        case "pedra":
            lista_objetos.append(Pedra(nova_coisa["cor"]))
        case _:
            return jsonify(f"tipo invalido"), 400
    

    print(lista_objetos)
    return jsonify(nova_coisa), 201




if __name__ == '__main__':
    api.run(debug=True)