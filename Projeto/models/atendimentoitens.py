class AtendimentoItens:
    def __init__(self, id, id_atendimento, id_servico, qtd, valor):
        self.id = id
        self.id_atendimento = id_atendimento
        self.id_servico = id_servico
        self.qtd = qtd
        self.valor = valor

    def get_id(self): return self.id
    def get_id_atendimento(self): return self.id_atendimento
    def get_id_servico(self): return self.id_servico
    def get_qtd(self): return self.qtd
    def get_valor(self): return self.valor

    def to_json(self):
        return {
            "id": self.id,
            "id_atendimento": self.id_atendimento,
            "id_servico": self.id_servico,
            "qtd": self.qtd,
            "valor": self.valor,
        }

    @staticmethod
    def from_json(dic):
        return AtendimentoItens(
            dic["id"],
            dic["id_atendimento"],
            dic["id_servico"],
            dic["qtd"],
            dic["valor"],
        )

    def __str__(self):
        return f"{self.id} - {self.id_servico} - {self.qtd} - {self.valor}"
