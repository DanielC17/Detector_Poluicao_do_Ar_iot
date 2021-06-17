from application import app
from application.model.dao.medidaDao import MedidaDao, medida_list
from flask import request, redirect, jsonify
from application.model.entity.medida import Medida


@app.route("/medicoes", methods=['GET'])
def mostrarMedicoes():
    medida_list_dict = []
    for i in medida_list.listarMedicoes():
        medida_list_dict.append(i.toDict())
    return jsonify(medida_list_dict)


@app.route("/medicoes", methods=['POST'])
def adicionarMedicoes():
    id = int(request.json.get("id", None))
    ozonio = float(request.json.get("ozonio", None))
    materialparticulado = float(request.json.get("materialparticulado", None))
    monoxido_carbono = float(request.json.get("monoxido_carbono", None))
    oxido_nitroso = float(request.json.get("oxido_nitroso", None))
    data = float(request.json.get("data", None))



