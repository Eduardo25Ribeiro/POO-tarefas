from dao_sql.dao import DAO
from models.clientes import Cliente


class ClienteDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = """
                INSERT INTO cliente (nome, email, fone, senha)
                VALUES (?, ?, ?, ?)
            """
            cursor = self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(),
                                        obj.get_senha()))
            obj.set_id(cursor.lastrowid)
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            sql = "SELECT * FROM cliente"
            rows = self.execute(sql).fetchall()
            return [Cliente(*row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            sql = "SELECT * FROM cliente WHERE id = ?"
            row = self.execute(sql, (id,)).fetchone()
            return Cliente(*row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = """
                UPDATE cliente SET nome=?, email=?, fone=?, senha=?
                WHERE id=?
            """
            self.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_fone(),
                               obj.get_senha(), obj.get_id()))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            sql = "DELETE FROM cliente WHERE id=?"
            self.execute(sql, (id,))
        finally:
            self.fechar()