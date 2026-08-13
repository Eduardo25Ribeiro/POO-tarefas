import streamlit as st
from service import Service
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.cliente_inserir()
            elif op == 2:
                UI.cliente_listar()
            elif op == 3:
                UI.cliente_atualizar()
            elif op == 4:
                UI.cliente_excluir()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(id, nome, email, fone)

    @staticmethod
    def cliente_listar():
        for obj in Service.cliente_listar():
            print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service.cliente_listar():
            print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def cadastrar_cliente():
        st.header("Cadastro de Cliente")

        id = st.number_input("Informe o id: ")
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o telefone: ")

        if st.button("Cadastrar"):
            Service.cliente_inserir(id, nome, email, fone)
            st.write(f"Cliente cadastrado: {nome}")
            st.success("Cliente cadastrado com sucesso!")

    @staticmethod
    def menu_streamlit():
        st.title("Cadastro de Clientes")

        opcao = st.selectbox("Menu", ["Cadastrar cliente", "Sair"], key="menu_opcao")

        if opcao == "Cadastrar cliente":
            UI.cadastrar_cliente()


