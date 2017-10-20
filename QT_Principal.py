from analise.Analise import Analise
from varredura.Varredura import Varredura
from persistencia.Armazenamento import Armazenamento
from persistencia.Serializacao import Serializacao
from modelos.Quarentena import Quarentena
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from layout.layout import Ui_Kanschau

#--------------------------------------------------------#

varredura = Varredura()
quarentena = Quarentena()

pipe = os.popen('echo ${HOME}/')
home = pipe.read().replace('\n','')
pipe.close()

if __name__ == '__main__':
    app = QApplication([])
    window = QMainWindow()
    main_window = Ui_Kanschau()
    main_window.setupUi(window, home, varredura, quarentena)
    window.show()
    app.exec_()