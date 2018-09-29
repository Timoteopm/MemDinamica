class memDinamica:
    __author__ = 'Timoteo'


cerveceria = ['modelo', 'corona', 'victoria', 'ultra', 'barrilito', 'dosequis']
precios = ['15', '16', '14', '12', '8', '10']

listas = cerveceria(cerveceria)
listas.imprimirLista()
listas.agregarElementoarray('Heinekeen')
listas.imprimirLista()
listas.agregarElementoarray('Indio')
listas.imprimirLista()
listas.eliminarElemento('victoria')
listas.imprimirLista()
listas.insertarNPosition(3, 'Tecate')
listas.imprimirLista()
listas.eliminarNElemento(2)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()

listas1 = precios(precios)
listas1.imprimirLista()
listas1.agregarElementoarray('13')
listas1.imprimirLista()
listas1.eliminarNElementos(2)
listas1.imprimirLista()
listas1.agregarElementoarray('17')
listas1.imprimirLista()
