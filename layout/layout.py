# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout-kanschau.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from analise.Analise import Analise

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Kanschau(object):
    def setupUi(self, Kanschau, home, varredura, quarentena):

        self.txtHome = home
        self.varredura = varredura
        self.quarentena = quarentena

        Kanschau.setObjectName("Kanschau")
        Kanschau.resize(693, 600)
        Kanschau.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(Kanschau)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 691, 601))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.tb_inicio = QtWidgets.QWidget()
        self.tb_inicio.setObjectName("tb_inicio")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tb_inicio)
        self.lcdNumber.setGeometry(QtCore.QRect(430, 80, 161, 41))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setProperty("intValue", len(self.quarentena.obterArquivosIgnorados()))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(self.tb_inicio)
        self.label.setGeometry(QtCore.QRect(460, 130, 121, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tb_inicio)
        self.label_2.setGeometry(QtCore.QRect(130, 130, 121, 18))
        self.label_2.setObjectName("label_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tb_inicio)
        self.lcdNumber_2.setGeometry(QtCore.QRect(100, 80, 161, 41))
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_2.setProperty("intValue", len(self.quarentena.obterArquivosQuarentena()))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.pushButton = QtWidgets.QPushButton(self.tb_inicio)
        self.pushButton.setGeometry(QtCore.QRect(10, 230, 661, 151))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.aba1)

        self.pushButton_2 = QtWidgets.QPushButton(self.tb_inicio)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 400, 661, 151))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.aba2)

        self.tabWidget.addTab(self.tb_inicio, "")
        self.tb_verificacao_completa = QtWidgets.QWidget()
        self.tb_verificacao_completa.setObjectName("tb_verificacao_completa")
        self.progressBar = QtWidgets.QProgressBar(self.tb_verificacao_completa)
        self.progressBar.setGeometry(QtCore.QRect(20, 520, 641, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.btn_inicia_verificacao_completa = QtWidgets.QPushButton(self.tb_verificacao_completa)
        self.btn_inicia_verificacao_completa.setGeometry(QtCore.QRect(290, 20, 88, 34))
        self.btn_inicia_verificacao_completa.setObjectName("btn_inicia_verificacao_completa")
        self.btn_inicia_verificacao_completa.clicked.connect(self.iniVerificacaoCompleta)

        self.tabWidget.addTab(self.tb_verificacao_completa, "")
        self.tb_verificacao_avancada = QtWidgets.QWidget()
        self.tb_verificacao_avancada.setObjectName("tb_verificacao_avancada")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tb_verificacao_avancada)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 520, 641, 20))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.lb_caminho_avancada = QtWidgets.QLabel(self.tb_verificacao_avancada)
        self.lb_caminho_avancada.setGeometry(QtCore.QRect(30, 20, 59, 18))
        self.lb_caminho_avancada.setObjectName("lb_caminho_avancada")
        self.lb_user = QtWidgets.QLabel(self.tb_verificacao_avancada)
        self.lb_user.setGeometry(QtCore.QRect(100, 20, 111, 18))

        self.lb_user.setText(self.txtHome)
        self.lb_user.setObjectName("lb_user")
        self.lineEdit = QtWidgets.QLineEdit(self.tb_verificacao_avancada)
        self.lineEdit.setGeometry(QtCore.QRect(220, 10, 351, 32))
        self.lineEdit.setObjectName("lineEdit")

        self.btn_inicia_verificacao_avancada_2 = QtWidgets.QPushButton(self.tb_verificacao_avancada)
        self.btn_inicia_verificacao_avancada_2.setGeometry(QtCore.QRect(580, 10, 88, 34))
        self.btn_inicia_verificacao_avancada_2.setObjectName("btn_inicia_verificacao_avancada_2")
        self.btn_inicia_verificacao_avancada_2.clicked.connect(self.iniVerificacaoAvancada)


        self.tabWidget.addTab(self.tb_verificacao_avancada, "")
        self.tb_quarentena = QtWidgets.QWidget()
        self.tb_quarentena.setObjectName("tb_quarentena")

        self.btn_ign_tb_quarentena = QtWidgets.QPushButton(self.tb_quarentena)
        self.btn_ign_tb_quarentena.setGeometry(QtCore.QRect(0, 510, 221, 51))
        self.btn_ign_tb_quarentena.setObjectName("btn_ign_tb_quarentena")
        #self.btn_ign_tb_quarentena.clicked.connect()

        self.btn_rm_tb_quarentena = QtWidgets.QPushButton(self.tb_quarentena)
        self.btn_rm_tb_quarentena.setGeometry(QtCore.QRect(460, 510, 221, 51))
        self.btn_rm_tb_quarentena.setObjectName("btn_rm_tb_quarentena")
        # self.btn_rm_tb_quarentena.clicked.connect()

        self.lista_arq_quarentena = QtWidgets.QListWidget(self.tb_quarentena)
        self.lista_arq_quarentena.setGeometry(QtCore.QRect(0, 20, 681, 481))
        self.lista_arq_quarentena.setObjectName("lista_arq_quarentena")

        self.addItemQuarentena()

        self.chk_full_quarentena = QtWidgets.QCheckBox(self.tb_quarentena)
        self.chk_full_quarentena.setGeometry(QtCore.QRect(0, 0, 141, 22))
        self.chk_full_quarentena.setSizeIncrement(QtCore.QSize(0, 0))
        self.chk_full_quarentena.setChecked(False)
        self.chk_full_quarentena.setTristate(False)
        self.chk_full_quarentena.setObjectName("chk_full_quarentena")
        self.tabWidget.addTab(self.tb_quarentena, "")
        self.tb_lista_de_ignorados = QtWidgets.QWidget()
        self.tb_lista_de_ignorados.setObjectName("tb_lista_de_ignorados")
        self.lista_arq_ignorados = QtWidgets.QListWidget(self.tb_lista_de_ignorados)
        self.lista_arq_ignorados.setGeometry(QtCore.QRect(0, 20, 681, 481))
        self.lista_arq_ignorados.setObjectName("lista_arq_ignorados")

        self.addItemIgnorado()

        self.chk_full_ignorados = QtWidgets.QCheckBox(self.tb_lista_de_ignorados)
        self.chk_full_ignorados.setGeometry(QtCore.QRect(0, 0, 141, 22))
        self.chk_full_ignorados.setSizeIncrement(QtCore.QSize(0, 0))
        self.chk_full_ignorados.setChecked(False)
        self.chk_full_ignorados.setTristate(False)
        self.chk_full_ignorados.setObjectName("chk_full_ignorados")
        self.btn_rm_tb_ignorados = QtWidgets.QPushButton(self.tb_lista_de_ignorados)
        self.btn_rm_tb_ignorados.setGeometry(QtCore.QRect(240, 510, 221, 51))
        self.btn_rm_tb_ignorados.setObjectName("btn_rm_tb_ignorados")
        self.tabWidget.addTab(self.tb_lista_de_ignorados, "")
        self.tb_ajuda = QtWidgets.QWidget()
        self.tb_ajuda.setObjectName("tb_ajuda")
        self.tabWidget.addTab(self.tb_ajuda, "")
        Kanschau.setCentralWidget(self.centralwidget)

        self.retranslateUi(Kanschau)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Kanschau)

    def retranslateUi(self, Kanschau):
        _translate = QtCore.QCoreApplication.translate
        Kanschau.setWindowTitle(_translate("Kanschau", "MainWindow"))
        self.label.setText(_translate("Kanschau", "Itens Ignorados"))
        self.label_2.setText(_translate("Kanschau", "Itens Quarentena"))
        self.pushButton.setText(_translate("Kanschau", "INICIAR VERIFICAÇÃO COMPLETA"))
        self.pushButton_2.setText(_translate("Kanschau", "INICIAR VERIFICAÇÃO AVANÇADA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_inicio), _translate("Kanschau", "Início"))
        self.btn_inicia_verificacao_completa.setText(_translate("Kanschau", "INICIAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_verificacao_completa), _translate("Kanschau", "Verificação Completa"))
        self.lb_caminho_avancada.setText(_translate("Kanschau", "Caminho:"))
        self.btn_inicia_verificacao_avancada_2.setText(_translate("Kanschau", "INICIAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_verificacao_avancada), _translate("Kanschau", "Verificação Avançada"))
        self.btn_ign_tb_quarentena.setText(_translate("Kanschau", "Ignorar Arquivo(s)"))
        self.btn_rm_tb_quarentena.setText(_translate("Kanschau", "Excluir Arquivo(s)"))
        __sortingEnabled = self.lista_arq_quarentena.isSortingEnabled()
        self.lista_arq_quarentena.setSortingEnabled(False)
        # item = self.lista_arq_quarentena.item(0)
        # item.setText(_translate("Kanschau", "item01"))
        self.lista_arq_quarentena.setSortingEnabled(__sortingEnabled)
        self.chk_full_quarentena.setText(_translate("Kanschau", "Marcar Todos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_quarentena), _translate("Kanschau", "Quarentena"))
        __sortingEnabled = self.lista_arq_ignorados.isSortingEnabled()
        self.lista_arq_ignorados.setSortingEnabled(False)
        # item = self.lista_arq_ignorados.item(0)
        # item.setText(_translate("Kanschau", "item01"))
        self.lista_arq_ignorados.setSortingEnabled(__sortingEnabled)
        self.chk_full_ignorados.setText(_translate("Kanschau", "Marcar Todos"))
        self.btn_rm_tb_ignorados.setText(_translate("Kanschau", "Remover arquivo(s) da lista"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_lista_de_ignorados), _translate("Kanschau", "Lista de Ignorados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_ajuda), _translate("Kanschau", "Ajuda"))

    def editHome(self, txt = ""):
        self.lb_user.setText(txt)

    def aba1(self):
        self.tabWidget.setCurrentIndex(1)

    def aba2(self):
        self.tabWidget.setCurrentIndex(2)

    def addItemQuarentena(self):

        self.lista_arq_quarentena.clear()

        for arquivo in self.quarentena.obterArquivosQuarentena():
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setText(arquivo.obterDiretorio() + arquivo.obterNome())
            self.lista_arq_quarentena.addItem(item)

    def addItemIgnorado(self):

        self.lista_arq_ignorados.clear()

        for arquivo in self.quarentena.obterArquivosIgnorados():
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)
            item.setText(arquivo.obterDiretorio() + arquivo.obterNome())
            self.lista_arq_ignorados.addItem(item)

    def iniVerificacaoAvancada(self):
        self.varredura.limparDados()
        self.varredura.capturarArquivos(self.txtHome + self.lineEdit.displayText())
        numTotal = self.varredura.obterNumeroLido()
        numAtual = 1
        analise = Analise()
        lista = self.varredura.obterArquivosCapturados()

        for arq in lista:
            analise.analisar(arq, self.quarentena)
            self.progressBar_2.setProperty("value", (numAtual*100)/numTotal)
            numAtual+=1

        self.lcdNumber_2.setProperty("intValue", len(self.quarentena.obterArquivosQuarentena()))
        self.addItemQuarentena()

    def iniVerificacaoCompleta(self):
        self.varredura.limparDados()
        self.varredura.capturarArquivos(self.txtHome)
        numTotal = self.varredura.obterNumeroLido()
        numAtual = 1
        analise = Analise()
        lista = self.varredura.obterArquivosCapturados()

        for arq in lista:
            analise.analisar(arq, self.quarentena)
            self.progressBar_2.setProperty("value", (numAtual*100)/numTotal)
            numAtual+=1

        self.lcdNumber_2.setProperty("intValue", len(self.quarentena.obterArquivosQuarentena()))
        self.addItemQuarentena()

    def ignorarArqQuarentena(self):
        for arq in self.lista_arq_quarentena:
            pass


