class Cliente:
    def __init__(self, id, nome, email, fone, senha, id_convenio=None):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
        self.set_id_convenio(id_convenio)

    def set_id(self, id):
        if id < 0:
            raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome deve ser informado")
        self.__nome = nome

    def set_email(self, email):
        if email == "":
            raise ValueError("E-mail deve ser informado")
        self.__email = email

    def set_fone(self, fone):
        if fone == "":
            raise ValueError("Fone deve ser informado")
        self.__fone = fone

    def set_senha(self, senha):
        if senha is None or senha == "":
            raise ValueError("Senha deve ser informada")
        self.__senha = senha

    def set_id_convenio(self, id_convenio):
        self.__id_convenio = id_convenio

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def get_senha(self):
        return self.__senha

    def get_id_convenio(self):
        return self.__id_convenio

    def to_json(self):
        return {"id": self.__id,"nome": self.__nome,"email": self.__email,"fone": self.__fone,"senha": self.__senha,"id_convenio": self.__id_convenio}

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"],dic["nome"],dic["email"],dic["fone"],dic.get("senha"),dic.get("id_convenio"))

    def __str__(self):
        return (f"{self.__id}-{self.__nome}-{self.__email}-"f"{self.__fone}-convênio:{self.__id_convenio}")
