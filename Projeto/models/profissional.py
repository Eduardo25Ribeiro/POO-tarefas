from datetime import datetime


class Profissional:
    def __init__(self, id, data, confirmado, id_cliente, id_servico):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_id_profissional(id_cliente)
        self.set_id_servico(id_servico)

    def set_id(self, id):
        if not isinstance(id, int):
            raise TypeError("Id deve ser um número inteiro")
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_data(self, data):
        if isinstance(data, datetime):
            self.__data = data
            return
        if isinstance(data, str):
            self.__data = datetime.strptime(data, "%d/%m/%Y %H:%M")
            return
        raise TypeError("Data deve ser do tipo datetime ou string no formato dd/mm/AAAA HH:MM")

    def set_confirmado(self, confirmado):
        if not isinstance(confirmado, bool):
            raise TypeError("Confirmado deve ser True ou False")
        self.__confirmado = confirmado

    def set_id_profissional(self, id_cliente):
        if not isinstance(id_cliente, int):
            raise TypeError("Id do cliente deve ser um número inteiro")
        if id_cliente < 0:
            raise ValueError("Id do cliente deve ser positivo")
        self.__id_cliente = id_cliente

    def set_id_servico(self, id_servico):
        if not isinstance(id_servico, int):
            raise TypeError("Id do serviço deve ser um número inteiro")
        if id_servico < 0:
            raise ValueError("Id do serviço deve ser positivo")
        self.__id_servico = id_servico

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_confirmado(self):
        return self.__confirmado

    def get_id_profissional(self):
        return self.__id_cliente

    def get_id_servico(self):
        return self.__id_servico

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
        }

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic["id"],
            dic["data"],
            dic["confirmado"],
            dic["id_cliente"],
            dic["id_servico"],
        )
