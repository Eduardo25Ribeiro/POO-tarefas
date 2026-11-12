import json
from models.horario import Horario
from dao_json.dao import DAO



class HorarioDAO(DAO):
    def __init__(self):
        super().__init__("horarios.json")

    
    
    def _abrir(self):
        try:
            with open(self._arquivo, mode="r") as arquivo:
                list_dic = json.load(arquivo)
                self._objetos = [Horario.from_json(dic) for dic in list_dic]
        except FileNotFoundError:
            self._objetos = []

    def _salvar(self):
        with open(self._arquivo, mode="w") as arquivo:
            json.dump([obj.to_json() for obj in self._objetos], arquivo, indent=2)
