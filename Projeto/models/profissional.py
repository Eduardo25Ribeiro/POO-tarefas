from datetime import datetime


class Profissional:
    def __init__(self, id, nome,email,especialidade,senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)
        self.set_senha(senha)

    def set_id(self, id):
        if not isinstance(id, int):
            raise TypeError("Id deve ser um número inteiro")
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, data):
        if isinstance(data, datetime):
            self.__nome = data
            return
        if isinstance(data, str):
            self.__nome = datetime.strptime(data, "%d/%m/%Y %H:%M")
            return
        raise TypeError("Data deve ser do tipo datetime ou string no formato dd/mm/AAAA HH:MM")

    def set_email(self, confirmado):
        if not isinstance(confirmado, bool):
            raise TypeError("Confirmado deve ser True ou False")
        self.__email = confirmado

    def set_especialidade(self, id_cliente):
        if not isinstance(id_cliente, int):
            raise TypeError("Id do cliente deve ser um número inteiro")
        if id_cliente < 0:
            raise ValueError("Id do cliente deve ser positivo")
        self.__especialidade = id_cliente

    def set_senha(self, id_servico):
        if not isinstance(id_servico, int):
            raise TypeError("Id do serviço deve ser um número inteiro")
        if id_servico < 0:
            raise ValueError("Id do serviço deve ser positivo")
        self.__senha = id_servico

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_especialidade(self):
        return self.__especialidade

    def get_senha(self):
        return self.__senha

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome.strftime("%d/%m/%Y %H:%M"),
            "email": self.__email,
            "especialidade": self.__especialidade,
            "senha": self.__senha,
        }

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"],dic["nome"],dic["email"],dic["especialidade"],dic["senha"],)
