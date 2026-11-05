import json
from models.clientes import Cliente
from models.dao import DAO


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__("clientes.json")

    def inserir(self, obj):
        proximo_id = max(
            (cliente.get_id() for cliente in self._objetos),
            default=0,
        ) + 1
        obj.set_id(proximo_id)
        super().inserir(obj)

    def listar(self):
        return self._objetos

    def listar_id(self, id):
        for obj in self._objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux is not None:
            self._objetos.remove(aux)
            self._objetos.append(obj)
            self._salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux is not None:
            self._objetos.remove(aux)
            self._salvar()

    def _abrir(self):
        try:
            with open(self._arquivo, mode="r") as arquivo:
                list_dic = json.load(arquivo)
                self._objetos = [Cliente.from_json(dic) for dic in list_dic]
        except FileNotFoundError:
            self._objetos = []

    def _salvar(self):
        with open(self._arquivo, mode="w") as arquivo:
            json.dump([obj.to_json() for obj in self._objetos], arquivo, indent=2)
