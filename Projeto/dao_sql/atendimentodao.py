from datetime import datetime

from models.atendimento import Atendimento
from dao_sql.dao import DAO


class AtendimentoDAO(DAO):
    def inserir(self, obj):
        self.abrir()
        try:
            sql = """
                INSERT INTO atendimento
                    (data, queixa_principal, historico_saude, avaliacao, prescricao,
                     id_horario, total, pago)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor = self.execute(sql, (
                obj.get_data(), obj.get_queixa_principal(), obj.get_historico_saude(),
                obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario(),
                obj.get_total(), obj.get_pago()
            ))
            obj.set_id(cursor.lastrowid)
        finally:
            self.fechar()

    def listar(self):
        self.abrir()
        try:
            sql = "SELECT * FROM atendimento"
            rows = self.execute(sql).fetchall()
            return [self._from_row(row) for row in rows]
        finally:
            self.fechar()

    def listar_id(self, id):
        self.abrir()
        try:
            sql = "SELECT * FROM atendimento WHERE id = ?"
            row = self.execute(sql, (id,)).fetchone()
            return self._from_row(row) if row else None
        finally:
            self.fechar()

    def atualizar(self, obj):
        self.abrir()
        try:
            sql = """
                UPDATE atendimento
                SET data=?, queixa_principal=?, historico_saude=?, avaliacao=?,
                    prescricao=?, id_horario=?, total=?, pago=?
                WHERE id=?
            """
            self.execute(sql, (
                obj.get_data(), obj.get_queixa_principal(), obj.get_historico_saude(),
                obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario(),
                obj.get_total(), obj.get_pago(), obj.get_id()
            ))
        finally:
            self.fechar()

    def excluir(self, id):
        self.abrir()
        try:
            sql = "DELETE FROM atendimento WHERE id=?"
            self.execute(sql, (id,))
        finally:
            self.fechar()

    def _from_row(self, row):
        id, data, queixa_principal, historico_saude, avaliacao, prescricao, \
            id_horario, total, pago = row
        if isinstance(data, str):
            data = datetime.fromisoformat(data)
        return Atendimento(
            id, data, queixa_principal, historico_saude, avaliacao, prescricao,
            id_horario, total, bool(pago)
        )