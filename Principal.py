from analise.Analise import Analise
from varredura.Varredura import Varredura
from persistencia.Armazenamento import Armazenamento
from persistencia.Serializacao import Serializacao
from modelos.Arquivo import Arquivo
from modelos.Quarentena import Quarentena

#--------------------------------------------------------#

varredura = Varredura()
quarentena = Quarentena()

varredura.capturarArquivos("/home/srfr33dy/Documentos/")

analise = Analise(varredura.obterArquivosCapturados(),quarentena)

for arquivo in quarentena.obterArquivosQuarentena():

    print(arquivo.obterNome())


