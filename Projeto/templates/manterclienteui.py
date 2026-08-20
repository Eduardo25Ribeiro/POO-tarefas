import streamlit as st
import pandas as pd
import time
from service import Service





class ManterClienteUI:
    def main():
        st.header("Cadrastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inserir", "Listar", "Atualizar", "Excluir"]
        )
        with tab1: ManterClienteUI.cliente_inserir()
        with tab2: ManterClienteUI.cliente_listar()
        with tab3: ManterClienteUI.cliente_atualizar()
        with tab4: ManterClienteUI.cliente_excluir()

    @staticmethod
    def cliente_listar():
        clientes = Service.cliente_listar()
        if not clientes:
            st.write("Nenhum cliente cadastrado.")
            return

        df = pd.DataFrame([cliente.to_json() for cliente in clientes])
        st.dataframe(df, hide_index=True)

    @staticmethod
    def cliente_inserir():
        st.header("Cadastro de Cliente")
        id = st.number_input("Informe o id:", min_value=0, step=1)
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o e-mail:")
        fone = st.text_input("Informe o telefone:")
        if st.button("Inserir"):
            Service.cliente_inserir(id, nome, email, fone)
            st.success("Cliente inserido com sucesso!")
            st.write(f"Cliente inserido: {nome}")

    @staticmethod
    def cliente_atualizar():
        clientes = Service.cliente_listar()
        if not clientes:
            st.write("Nenhum cliente cadastrado.")
            return

        cliente = st.selectbox(
            "Atualização de Clientes",
            clientes,
            format_func=str,
        )
        nome = st.text_input("Novo nome", value=cliente.get_nome())
        email = st.text_input("Novo e-mail", value=cliente.get_email())
        fone = st.text_input("Novo fone", value=cliente.get_fone())
        if st.button("Atualizar"):
            Service.cliente_atualizar(cliente.get_id(), nome, email, fone)
            st.success("Cliente atualizado com sucesso!")

    @staticmethod
    def cliente_excluir():
        clientes = Service.cliente_listar()
        if not clientes:
            st.write("Nenhum cliente cadastrado.")
            return

        cliente = st.selectbox(
            "Exclusão de Clientes",
            clientes,
            format_func=str,
        )
        if st.button("Excluir"):
            Service.cliente_excluir(cliente.get_id())
            st.success("Cliente excluído com sucesso!")