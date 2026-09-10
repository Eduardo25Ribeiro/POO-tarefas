import streamlit as st
import pandas as pd
import time
from service import Service





class ManterHorarioUI:
    def main():
        st.header("Cadrastro de Serviço")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inserir", "Listar", "Atualizar", "Excluir"]
        )
        with tab1: ManterHorarioUI.servico_inserir()
        with tab2: ManterHorarioUI.servico_listar()
        with tab3: ManterHorarioUI.servico_atualizar()
        with tab4: ManterHorarioUI.servico_excluir()

    @staticmethod
    def servico_listar():
        servico = Service.servico_listar()
        if not servico:
            st.write("Nenhum serviço cadastrado.")
            return

        df = pd.DataFrame([servico.to_json() for servico in servico])
        st.dataframe(df, hide_index=True)

    @staticmethod
    def servico_inserir():
        st.header("Cadastro de Serviços")
        id = st.number_input("Informe o id:", min_value=0, step=1)
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o e-mail:")
        fone = st.text_input("Informe o telefone:")
        if st.button("Inserir"):
            Service.servico_inserir(id, nome, email, fone)
            st.success("Serviço inserido com sucesso!")
            st.write(f"Serviço inserido: {nome}")

    @staticmethod
    def servico_atualizar():
        servicos = Service.servico_listar()
        if not servicos:
            st.write("Nenhum Serviço cadastrado.")
            return

        servico = st.selectbox(
            "Atualização de Serviço",
            servicos,
            format_func=str,
        )
        nome = st.text_input("Novo nome", value=servico.get_nome())
        email = st.text_input("Novo e-mail", value=servico.get_email())
        fone = st.text_input("Novo fone", value=servico.get_fone())
        if st.button("Atualizar"):
            Service.convenio_atualizar(servico.get_id(), nome, email, fone)
            st.success("Serviço atualizado com sucesso!")

    @staticmethod
    def servico_excluir():
        servicos = Service.servico_listar()
        if not servicos:
            st.write("Nenhum cliente cadastrado.")
            return

        servico = st.selectbox(
            "Exclusão de Serviços",
            servicos,
            format_func=str,
        )
        if st.button("Excluir"):
            Service.servico_excluir(servico.get_id())
            st.success("Serviço excluído com sucesso!")