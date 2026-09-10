from templates.manterclienteui import ManterClienteUI
from templates.manterconvenioui import ManterConvenioUI
import streamlit as st


class IndexUI:
    @staticmethod
    def main():
        st.title("Sistema de Agendamento de Serviços")
        tab_cliente, tab_convenio = st.tabs(["Clientes", "Convênios"])
        with tab_cliente:
            ManterClienteUI.main()
        with tab_convenio:
            ManterConvenioUI.main()


IndexUI.main()