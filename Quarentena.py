import os
from persistencia.Serializacao import Serializacao
from persistencia.Armazenamento import Armazenamento

class Quarentena(object):

    def __init__(self):

        if os.path.exists("bases/Base_Quarentena"):
            self.__arquivosQuarentena = Serializacao.recuperarSerializado(Armazenamento.recuperarObjetoSerializao("bases/Base_Quarentena"))
        else:
            self.__arquivosQuarentena = []

        if os.path.exists("bases/Base_Ignorados"):
            self.__arquivosIgnorados = Serializacao.recuperarSerializado(Armazenamento.recuperarObjetoSerializao("bases/Base_Ignorados"))

        else:
            self.__arquivosIgnorados = []

    def obterArquivosQuarentena(self):
        return self.__arquivosQuarentena

    def obterArquivosIgnorados(self):
        return self.__arquivosIgnorados

    def adicionarArquivoQuarentena(self,arquivo):
        self.__arquivosQuarentena.append(arquivo)

    def atualizarStatusArquivoQuarentena(self,arquivo):

        index = self.__arquivosQuarentena.index(arquivo)
        self.__arquivosQuarentena[index].definirStatus(True)

    def atualizarStatusArquivoIgnorado(self,arquivo):

        index = self.__arquivosIgnorados.index(arquivo)
        self.__arquivosIgnorados[index].definirStatus(False)

    def atualizarQuarentena(self,acao):

        listaAtualizadaQuarentena = []

        for item in self.__arquivosQuarentena:

            if not item.obterStatus():
                listaAtualizadaQuarentena.append(item)
            elif(acao == "excluir"):
                os.system("rm -f " + item.obterDiretorio()+item.obterNome())
            elif(acao == "ignorar"):
                self.__arquivosIgnorados.append(item)

        self.__arquivosQuarentena=listaAtualizadaQuarentena

    def atualizarIgnorados(self):

        listaAtualizadaIgnorados = []

        for item in self.__arquivosIgnorados:

            if item.obterStatus():
                listaAtualizadaIgnorados.append(item)

        self.__arquivosIgnorados = listaAtualizadaIgnorados