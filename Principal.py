from analise.Analise import Analise
from varredura.Varredura import Varredura
from persistencia.Armazenamento import Armazenamento
from persistencia.Serializacao import Serializacao
from modelos.Arquivo import Arquivo
from modelos.Quarentena import Quarentena

#--------------------------------------------------------#

varredura = Varredura()
quarentena = Quarentena()

varredura.capturarArquivos("/home/maykon/Downloads/")

analise = Analise(varredura.obterArquivosCapturados(),quarentena)

for arquivo in quarentena.obterArquivosQuarentena():

    print(arquivo.obterNome())


