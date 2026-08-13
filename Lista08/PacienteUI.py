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
            paciente = Paciente(str(nome), str(cpf), str(telefone), datetime.strptime(nascimento, "%d/%m/%Y").date())
            st.write(f"Paciente cadastrado: {paciente}")
            st.write(f"Idade: {paciente.idade()} anos")
            st.success("Paciente cadastrado com sucesso!")

    @staticmethod
    def menu():
        st.title("Cadastro de Pacientes")

        opcao = st.selectbox("Menu", ["Cadastrar paciente", "Sair"])

        if opcao == "Cadastrar paciente":
            PacienteUI.main()