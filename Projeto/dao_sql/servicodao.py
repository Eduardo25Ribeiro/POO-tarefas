from models.servico import Servico
from dao_json.dao import DAO

class ServicoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        try:
            sql = """
                INSERT INTO servico (nome, descricao, valor)
                VALUES (?, ?, ?)
            """
            cls.execute(sql, (obj.get_nome(), obj.get_descricao(), obj.get_valor()))
        finally:
            cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        try:
            sql = "SELECT * FROM servico"
            cursor = cls.execute(sql)
            rows = cursor.fetchall()
            return [Servico(id, nome, descricao, valor) for (id, nome, descricao, valor) in rows]
        finally:
            cls.fechar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        try:
            sql = "SELECT * FROM servico WHERE id = ?"
            cursor = cls.execute(sql, (id,))
            row = cursor.fetchone()
            return Servico(*row) if row else None
        finally:
            cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        try:
            sql = """
                UPDATE servico SET nome=?, descricao=?, valor=?
                WHERE id=?
            """
            cls.execute(sql, (obj.get_nome(), obj.get_descricao(), obj.get_valor(), obj.get_id()))
        finally:
            cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        try:
            sql = "DELETE FROM servico WHERE id=?"
            cls.execute(sql, (obj.get_id(),))
        finally:
            cls.fechar()