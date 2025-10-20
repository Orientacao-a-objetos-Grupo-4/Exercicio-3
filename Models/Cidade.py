class Cidade:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    def getCidade(self):
        return self.__cidade

    def getEstado(self):
        return self.__estado

    def setCidade(self, estado):
        self.__estado = estado

    def setEstado(self, estado):
        self.__estado = estado