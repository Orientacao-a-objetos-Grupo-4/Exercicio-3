class Curso:
    def __init__(self, nome, escola, coordenacao):
        self.__nome = nome
        self.__escola = escola
        self.__coordenacao = coordenacao
        self.__tipoEnsino = None

    def getNome(self):
        return self.__nome

    def getEscola(self):
        return self.__escola

    def getCoordenacao(self):
        return self.__coordenacao

    def getTipoEnsino(self):
        return self.__tipoEnsino

    def setNome(self, nome):
        self.__nome = nome

    def setEscola(self, escola):
        self.__escola = escola

    def setCoordenacao(self, coordenacao):
        self.__coordenacao = coordenacao

    def setTipoEnsino(self, tipoEnsino):
        self.__tipoEnsino = tipoEnsino
