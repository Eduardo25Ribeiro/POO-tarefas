import streamlit as st
from service import Service


class ADMAlterarSenhaUI:
    @staticmethod
    def main():
        st.header("Alterar senha")
        cliente = Service.cliente_listar_id(st.session_state["usuario_id"])
        senha = st.text_input("Nova senha", type="password")
        confirmar = st.text_input("Confirme a nova senha", type="password")
        if st.button("Alterar senha"):
            if not senha:
                st.error("Informe a nova senha.")
            elif senha != confirmar:
                st.error("As senhas não conferem.")
            else:
                Service.cliente_atualizar(
                    cliente.get_id(),
                    cliente.get_nome(),
                    cliente.get_email(),
                    cliente.get_fone(),
                    senha,
                )
                st.success("Senha alterada com sucesso.")
