import pickle

class Serializacao():

    @staticmethod
    def serializar(objeto):

        objetoSerializado = pickle.dumps(objeto)

        return objetoSerializado

    @staticmethod
    def recuperarSerializado(objetoSerializado):

        objetoRecuperado = pickle.loads(objetoSerializado)

        return objetoRecuperado