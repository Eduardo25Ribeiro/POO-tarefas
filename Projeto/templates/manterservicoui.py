
import streamlit as st
import pandas as pd
import time
from service import Service


class ManterServicoUI:
    def main():
        st.header("Cadrastro de Serviço")
        tab1, tab2, tab3, tab4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.servico_inserir()
        with tab2: ManterServicoUI.servico_listar()
        with tab3: ManterServicoUI.servico_atualizar()
        with tab4: ManterServicoUI.servico_excluir()

    @staticmethod
    def servico_listar():
        servicos = Service.servico_listar()
        if not servicos:
            st.write("Nenhum serviço cadastrado.")
            return

        df = pd.DataFrame([servico.to_json() for servico in servicos])
        st.dataframe(df, hide_index=True)

    @staticmethod
    def servico_inserir():
        st.header("Cadastro de Serviços")
        descricao = st.text_input("Informe a descrição:")
        valor = st.number_input("Informe o valor:", min_value=0, step=1)
        if st.button("Inserir"):
            Service.servico_inserir(descricao, valor)
            st.success("Serviço inserido com sucesso!")
            st.write(f"Serviço inserido: {descricao}")

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
        descricao = st.text_input("Nova descrição", value=servico.get_descricao())
        valor = st.number_input("Novo valor", min_value=0, value=servico.get_valor(), step=1)
        if st.button("Atualizar"):
            Service.servico_atualizar(servico.get_id(), descricao, valor)
            st.success("Serviço atualizado com sucesso!")

    @staticmethod
    def servico_excluir():
        servicos = Service.servico_listar()
        if not servicos:
            st.write("Nenhum serviço cadastrado.")
            return

        servico = st.selectbox(
            "Exclusão de Serviços",
            servicos,
            format_func=str,
        )
        if st.button("Excluir"):
            Service.servico_excluir(servico.get_id())
            st.success("Serviço excluído com sucesso!")
