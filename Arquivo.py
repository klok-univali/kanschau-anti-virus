class Arquivo(object):

    def __init__(self,nome="",diretorio="",hash=""):
        self.__nome = nome
        self.__diretorio = diretorio
        self.__hash = hash

    def obterNome(self):
        return self.__nome

    def definirNome(self,nome):
        self.__nome = nome

    def obterDiretorio(self):
        return self.__diretorio

    def definirDiretorio(self,diretorio):
        self.__diretorio = diretorio

    def obterHash(self):
        return self.__hash

    def definirHash(self,hash):
        self.__hash = hash