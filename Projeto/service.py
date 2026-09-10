from models.clientes import Cliente
from models.clientedao import ClienteDAO
from models.convenio import Convenio
from models.convenioDAO import ConvenioDAO


class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone, id_convenio):
        obj = Cliente(id, nome, email, fone, id_convenio)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, id_convenio):
        obj = Cliente(id, nome, email, fone, id_convenio)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    @staticmethod
    def cliente_listar_convenio(id_convenio):
        return [
            cliente
            for cliente in ClienteDAO().listar()
            if cliente.get_id_convenio() == id_convenio
        ]

    @staticmethod
    def cliente_associar_ao_convenio(id, id_convenio):
        cliente = ClienteDAO().listar_id(id)
        if cliente is None:
            raise ValueError("Cliente não encontrado")
        if ConvenioDAO().listar_id(id_convenio) is None:
            raise ValueError("Convênio não encontrado")
        cliente.set_convenio(id_convenio)
        ClienteDAO().atualizar(cliente)

    @staticmethod
    def convenio_inserir(id, nome, contato, fone):
        obj = Convenio(id, nome, contato, fone)
        ConvenioDAO().inserir(obj)

    @staticmethod
    def convenio_listar():
        return ConvenioDAO().listar()

    @staticmethod
    def convenio_listar_id(id):
        return ConvenioDAO().listar_id(id)

    @staticmethod
    def convenio_atualizar(id, nome, contato, fone):
        obj = Convenio(id, nome, contato, fone)
        ConvenioDAO().atualizar(obj)

    @staticmethod
    def convenio_excluir(id):
        ConvenioDAO().excluir(id)
