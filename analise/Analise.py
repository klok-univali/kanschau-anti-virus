import os
from modelos.Arquivo import Arquivo

class Analise():

    def __init__(self, listaArquivos,quarentena):
        baseVirus = open("bases/Base_Virus",'r')

        for arquivo in listaArquivos:

            pipe = os.popen("md5sum -b " + arquivo + "|cut -f1 -d\' \'")
            hash = pipe.read().replace('\n','')
            pipe.close()

            if self.itemQuarentena(hash,quarentena.obterArquivosQuarentena()) or self.itemIgnorado(hash,quarentena.obterArquivosIgnorados()):
                continue

            for hashVirus in baseVirus.readlines():

                if hash in hashVirus.replace('\n',''):
                    objetoArquivo = Arquivo()
                    objetoArquivo.definirNome(os.path.basename(arquivo))
                    objetoArquivo.definirDiretorio(os.path.dirname(arquivo)+'/')
                    objetoArquivo.definirHash(hash)
                    quarentena.adicionarArquivoQuarentena(objetoArquivo)

            baseVirus.seek(0,0)

    def itemQuarentena(self,hash,quarentena):

        for arquivo in quarentena:

            if arquivo.obterHash() == hash:
                return True

        return False

    def itemIgnorado(self,hash,ignorados):

        for arquivo in ignorados:

            if arquivo.obterHash() == hash:
                return True

        return False

