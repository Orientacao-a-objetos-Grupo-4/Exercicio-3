
class Pessoa:
    def __init__(self, nome, idade, escolaridade, naturalidade):
        self.__nome = nome
        self.__idade = idade
        self.__escolaridade = escolaridade
        self.__naturalidade = naturalidade

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getEscolaridade(self):
        return self.__escolaridade

    def getNaturalidade(self):
        return self.__naturalidade

    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setEscolaridade(self, escolaridade):
        self.__escolaridade = escolaridade

    def setNaturalidade(self, naturalidade):
        self.__naturalidade = naturalidade