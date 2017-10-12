class Arquivo(object):

    def __init__(self,nome="",diretorio="",hash="",status=False):
        self.__nome = nome
        self.__diretorio = diretorio
        self.__hash = hash
        self.__status = status

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

    def obterStatus(self):
        return self.__status

    def definirStatus(self,status):
        self.__status=status