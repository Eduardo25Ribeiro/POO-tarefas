from datetime import datetime


class Pagamento:

  def __init__(self, id, id_atendimento, id_cliente, valor, data, forma):
    self.id = id
    self.id_atendimento = id_atendimento
    self.id_cliente = id_cliente
    self.valor = valor
    self.data = data
    self.forma = forma

  def get_id(self):
    return self.id

  def get_id_atendimento(self):
    return self.id_atendimento

  def get_id_cliente(self):
    return self.id_cliente

  def get_valor(self):
    return self.valor

  def get_data(self):
    return self.data

  def get_forma(self):
    return self.forma

  def to_json(self):
    return {
        "id": self.id,
        "id_atendimento": self.id_atendimento,
        "id_cliente": self.id_cliente,
        "valor": self.valor,
        "data": self.data.strftime("%d/%m/%Y %H:%M"),
        "forma": self.forma,
    }

  @staticmethod
  def from_json(dic):
    return Pagamento(
        dic["id"],
        dic["id_atendimento"],
        dic["id_cliente"],
        dic["valor"],
        datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"),
        dic["forma"],
    )