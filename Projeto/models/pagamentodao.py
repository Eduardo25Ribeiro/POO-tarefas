import json
from models.pagamento import Pagamento


class PagamentoDAO:
    def __init__(self):
        self.__arquivo = "pagamentos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        id = 0
        for aux in self.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.id = id + 1
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def __abrir(self):
        try:
            with open(self.__arquivo, mode="r") as arquivo:
                list_dic = json.load(arquivo)
                self.__objetos = [Pagamento.from_json(dic) for dic in list_dic]
        except FileNotFoundError:
            self.__objetos = []

    def __salvar(self):
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump([obj.to_json() for obj in self.__objetos], arquivo, indent=2)
