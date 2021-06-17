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
    data = request.json.get("data", None)

    medida = Medida(id, ozonio, materialparticulado, monoxido_carbono, oxido_nitroso, data)
    medida_list.adicionarMedicoes(medida)
    return medida.toDict()


@app.route("/medicoes/id/<id>", methods=['GET'])
def buscarIdMedicoes(id: int):
    medida_list_dict = []
    for i in medida_list.listarMedicoes():
        if int(i.get_id()) == int(id):
            medida_list_dict.append(i.toDict())
    return jsonify(medida_list_dict)


@app.route("/medicoes/data/<data>", methods=['GET'])
def buscarDataMedicoes(data):
    medida_list_dict = []
    for i in medida_list.listarMedicoes():
        date = i.get_data().replace("/", "")
        if date == data:
            medida_list_dict.append(i.toDict())
    return jsonify(medida_list_dict)
