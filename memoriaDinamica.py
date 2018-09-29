
    __author__ = 'Timoteo'

class memoriaDinamica:
    __lista = []

def __init__(self, list):
    self.__lista = list

    def agregarElementoarray(self, elemento):
       self.__lista.append(elemento)

    def ordenarLista(self):
        self.__lista.sort()

    def eliminarNElemento(self, numero):
        self.__lista.pop(numero)

    def eliminarElemento(self, elemento):
        self.__lista.remove(elemento)

    def insertarNPosicion(self, numero, elemento):
        self.__lista.insert(numero, elemento)

    def imprimirLista(self):
        print(self.__lista)