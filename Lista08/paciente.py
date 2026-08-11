

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    
    def idade(self):
        from datetime import datetime
       
        hoje = datetime.now()
        idade = hoje.year - self.__nascimento.year - ((hoje.month, hoje.day) < (self.__nascimento.month, self.__nascimento.day))
        return idade
    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Telefone: {self.__telefone}, Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"