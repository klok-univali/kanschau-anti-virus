import os

class Varredura(object):

    def __init__(self):
        self.__arquivos = []
        self.__numeroLido = 0

    def capturarArquivos(self,diretorio):
       self.limparDados()
       itens = os.listdir(os.path.expanduser(diretorio))
       for item in itens:
           if(os.path.isfile(diretorio + item)):
               self.__arquivos.append(str(diretorio + item).replace(" ","\ ").replace("(","\(").replace(")","\)"))
               self.__numeroLido+=1
           if(os.path.isdir(diretorio + item)):
               self.capturarArquivos(diretorio + item + '/')

    def obterArquivosCapturados(self):
        return self.__arquivos

    def limparDados(self):
        self.__numeroLido = 0
        self.__arquivos = []

    def obterNumeroLido(self):
        return self.__numeroLido