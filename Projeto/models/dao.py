from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, arquivo):
        self._arquivo = arquivo
        self._objetos = []
        self._abrir()

    @abstractmethod
    def _abrir(self):
        pass
    @abstractmethod
    def _salvar(self):
        pass

    def inserir(self, obj):
        self._objetos.append(obj)
        self._salvar()

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