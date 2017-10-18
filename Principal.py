from analise.Analise import Analise
from varredura.Varredura import Varredura
from persistencia.Armazenamento import Armazenamento
from persistencia.Serializacao import Serializacao
from modelos.Arquivo import Arquivo
from modelos.Quarentena import Quarentena
import os

from PyQt5.QtWidgets import QMainWindow, QApplication
from layout.layout import Ui_Kanschau

#--------------------------------------------------------#

# varredura = Varredura()
# quarentena = Quarentena()
#
# varredura.capturarArquivos("/home/srfr33dy/Documentos/")
#
# analise = Analise(varredura.obterArquivosCapturados(),quarentena)
#
# for arquivo in quarentena.obterArquivosQuarentena():
#
#     print(arquivo.obterNome())

#  print(os.system("echo $HOME"))   ISSO PEGA O /HOME/USUARIO


app = QApplication([])
window = QMainWindow()
main_window = Ui_Kanschau()
main_window.setupUi(window)
window.show()
app.exec_()
