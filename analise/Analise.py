import hashlib
import os
from modelos.Arquivo import Arquivo

class Analise():

    def __init__(self, listaArquivos,quarentena):
        baseVirus = open("bases/Base_Virus",'r')

        hash = hashlib.md5()

        for arquivo in listaArquivos:
            file = open(arquivo)
            hash.update(file.read().encode())
            #print(hash.hexdigest())
            if self.itemQuarentena(hash,quarentena.obterArquivosQuarentena()) or self.itemIgnorado(hash,quarentena.obterArquivosIgnorados()):
                continue

            for hashVirus in baseVirus.readlines():
                #print(arquivo)

                if hash.hexdigest() in hashVirus.replace('\n',''):
                    objetoArquivo = Arquivo()
                    objetoArquivo.definirNome(os.path.basename(arquivo))
                    objetoArquivo.definirDiretorio(os.path.dirname(arquivo)+'/')
                    objetoArquivo.definirHash(hash.hexdigest())
                    quarentena.adicionarArquivoQuarentena(objetoArquivo)

            baseVirus.seek(0,0)

    def itemQuarentena(self,hash,quarentena):

        for arquivo in quarentena:

            if arquivo.obterHash() == hash.hexdigest():
                return True

        return False

    def itemIgnorado(self,hash,ignorados):

        for arquivo in ignorados:

            if arquivo.obterHash() == hash.hexdigest():
                return True

        return False

