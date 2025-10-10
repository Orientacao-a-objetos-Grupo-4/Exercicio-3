from Models.Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, escolaridade, naturalidade, materia):
        super().__init__(nome, idade, escolaridade, naturalidade)
        self.__materia = materia
        self.__contratacao = None

    def getMateria(self):
        return self.__materia

    def getContratacao(self):
        return self.__contratacao

    def setMateria(self, materia):
        self.__materia = materia

    def setContratacao(self, contratacao):
        self.__contratacao = contratacao
