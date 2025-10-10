from Models.Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.__matricula = matricula
        self.__curso = curso

    def getMatricula(self):
        return self.__matricula

    def getCurso(self):
        return self.__curso

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def setCurso(self, curso):
        self.__curso = curso
