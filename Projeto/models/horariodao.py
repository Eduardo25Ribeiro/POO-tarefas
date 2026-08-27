import json
from models.horario import horario



class ServicoDAO:
    def __init__(self):
        self.__arquivo = "servicos.json"
        self.__objetos = []
        self.__abrir()
    
    def inserir(self, obj):
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux is not None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux is not None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):
        try:
            with open(self.__arquivo, mode="r") as arquivo:
                list_dic = json.load(arquivo)
                self.__objetos = [horario.from_json(dic) for dic in list_dic]
        except FileNotFoundError:
            self.__objetos = []

    def __salvar(self):
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump([obj.to_json() for obj in self.__objetos], arquivo, indent=2)
