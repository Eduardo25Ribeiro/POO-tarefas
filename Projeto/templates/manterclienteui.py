import streamlit as st
import pandas as pd
from service import Service


class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inserir", "Listar", "Atualizar", "Excluir"]
        )
        with tab1: ManterClienteUI.cliente_inserir()
        with tab2: ManterClienteUI.cliente_listar()
        with tab3: ManterClienteUI.cliente_atualizar()
        with tab4: ManterClienteUI.cliente_excluir()

    @staticmethod
    def _selecionar_convenio(label, key):
        convenios = Service.convenio_listar()
        if not convenios:
            st.warning("Cadastre um convênio antes de continuar.")
            return None
        return st.selectbox(label, convenios, format_func=str, key=key)

    @staticmethod
    def cliente_inserir():
        id = st.number_input("Informe o id:", min_value=0, step=1, key="cliente_id")
        nome = st.text_input("Informe o nome:", key="cliente_nome")
        email = st.text_input("Informe o e-mail:", key="cliente_email")
        fone = st.text_input("Informe o telefone:", key="cliente_fone")
        convenio = ManterClienteUI._selecionar_convenio(
            "Selecione o convênio:", "cliente_convenio"
        )
        if st.button("Inserir cliente", key="cliente_inserir_button"):
            if convenio is None:
                return
            Service.cliente_inserir(id, nome, email, fone, convenio.get_id())
            st.success("Cliente inserido com sucesso!")

    @staticmethod
    def cliente_listar():
        clientes = Service.cliente_listar()
        if not clientes:
            st.write("Nenhum cliente cadastrado.")
            return
        registros = []
        for cliente in clientes:
            registro = cliente.to_json()
            convenio = Service.convenio_listar_id(cliente.get_id_convenio())
            registro["convenio"] = convenio.get_nome() if convenio else "Não informado"
            registros.append(registro)
        df = pd.DataFrame(registros)
        st.dataframe(df, hide_index=True)

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
        convenio = ManterClienteUI._selecionar_convenio(
            "Novo convênio:", "cliente_atualizar_convenio"
        )
        if st.button("Atualizar", key="cliente_atualizar_button"):
            if convenio is None:
                return
            Service.cliente_atualizar(
                cliente.get_id(), nome, email, fone, convenio.get_id()
            )
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
        if st.button("Excluir", key="cliente_excluir_button"):
            Service.cliente_excluir(cliente.get_id())
            st.success("Cliente excluído com sucesso!")