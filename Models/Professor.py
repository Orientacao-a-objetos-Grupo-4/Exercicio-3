from Models.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, idade, materia, contratacao):
        super().__init__(nome, idade)
        self.__materia = materia
        self.__contratacao = contratacao