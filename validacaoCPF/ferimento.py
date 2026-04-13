from flask import Flask, jsonify, request
api = Flask(__name__)

dict_pessoas = {}

def validar_cpf(cpf):
    
    if (len(cpf) != 11 or not cpf.isdigit()):
        return False

    soma = 0
    for i in range(0, 9):
        soma += int(cpf[i]) * (10-i)

    soma = (soma * 10) % 11
    soma = 0 if soma == 10 else soma

    if (soma != int(cpf[9])):
        return False
    
    soma = 0
    for i in range(0, 10):
        soma += int(cpf[i]) * (11-i)

    soma = (soma * 10) % 11
    soma = 0 if soma == 10 else soma

    if (soma != int(cpf[10])):
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
    afdasf = request.json

    if ("cpf" in afdasf and "nome" in afdasf):
        if (validar_cpf(afdasf["cpf"])):  
            if (afdasf["cpf"] not in dict_pessoas):
                dict_pessoas[afdasf["cpf"]] = afdasf["nome"]
                return jsonify(afdasf), 201
            return jsonify(f"cpf ja cadastrado"), 400
        return jsonify(f"cpf invalido"), 400
    return jsonify(f"sem nome / cpf"), 400



if __name__ == '__main__':
    api.run(debug=True)