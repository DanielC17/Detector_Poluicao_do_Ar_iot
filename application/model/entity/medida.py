from datetime import datetime
class Medida:
        def __init__(self, id, ozonio, materialparticulado, monoxido_carbono, oxido_nitroso, data):
            self._id = id
            self._ozonio = ozonio
            self._materialparticulado = materialparticulado
            self._monoxido_carbono = monoxido_carbono
            self._oxido_nitroso = oxido_nitroso
            self._data = data


        def get_id(self):
            return self._id

        
        def get_ozonio(self):
            return self._ozonio

        
        def set_ozonio(self, value):
            self._ozonio = value

        
        def get_materialparticulado(self):
            return self._materialparticulado

        
        def set_materialparticulado(self, value):
            self._materialparticulado = value

        
        def get_monoxido_carbono(self):
            return self._monoxido_carbono

        
        def set_monoxido_carbono(self, value):
            self._monoxido_carbono = value

    
        def get_oxido_nitroso(self):
            return self._oxido_nitroso

        
        def set_oxido_nitroso(self, value):
            self._oxido_nitroso = value

        
        def get_data(self):
            return self._data

        
        def set_data(self, value):
            self._data = value

        def toDict(self):
            return {
                "id": self._id,
                "ozonio": self._ozonio,
                "materialparticulado": self._materialparticulado,
                "monoxido_carbono": self._monoxido_carbono,
                "oxido_nitroso": self._oxido_nitroso,
                "data": self._data.strftime('%d/%m/%Y %H:%M')
            }
