from models.clientes import Cliente
from models.clientedao import ClienteDAO
from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO
from models.atendimento import Atendimento
from models.atendimentoDAO import AtendimentoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO


class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    @staticmethod
    def profissional_inserir(id, nome, email, especialidade):
        obj = Profissional(id, nome, email, especialidade)
        ProfissionalDAO().inserir(obj)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade):
        obj = Profissional(id, nome, email, especialidade)
        ProfissionalDAO().atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)

    @staticmethod
    def atendimento_inserir(id, cliente, profissional, servico, horario):
        obj = Atendimento(id, cliente, profissional, servico, horario)
        AtendimentoDAO().inserir(obj)

    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()

    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)

    @staticmethod
    def atendimento_atualizar(id, cliente, profissional, servico, horario):
        obj = Atendimento(id, cliente, profissional, servico, horario)
        AtendimentoDAO().atualizar(obj)

    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)

    @staticmethod
    def horario_inserir(id, data, hora):
        obj = Horario(id, data, hora)
        HorarioDAO().inserir(obj)

    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()

    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)

    @staticmethod
    def horario_atualizar(id, data, hora):
        obj = Horario(id, data, hora)
        HorarioDAO().atualizar(obj)

    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id)
