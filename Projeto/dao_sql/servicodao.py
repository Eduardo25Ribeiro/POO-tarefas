from models.servico import Servico
from dao_sql.dao import DAO

class ServicoDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = """
                INSERT INTO servico (descricao, valor)
                VALUES (?, ?)
            """
            cursor = self.execute(sql, (obj.get_descricao(), obj.get_valor()))
            obj.set_id(cursor.lastrowid)
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            sql = "SELECT * FROM servico"
            cursor = self.execute(sql)
            rows = cursor.fetchall()
            return [Servico(*row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            sql = "SELECT * FROM servico WHERE id = ?"
            cursor = self.execute(sql, (id,))
            row = cursor.fetchone()
            return Servico(*row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = """
                UPDATE servico SET descricao=?, valor=?
                WHERE id=?
            """
            self.execute(sql, (obj.get_descricao(), obj.get_valor(), obj.get_id()))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            sql = "DELETE FROM servico WHERE id=?"
            self.execute(sql, (id,))
        finally:
            self.fechar()