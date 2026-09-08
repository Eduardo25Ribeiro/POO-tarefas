import streamlit as st
import pandas as pd
import time
from service import Service





class ManterAtendimentoUI:
    def main():
        st.header("Cadrastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inserir", "Listar", "Atualizar", "Excluir"]
        )
        with tab1: ManterAtendimentoUI.cliente_inserir()
        with tab2: ManterAtendimentoUI.atendimento_listar()
        with tab3: ManterAtendimentoUI.atendimento_atualizar()
        with tab4: ManterAtendimentoUI.cliente_excluir()

    @staticmethod
    def atendimento_listar():
        clientes = Service.cliente_listar()
        if not clientes:
            st.write("Nenhum cliente cadastrado.")
            return

        df = pd.DataFrame([cliente.to_json() for cliente in clientes])
        st.dataframe(df, hide_index=True)

    @staticmethod
    def atendimento_inserir():
        st.header("Cadastro de Atendimento")
        id = st.number_input("Informe o id:", min_value=0, step=1)
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o e-mail:")
        fone = st.text_input("Informe o telefone:")
        if st.button("Inserir"):
            Service.cliente_inserir(id, nome, email, fone)
            st.success("Atendimento inserido com sucesso!")
            st.write(f"Atendimento inserido: {nome}")

    @staticmethod
    def atendimento_atualizar():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum Atendimento cadastrado.")
            return

        cliente = st.selectbox(
            "Atualização de Clientes",
            atendimentos,
            format_func=str,
        )
        nome = st.text_input("Novo nome", value=cliente.get_nome())
        email = st.text_input("Novo e-mail", value=cliente.get_email())
        fone = st.text_input("Novo fone", value=cliente.get_fone())
        if st.button("Atualizar"):
            Service.cliente_atualizar(cliente.get_id(), nome, email, fone)
            st.success("Atendimento atualizado com sucesso!")

    @staticmethod
    def cliente_excluir():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum Atendimento cadastrado.")
            return

        cliente = st.selectbox(
            "Exclusão de Atendimentos",
            atendimentos,
            format_func=str,
        )
        if st.button("Excluir"):
            Service.cliente_excluir(cliente.get_id())
            st.success("Atendimentos excluído com sucesso!")