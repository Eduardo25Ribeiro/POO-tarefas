import streamlit as st
import pandas as pd
import time
from service import Service


class ManterAtendimentoUI:
    @staticmethod
    def main():
        st.header("Cadrastro de Atendimentos")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inserir", "Listar", "Atualizar", "Excluir"]
        )
        with tab1: ManterAtendimentoUI.atendimento_inserir()
        with tab2: ManterAtendimentoUI.atendimento_listar()
        with tab3: ManterAtendimentoUI.atendimento_atualizar()
        with tab4: ManterAtendimentoUI.atendimento_excluir()

    @staticmethod
    def atendimento_listar():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum atendimento cadastrado.")
            return

        df = pd.DataFrame([atendimento.to_json() for atendimento in atendimentos])
        st.dataframe(df, hide_index=True)

    @staticmethod
    def atendimento_inserir():
        st.header("Cadastro de Atendimento")
        data = st.date_input("Informe a data:")
        queixa_principal = st.text_input("Informe a queixa principal:")
        historico_saude = st.text_area("Informe o histórico de saúde:")
        avaliacao = st.text_area("Informe a avaliação:")
        prescricao = st.text_area("Informe a prescrição:")
        id_horario = st.number_input("Informe o id do horário:", min_value=0, step=1)

        if st.button("Inserir"):
            Service.atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            st.success("Atendimento inserido com sucesso!")
            st.write(f"Atendimento inserido: {queixa_principal}")

    @staticmethod
    def atendimento_atualizar():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum Atendimento cadastrado.")
            return

        atendimento = st.selectbox(
            "Atualização de Atendimentos",
            atendimentos,
            format_func=str,
        )
        data = st.date_input("Nova data", value=atendimento.get_data())
        queixa_principal = st.text_input("Nova queixa principal", value=atendimento.get_queixa_principal())
        historico_saude = st.text_area("Novo histórico de saúde", value=atendimento.get_historico_saude())
        avaliacao = st.text_area("Nova avaliação", value=atendimento.get_avaliacao())
        prescricao = st.text_area("Nova prescrição", value=atendimento.get_prescricao())
        id_horario = st.number_input("Novo id do horário", min_value=0, step=1, value=atendimento.get_id_horario())

        if st.button("Atualizar"):
            Service.atendimento_atualizar(atendimento.get_id(), data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
            st.success("Atendimento atualizado com sucesso!")

    @staticmethod
    def atendimento_excluir():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum Atendimento cadastrado.")
            return

        atendimento = st.selectbox(
            "Exclusão de Atendimentos",
            atendimentos,
            format_func=str,
        )
        if st.button("Excluir"):
            Service.atendimento_excluir(atendimento.get_id())
            st.success("Atendimento excluído com sucesso!")
