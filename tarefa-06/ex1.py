from enum import Enum
from datetime import datetime


class Grupo(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12


class Fase(Enum):
    GRUPOS = 1
    DEZESSEIS_AVOS = 2
    OITAVAS = 3
    QUARTAS = 4
    SEMIFINAIS = 5
    TERCEIRO_LUGAR = 6
    FINAL = 7


GRUPOS_COPA = {
    Grupo.A: ["México", "África do Sul", "Coreia do Sul", "Tchéquia"],
    Grupo.B: ["Canadá", "Suíça", "Catar", "Bósnia e Herzegovina"],
    Grupo.C: ["Brasil", "Marrocos", "Escócia", "Haiti"],
    Grupo.D: ["Estados Unidos", "Paraguai", "Austrália", "Turquia"],
    Grupo.E: ["Alemanha", "Equador", "Costa do Marfim", "Curaçao"],
    Grupo.F: ["Países Baixos", "Japão", "Suécia", "Tunísia"],
    Grupo.G: ["Bélgica", "Egito", "Irã", "Nova Zelândia"],
    Grupo.H: ["Espanha", "Uruguai", "Arábia Saudita", "Cabo Verde"],
    Grupo.I: ["França", "Senegal", "Noruega", "Iraque"],
    Grupo.J: ["Argentina", "Áustria", "Argélia", "Jordânia"],
    Grupo.K: ["Portugal", "Colômbia", "República Democrática do Congo", "Uzbequistão"],
    Grupo.L: ["Inglaterra", "Croácia", "Gana", "Panamá"]
}


class Pais:
    def __init__(self, id: int, nome: str, sigla: str, grupo: Grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("ID deve ser maior que zero.")
        self.id = id

    def set_nome(self, nome):
        if nome.strip() == "":
            raise ValueError("Nome não pode ser vazio.")
        self.nome = nome

    def set_sigla(self, sigla):
        if len(sigla.strip()) != 3:
            raise ValueError("A sigla deve possuir 3 letras.")
        self.sigla = sigla.upper()

    def set_grupo(self, grupo):
        if not isinstance(grupo, Grupo):
            raise ValueError("Grupo inválido.")
        self.grupo = grupo

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_sigla(self):
        return self.sigla

    def get_grupo(self):
        return self.grupo

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Nome: {self.nome} | "
            f"Sigla: {self.sigla} | "
            f"Grupo: {self.grupo.name}"
        )


class Jogo:
    def __init__(
        self,
        id: int,
        id_pais1: int,
        id_pais2: int,
        gols1: int,
        gols2: int,
        fase: Fase,
        data_hora: datetime
    ):
        self.set_id(id)
        self.set_id_pais1(id_pais1)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("ID deve ser maior que zero.")
        self.id = id

    def set_id_pais1(self, id_pais1):
        if id_pais1 <= 0:
            raise ValueError("ID do país 1 inválido.")
        self.id_pais1 = id_pais1

    def set_id_pais2(self, id_pais2):
        if id_pais2 <= 0:
            raise ValueError("ID do país 2 inválido.")
        self.id_pais2 = id_pais2

    def set_gols1(self, gols1):
        if gols1 < 0:
            raise ValueError("Gols não podem ser negativos.")
        self.gols1 = gols1

    def set_gols2(self, gols2):
        if gols2 < 0:
            raise ValueError("Gols não podem ser negativos.")
        self.gols2 = gols2

    def set_fase(self, fase):
        if not isinstance(fase, Fase):
            raise ValueError("Fase inválida.")
        self.fase = fase

    def set_data_hora(self, data_hora):
        if not isinstance(data_hora, datetime):
            raise ValueError("Data inválida.")
        self.data_hora = data_hora

    def get_id(self):
        return self.id

    def get_id_pais1(self):
        return self.id_pais1

    def get_id_pais2(self):
        return self.id_pais2

    def get_gols1(self):
        return self.gols1

    def get_gols2(self):
        return self.gols2

    def get_fase(self):
        return self.fase

    def get_data_hora(self):
        return self.data_hora

    def __str__(self):
        return (
            f"Jogo {self.id} | "
            f"País 1: {self.id_pais1} | "
            f"País 2: {self.id_pais2} | "
            f"Placar: {self.gols1} x {self.gols2} | "
            f"Fase: {self.fase.name} | "
            f"Data: {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
        )


class UI:

    @staticmethod
    def listar_grupos():
        print("\n=== GRUPOS DA COPA ===\n")

        for grupo, paises in GRUPOS_COPA.items():
            print(f"GRUPO {grupo.name}")
            for pais in paises:
                print(f" - {pais}")
            print()

    @staticmethod
    def listar_fases():
        print("\n=== FASES ===\n")

        for fase in Fase:
            print(f"{fase.value} - {fase.name}")

    @staticmethod
    def menu():
        while True:
            print("\n=== SISTEMA COPA DO MUNDO ===")
            print("1 - Listar grupos")
            print("2 - Listar fases")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                UI.listar_grupos()

            elif opcao == "2":
                UI.listar_fases()

            elif opcao == "0":
                print("Encerrando...")
                break

            else:
                print("Opção inválida.")


if __name__ == "__main__":
    UI.menu()