class Escola:
    def __init__(self, nome, direcao, cidade):
        self.__nome = nome
        self.__direcao = direcao
        self.__cidade = cidade

    def getNome(self):
        return self.__nome

    def getDirecao(self):
        return self.__direcao

    def getCidade(self):
        return self.__cidade

    def setNome(self, nome):
        self.__nome = nome

    def setDirecao(self, direcao):
        self.__direcao = direcao

    def setCidade(self, cidade):
        self.__cidade = cidade
