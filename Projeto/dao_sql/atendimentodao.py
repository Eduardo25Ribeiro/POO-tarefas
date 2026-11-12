from models.atendimento import Atendimento
from dao_json.dao import DAO
import json

class AtendimentoDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO atendimento ( id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario, total, pago)
            VALUES (?, ?, ?, ?, ?, ?, ?, 0, False)
        """
        cls.execute(sql, (obj.get_id(), obj.get_data(), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario()))
        cls.fechar()
    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM atendimento"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario, total, pago) for (id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario, total, pago) in rows]
        cls.fechar()
        return objs
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM atendimento WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Atendimento(*row) if row else None
        cls.fechar()
        return obj
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE atendimento SET nome=?, email=?, fone=?, senha=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_id(), obj.get_data(), obj.get_queixa_principal(), obj.get_historico_saude(), obj.get_avaliacao(), obj.get_prescricao(), obj.get_id_horario(), obj.get_total(), obj.get_pago()))
        cls.fechar()
    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM atendimento WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()