from datetime import datetime

from models.horario import Horario
from dao_sql.dao import DAO


class HorarioDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = """
                INSERT INTO horario (data, confirmado, id_cliente, id_servico, id_profissional)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor = self.execute(sql, (
                obj.get_data(), obj.get_confirmado(), obj.get_id_cliente(),
                obj.get_id_servico(), obj.get_id_profissional()
            ))
            obj.set_id(cursor.lastrowid)
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            sql = "SELECT * FROM horario"
            rows = self.execute(sql).fetchall()
            return [self._from_row(row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            sql = "SELECT * FROM horario WHERE id = ?"
            row = self.execute(sql, (id,)).fetchone()
            return self._from_row(row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = """
                UPDATE horario SET data=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
                WHERE id=?
            """
            self.execute(sql, (
                obj.get_data(), obj.get_confirmado(), obj.get_id_cliente(),
                obj.get_id_servico(), obj.get_id_profissional(), obj.get_id()
            ))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            sql = "DELETE FROM horario WHERE id=?"
            self.execute(sql, (id,))
        finally:
            self.fechar()

    def _from_row(self, row):
        id, data, confirmado, id_cliente, id_servico, id_profissional = row
        if isinstance(data, str):
            data = datetime.fromisoformat(data)
        horario = Horario(id, data)
        horario.set_confirmado(bool(confirmado))
        horario.set_id_cliente(id_cliente)
        horario.set_id_servico(id_servico)
        horario.set_id_profissional(id_profissional)
        return horario