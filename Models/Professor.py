from Models.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, idade, materia, contratacao):
        super().__init__(nome, idade)
        self.__materia = materia
        self.__contratacao = contratacao

    def getMateria(self):
        return self.__materia

    def getContratacao(self):
        return self.__contratacao

    def setMateria(self, materia):
        self.__materia = materia

    def setContratacao(self, contratacao):
        self.__contratacao = contratacao
