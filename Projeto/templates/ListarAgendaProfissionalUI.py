import streamlit as st
import pandas as pd
from service import Service

class ListarAgendaProfissionalUI:
    def main():
        st.header("Agenda do Profissional")
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profissionais)
            horarios = Service.profissional_visualizar_agenda(profissional.get_id())
            if len(horarios) == 0:
                st.write("Nenhum horário cadastrado para este profissional")
                return
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({"id" : obj.get_id(),
                "data" : obj.get_data().strftime("%d/%m/%Y"),
                "hora" : obj.get_data().strftime("%H:%M"),
                "nome_do_client" : cliente,
                "descricao_do_servico" : servico})
            df = pd.DataFrame(dic)
            st.dataframe(df)