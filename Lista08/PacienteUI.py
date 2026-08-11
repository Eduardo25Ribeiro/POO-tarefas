import streamlit as st
from datetime import datetime
from paciente import Paciente


class PacienteUI:

    @staticmethod
    def main():
        st.header("Cadastro de Paciente")

        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")
        nascimento = st.text_input("Nascimento (dd/mm/aaaa)")

        if st.button("Cadastrar"):
            paciente = Paciente(str(nome), str(cpf), str(telefone), datetime.strptime(nascimento, "%d/%m/%Y"))

            st.write(f"Paciente cadastrado: {paciente}")
            st.write(f"Idade: {paciente.idade()} anos")