from application.model.entity.medida import Medida
from datetime import datetime


class MedidaDao():
    def __init__(self, medicoes):
        self._medicoes = medicoes

    def listarMedicoes(self):
        return self._medicoes

    def adicionarMedicoes(self, medicao):
        self._medicoes.append(medicao)


medicao_1 = Medida(1, 1, 1, 1, 1, "14/06/2021")
medicao_2 = Medida(1, 2, 2, 2 ,2, "15/06/2021")
medicao_3 = Medida(2, 3, 3, 3, 3, "16/06/2021")

medida_list = MedidaDao([medicao_1, medicao_2,medicao_3])



