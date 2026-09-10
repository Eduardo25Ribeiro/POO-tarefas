import streamlit as st
import pandas as pd
from service import Service





class ManterConvenioUI:
    @staticmethod
    def main():
        st.header("Cadastro de Convênios")
        tab1, tab2, tab3, tab4 = st.tabs(
            ["Inserir", "Listar", "Atualizar", "Excluir"]
        )
        with tab1: ManterConvenioUI.convenio_inserir()
        with tab2: ManterConvenioUI.convenio_listar()
        with tab3: ManterConvenioUI.convenio_atualizar()
        with tab4: ManterConvenioUI.convenio_excluir()

    @staticmethod
    def convenio_listar():
        convenios = Service.convenio_listar()
        if not convenios:
            st.write("Nenhum convênio cadastrado.")
            return

        df = pd.DataFrame([convenio.to_json() for convenio in convenios])
        st.dataframe(df, hide_index=True)

    @staticmethod
    def convenio_inserir():
        st.header("Cadastro de Convênio")
        id = st.number_input("Informe o id:", min_value=0, step=1)
        nome = st.text_input("Informe o nome:")
        contato = st.text_input("Informe o e-mail:")
        fone = st.text_input("Informe o telefone:")
        if st.button("Inserir", key="convenio_inserir_button"):
            Service.convenio_inserir(id, nome, contato, fone)
            st.success("Convênio inserido com sucesso!")
            st.write(f"Convênio inserido: {nome}")

    @staticmethod
    def convenio_atualizar():
        convenios = Service.convenio_listar()
        if not convenios:
            st.write("Nenhum convênio cadastrado.")
            return

        convenio = st.selectbox(
            "Atualização de Convenio",
            convenios,
            format_func=str,
        )
        nome = st.text_input("Novo nome", value=convenio.get_nome())
        contato = st.text_input("Novo e-mail", value=convenio.get_contato())
        fone = st.text_input("Novo fone", value=convenio.get_fone())
        if st.button("Atualizar", key="convenio_atualizar_button"):
            Service.convenio_atualizar(convenio.get_id(), nome, contato, fone,)
            st.success("Convênio atualizado com sucesso!")

    @staticmethod
    def convenio_excluir():
        convenios = Service.convenio_listar()
        if not convenios:
            st.write("Nenhum convênio cadastrado.")
            return

        convenio = st.selectbox(
            "Exclusão de Convenios",
            convenios,
            format_func=str,
        )
        if st.button("Excluir", key="convenio_excluir_button"):
            Service.convenio_excluir(convenio.get_id())
            st.success("Convênio excluído com sucesso!")