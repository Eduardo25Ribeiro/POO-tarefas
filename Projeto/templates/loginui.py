import streamlit as st
from service import Service

class LoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("Informe a senha", type="password")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = Service.cliente_autenticar(email,senha)
            if c == None: st.write("Email ou senha invalidos")
            else:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuaruio_nome"] = c["nome"]
                st.rerun()