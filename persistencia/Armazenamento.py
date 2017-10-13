class Armazenamento():

    @staticmethod
    def gravarObjetoSerializado(arquivo,objetoSerializado):

        arquivoAberto = open(arquivo,'wb')

        arquivoAberto.write(objetoSerializado)

        arquivoAberto.close()

    @staticmethod
    def recuperarObjetoSerializao(arquivo):

        arquivoAberto = open(arquivo,'rb')

        return arquivoAberto.read()
