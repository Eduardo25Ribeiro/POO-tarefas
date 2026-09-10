import streamlit as st
import pandas as pd
import time
from service import Service





class ManterProfissionalUI:
    def main():
        st.header("Cadrastro de Serviço")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inserir", "Listar", "Atualizar", "Excluir"]
        )
        with tab1: ManterProfissionalUI.servico_inserir()
        with tab2: ManterProfissionalUI.servico_listar()
        with tab3: ManterProfissionalUI.servico_atualizar()
        with tab4: ManterProfissionalUI.servico_excluir()

    @staticmethod
    def profissional_listar():
        servico = Service.servico_listar()
        if not servico:
            st.write("Nenhum serviço cadastrado.")
            return

        df = pd.DataFrame([servico.to_json() for servico in servico])
        st.dataframe(df, hide_index=True)

    @staticmethod
    def profissional_inserir():
        st.header("Cadastro de Profissional")
        id = st.number_input("Informe o id:", min_value=0, step=1)
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o e-mail:")
        fone = st.text_input("Informe o telefone:")
        if st.button("Inserir"):
            Service.servico_inserir(id, nome, email, fone)
            st.success("Profissional inserido com sucesso!")
            st.write(f"Profissional inserido: {nome}")

    @staticmethod
    def profissional_atualizar():
        servicos = Service.servico_listar()
        if not servicos:
            st.write("Nenhum Profissional cadastrado.")
            return

        servico = st.selectbox(
            "Atualização de Profissional",
            servicos,
            format_func=str,
        )
        nome = st.text_input("Novo nome", value=servico.get_nome())
        email = st.text_input("Novo e-mail", value=servico.get_email())
        fone = st.text_input("Novo fone", value=servico.get_fone())
        if st.button("Atualizar"):
            Service.convenio_atualizar(servico.get_id(), nome, email, fone)
            st.success("Profissional atualizado com sucesso!")

    @staticmethod
    def profissional_excluir():
        servicos = Service.servico_listar()
        if not servicos:
            st.write("Nenhum Profissional cadastrado.")
            return

        servico = st.selectbox(
            "Exclusão de Profissionais",
            servicos,
            format_func=str,
        )
        if st.button("Excluir"):
            Service.servico_excluir(servico.get_id())
            st.success("Profissional excluído com sucesso!")