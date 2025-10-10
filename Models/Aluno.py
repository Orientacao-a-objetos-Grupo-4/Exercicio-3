from Models.Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.__curso = curso