from flask import Flask, jsonify, request
api = Flask(__name__)

dict_pessoas = {}

def validar_cpf(cpf):
    def calcular_validador(digito):
        soma = 0

        for i in range(0, digito):
            soma += int(cpf[i]) * ((digito+1)-i)

        soma = (soma * 10) % 11
        return 0 if soma == 10 else soma


    if (len(cpf) != 11 or not cpf.isdigit()):
        return False

    if (calcular_validador(9) != int(cpf[9])):
        return False
    
    if (calcular_validador(10) != int(cpf[10])):
        return False
        
    return True


@api.route("/", methods=["GET"])
def get_main():
    return jsonify("funcionando."), 200

@api.route("/pessoa/<string:cpf>", methods=["GET"])
def get_pessoa(cpf):
    if (cpf not in dict_pessoas):
        return jsonify("pessoa nao existe"), 200

    return jsonify(dict_pessoas[cpf]), 200


@api.route("/adicionar", methods=["POST"])
def nova_pessoa():
    pessoa = request.get_json(silent=True) or {}
    nome = pessoa.get("nome")
    cpf = pessoa.get("cpf")

    if not nome or not cpf:
        return jsonify("sem nome / cpf"), 400
    
    if (not validar_cpf(cpf)):
        return jsonify("cpf invalido"), 400
    
    if (cpf in dict_pessoas):
        return jsonify("cpf ja cadastrado"), 400

    dict_pessoas[cpf] = nome
    return jsonify({"nome": nome, "cpf": cpf}), 201


if __name__ == '__main__':
    api.run(debug=True)