from analise.Analise import Analise
from varredura.Varredura import Varredura
from persistencia.Armazenamento import Armazenamento
from persistencia.Serializacao import Serializacao
from modelos.Quarentena import Quarentena
import os

#--------------------------------------------------------#

if __name__ == '__main__':

    varredura = Varredura()
    quarentena = Quarentena()

    pipe = os.popen('echo ${HOME}/')
    home = pipe.read().replace('\n','')
    pipe.close()

    print("-----------------------------------------------------------------------------------------------------------")
    print("Arquivo(s) em Quarentena: " + str(len(quarentena.obterArquivosQuarentena())))
    print("Arquivo(s) Ignorados: " + str(len(quarentena.obterArquivosIgnorados())))
    print("Home do usuário: " + home)
    print("-----------------------------------------------------------------------------------------------------------")

    cabecalho = "1. Varredura completa do sistema.\n" \
                "2. Varredura avançada.\n" \
                "3. Mostrar arquivos em quarentena.\n" \
                "4. Mostrar arquivos ignorados.\n" \
                "5. Sair.\n"

    while(True):

        print("\n" + cabecalho)
        opcao = input("Selecione a opção desejada: ")

        if(opcao == "1"):
            varredura.limparDados()
            print("Realizando varredura completa do sistema.....")
            varredura.capturarArquivos(home)
            print("Número de arquivos varridos: " + str(len(varredura.obterArquivosCapturados())))
            print("Realizando análise dos arquivos.....")
            Analise(varredura.obterArquivosCapturados(),quarentena)
            print("Varredura e Análise finalizadas, para verificar os arquivos em quarentena acessar a opção 3 do MENU "
                  "ou opção 4 para arquivos ignorados.")
        elif(opcao == "2"):
            varredura.limparDados()
            diretorio = input("Insira o caminho da pasta: " + home)

            if(os.path.isdir(home+diretorio)):
                print("Realizando a varredura do diretório " + home+diretorio + ".....")
                varredura.capturarArquivos(home+diretorio)
                print("Número de arquivos varridos: " + str(len(varredura.obterArquivosCapturados())))
                Analise(varredura.obterArquivosCapturados(), quarentena)
                print("Varredura e Análise finalizadas, para verificar os arquivos em quarentena acessar a opção 3 do MENU ou opção 4"
                    "para arquivos ignorados.")
            else:
                print("Diretório inválido, tente novamente!")

        elif(opcao == "3"):
            print("------------------------------------Arquivos em quarentena-----------------------------------------")
            contador = 1
            for arquivo in quarentena.obterArquivosQuarentena():
                print("Arquivo " + str(contador) + ": " + arquivo.obterNome())
            print("--------------------------------Fim Arquivos em quarentena-----------------------------------------")

            cabecalhoQuarentena = "1. Apagar arquivo específico.\n" \
                                  "2. Apagar todos os arquivos.\n" \
                                  "3. Ignorar arquivo especifico.\n" \
                                  "4. Ignorar todos os arquivos.\n" \
                                  "5. Voltar ao menu principal.\n"

            while(True):
                print("\n" + cabecalhoQuarentena)

                opcaoQuarentena = input("Selecione a opção desejada: ")

                if(opcaoQuarentena == "1"):
                    numero = input("Informe o número do arquivo que deseja apagar: ")

                    contador = 0

                    for arquivo in quarentena.obterArquivosQuarentena():

                        if(int(contador) == int(numero)-1):
                            print("Apagando arquivo " + arquivo.obterNome() + " !")
                            arquivo.definirStatus(True)
                        contador += 1
                    quarentena.atualizarQuarentena("excluir")

                elif(opcaoQuarentena == "2"):

                    for arquivo in quarentena.obterArquivosQuarentena():
                        print("Apagando arquivo " + arquivo.obterNome() + " !")
                        arquivo.definirStatus(True)

                    quarentena.atualizarQuarentena("excluir")

                elif(opcaoQuarentena == "3"):
                    numero = input("Informe o número do arquivo que deseja ignorar: ")

                    contador = 0

                    for arquivo in quarentena.obterArquivosQuarentena():

                        if (int(contador) == int(numero) - 1):
                            print("Ignorando arquivo " + arquivo.obterNome() + " !")
                            arquivo.definirStatus(True)
                        contador += 1
                    quarentena.atualizarQuarentena("ignorar")

                elif(opcaoQuarentena == "4"):

                    for arquivo in quarentena.obterArquivosQuarentena():
                        print("Ignorando arquivo " + arquivo.obterNome() + " !")
                        arquivo.definirStatus(True)

                    quarentena.atualizarQuarentena("ignorar")

                else:
                    break

        elif(opcao == "4"):
            print("--------------------------------------Arquivos ignorados-------------------------------------------")
            contador = 1
            for arquivo in quarentena.obterArquivosIgnorados():
                print("Arquivo " + str(contador) + ": " + arquivo.obterNome())
            print("------------------------------------Fim Arquivos ignorados-----------------------------------------")

            cabecalhoIgnorados =  "1. Retirar arquivo especifico da lista.\n" \
                                  "2. Retirar todos os arquivos da lista.\n" \
                                  "3. Voltar ao menu principal.\n"

            while (True):
                print("\n" + cabecalhoIgnorados)

                opcaoIgnorados = input("Selecione a opção desejada: ")

                if(opcaoIgnorados == "1"):
                    numero = input("Informe o número do arquivo que deseja retirar da lista: ")

                    contador = 0

                    for arquivo in quarentena.obterArquivosIgnorados():

                        if(int(contador) == int(numero)-1):
                            print("Retirando arquivo " + arquivo.obterNome() + " da lista!")
                            arquivo.definirStatus(True)
                        contador += 1
                    quarentena.atualizarIgnorados()

                elif(opcaoIgnorados == "2"):

                    for arquivo in quarentena.obterArquivosIgnorados():
                        print("Retirando arquivo " + arquivo.obterNome() + " da lista!")
                        arquivo.definirStatus(True)

                    quarentena.atualizarIgnorados()

                else:
                    break

        else:
            Armazenamento.gravarObjetoSerializado("bases/Base_Quarentena",Serializacao.serializar(quarentena.obterArquivosQuarentena()))
            Armazenamento.gravarObjetoSerializado("bases/Base_Ignorados",Serializacao.serializar(quarentena.obterArquivosIgnorados()))
            exit(0)


