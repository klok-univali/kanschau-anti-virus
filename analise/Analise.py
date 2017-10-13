import hashlib

class Analise():

    def __init__(self, listaArqLidos):
        h = hashlib.md5()

        for arqLido in listaArqLidos:
            file = open(arqLido)
            h.update(file.read().encode())
            #print(h.hexdigest())

            if self.itemQuarentena() or self.itemIgnorado():
                continue

            





    def itemQuarentena(self):
        pass
        return

    def itemIgnorado(self):
        pass
        return

