from models.profissional import Profissional
from dao_sql.dao import DAO


class ProfissionalDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = """
                INSERT INTO profissional (nome, email, especialidade, senha)
                VALUES (?, ?, ?, ?)
            """
            cursor = self.execute(sql, (
                obj.get_nome(), obj.get_email(), obj.get_especialidade(), obj.get_senha()
            ))
            obj.set_id(cursor.lastrowid)
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            sql = "SELECT * FROM profissional"
            rows = self.execute(sql).fetchall()
            return [Profissional(*row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            sql = "SELECT * FROM profissional WHERE id = ?"
            row = self.execute(sql, (id,)).fetchone()
            return Profissional(*row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = """
                UPDATE profissional SET nome=?, email=?, especialidade=?, senha=?
                WHERE id=?
            """
            self.execute(sql, (
                obj.get_nome(), obj.get_email(), obj.get_especialidade(),
                obj.get_senha(), obj.get_id()
            ))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            sql = "DELETE FROM profissional WHERE id=?"
            self.execute(sql, (id,))
        finally:
            self.fechar()