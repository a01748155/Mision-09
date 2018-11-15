# Autor: Erick David Ramírez Martínez, A01748155, Grupo: 02
# Programa que raliza varias funciones con listas


# Función que extrae los números pares de una lista a otra y regresa la nueva
def extraerPares(lista):
    listaPares = []
    for k in lista:
        if k%2 == 0:
            listaPares.append(k)

    return listaPares


# Función que extrae los números mayores a un elemento previo a otra lista y la regresa
def extraerMayoresPrevio(lista):
    listaMayoresPrevio = []
    for k in range(len(lista)-1):
        if lista[k] < lista[k+1]:
            listaMayoresPrevio.append(lista[k+1])

    return listaMayoresPrevio


# Función que reordena pares de números en un orden inverso dentro de una nueva lista y la regresa
def intercambiarParejas(lista):
    listaIntercambiada = []
    if len(lista)%2 == 0:
        for k in range(0, len(lista)-1, 2):
            listaIntercambiada.append(lista[k+1])
            listaIntercambiada.append(lista[k])
    else:  # Si la lista es impar el último elemento no cambia por lo que se agrega por defecto.
        for k in range(0, len(lista)-2, 2):
            listaIntercambiada.append(lista[k+1])
            listaIntercambiada.append(lista[k])
        listaIntercambiada.append(lista[len(lista)-1])

    return listaIntercambiada


# Función que calcula el mayor y el menor número de una lista e invierte su posición
def intercambiarMM(lista):
    if len(lista) != 0:
        mayor = lista[0]
        indiceMayor = 0
        menor = lista[0]
        indiceMenor = 0
        for k in range(len(lista)):
            if lista[k] > mayor:
                mayor = lista[k]
                indiceMayor = k # Posición del número mayor
            if lista[k] < menor:
                menor = lista[k]
                indiceMenor = k # Posición del número menor
        lista[indiceMayor] = menor
        lista[indiceMenor] = mayor

    return lista


# Función que calcula el promedio centro de la lista y lo regresa
def promediarCentro(lista):
    promedio = 0
    suma = 0
    listapromedio = lista  # La lisa nueva es la misma que la lista ingresada pero sin el mayor ni el menor
    if len(lista) != 0:  # Primero se verifica que haya valores a evaluar
        mayor = lista[0]
        menor = lista[0]
        for k in range(len(lista)):
            if lista[k] > mayor:
                mayor = lista[k]
            if lista[k] < menor:
                menor = lista[k]
        #  Se verifica que existen el número mayor y menor en la lista para quitarlos
        if menor in listapromedio:
            listapromedio.remove(menor)
        if mayor in listapromedio:
            listapromedio.remove(mayor)
        for k in listapromedio:
            suma += k
        promedio = suma // len(listapromedio)

    return promedio


# Función que calcula la desviación estándar de un conjunto de valores de una lista y la regresa junto a su promedio
def calcularEstadistica(lista):
    suma = 0
    suma2 = 0
    media = 0
    s = 0
    for k in lista:
        suma += k
    if len(lista) != 0:
        media = suma / len(lista)
    for k in lista:
        suma2 += (k-media)**2
    if len(lista) != 1:
        s = (suma2 / (len(lista)-1))**0.5  # Fórmula de la desviación estándar

    return (media,s)


# Función que calcula la suma de los valores de una lista con excepción del 13 y cualquier número que esté a su lado
def calcularSuma(lista):
    suma = 0
    listaNueva = []
    for k in range(len(lista)):
        if len(lista) == 1:  # Si la lista solo tiene un elemento solo hay que verificar que este no sea 13
            if lista[0] != 13:
                listaNueva.append(lista[0])
        if len(lista) == 2:  # Si la lista solo tiene 2 elementos solo hay que verificar que ninguno sea 13
            if lista[0] != 13 and lista[1] != 13:
                listaNueva.append(lista[0])
                listaNueva.append(lista[1])
        if k == 0 and len(lista) > 2:  # Evaluación de los primeros 2 valores
            if lista[0] != 13 and lista[1] != 13:
                listaNueva.append(lista[0])
        elif k > 0 and k < len(lista)-1:  # Evaluación de todos los valores menos el primero y el último
            if lista[k] != 13 and lista[k-1] != 13 and lista[k+1] != 13:
                listaNueva.append(lista[k])
        elif k == len(lista)-1 and len(lista) > 2:  # Evaluación de los últimos 2 valores
            if lista[k] != 13 and lista[k-1] != 13:
                listaNueva.append(lista[k])
    for k in listaNueva:
        suma += k

    return suma


# Múltiples evaluaciones con las funciones
def main():

    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista1 = [5,4,3,2,1]
    lista2 = [1,2,3]
    lista3 = [1,2,3,4,5,6]
    lista4 = [5,9,3,22,19,31,10,7]
    lista5 = [70,80,90]
    lista6 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista7 = [20, 55, 30, 5, 55, 5]
    lista8 = [5, 9, 1, 8]
    lista9 = []
    listaExtra1 = [1, 2, 3, 4, 5, 6]
    listaExtra2 = [5, 2, 13, 4, 1, 6, 1, 8, 4, 1, 5]
    listaExtra3 = [5, 2, 13, 4, 1, 6, 1, 8, 4, 13, 1]
    listaExtra4 = [13, 49]
    listaExtra5 = [13]
    listaExtra6 = []

    print("Problema 1: Regresa una lista con los números pares de una lista ingresada")
    print("Con la lista: %s, regresa: %s" % (lista, extraerPares(lista)))
    print("Con la lista: %s, regresa: %s" % (lista1, extraerPares(lista1)))
    print("Con la lista: %s, regresa: %s" % (lista2, extraerPares(lista2)))
    print("Con la lista: %s, regresa: %s" % (lista3, extraerPares(lista3)))
    print("Con la lista: %s, regresa: %s" % (lista4, extraerPares(lista4)))
    print("Con la lista: %s, regresa: %s" % (lista5, extraerPares(lista5)))
    print("Con la lista: %s, regresa: %s" % (lista6, extraerPares(lista6)))
    print("Con la lista: %s, regresa: %s" % (lista7, extraerPares(lista7)))
    print("Con la lista: %s, regresa: %s" % (lista8, extraerPares(lista8)))
    print("Con la lista: %s, regresa: %s" % (lista9, extraerPares(lista9)))
    print("")
    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista1 = [5,4,3,2,1]
    lista2 = [1,2,3]
    lista3 = [1,2,3,4,5,6]
    lista4 = [5,9,3,22,19,31,10,7]
    lista5 = [70,80,90]
    lista6 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista7 = [20, 55, 30, 5, 55, 5]
    lista8 = [5, 9, 1, 8]
    lista9 = []
    print("Problema 2: Regresa una lista con los números mayores a un valor previo de una lista")
    print("Con la lista: %s, regresa: %s" % (lista, extraerMayoresPrevio(lista)))
    print("Con la lista: %s, regresa: %s" % (lista1, extraerMayoresPrevio(lista1)))
    print("Con la lista: %s, regresa: %s" % (lista2, extraerMayoresPrevio(lista2)))
    print("Con la lista: %s, regresa: %s" % (lista3, extraerMayoresPrevio(lista3)))
    print("Con la lista: %s, regresa: %s" % (lista4, extraerMayoresPrevio(lista4)))
    print("Con la lista: %s, regresa: %s" % (lista5, extraerMayoresPrevio(lista5)))
    print("Con la lista: %s, regresa: %s" % (lista6, extraerMayoresPrevio(lista6)))
    print("Con la lista: %s, regresa: %s" % (lista7, extraerMayoresPrevio(lista7)))
    print("Con la lista: %s, regresa: %s" % (lista8, extraerMayoresPrevio(lista8)))
    print("Con la lista: %s, regresa: %s" % (lista9, extraerMayoresPrevio(lista9)))
    print("")
    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista1 = [5,4,3,2,1]
    lista2 = [1,2,3]
    lista3 = [1,2,3,4,5,6]
    lista4 = [5,9,3,22,19,31,10,7]
    lista5 = [70,80,90]
    lista6 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista7 = [20, 55, 30, 5, 55, 5]
    lista8 = [5, 9, 1, 8]
    lista9 = []
    print("Problema 3: Regresa una lista con pares de números invertidos")
    print("Con la lista: %s, regresa: %s" % (lista, intercambiarParejas(lista)))
    print("Con la lista: %s, regresa: %s" % (lista1, intercambiarParejas(lista1)))
    print("Con la lista: %s, regresa: %s" % (lista2, intercambiarParejas(lista2)))
    print("Con la lista: %s, regresa: %s" % (lista3, intercambiarParejas(lista3)))
    print("Con la lista: %s, regresa: %s" % (lista4, intercambiarParejas(lista4)))
    print("Con la lista: %s, regresa: %s" % (lista5, intercambiarParejas(lista5)))
    print("Con la lista: %s, regresa: %s" % (lista6, intercambiarParejas(lista6)))
    print("Con la lista: %s, regresa: %s" % (lista7, intercambiarParejas(lista7)))
    print("Con la lista: %s, regresa: %s" % (lista8, intercambiarParejas(lista8)))
    print("Con la lista: %s, regresa: %s" % (lista9, intercambiarParejas(lista9)))
    print("")
    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista1 = [5,4,3,2,1]
    lista2 = [1,2,3]
    lista3 = [1,2,3,4,5,6]
    lista4 = [5,9,3,22,19,31,10,7]
    lista5 = [70,80,90]
    lista6 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista7 = [20, 55, 30, 5, 55, 5]
    lista8 = [5, 9, 1, 8]
    lista9 = []
    print("Problema 4: Regresa una lista con el número mayor y el número menor invertidos")
    print("Con la lista: ", lista)
    print("Regresa: ", intercambiarMM(lista))
    print("Con la lista: ", lista1)
    print("Regresa: ", intercambiarMM(lista1))
    print("Con la lista: ", lista2)
    print("Regresa: ", intercambiarMM(lista2))
    print("Con la lista: ", lista3)
    print("Regresa: ", intercambiarMM(lista3))
    print("Con la lista: ", lista4)
    print("Regresa: ", intercambiarMM(lista4))
    print("Con la lista: ", lista5)
    print("Regresa: ", intercambiarMM(lista5))
    print("Con la lista: ", lista6)
    print("Regresa: ", intercambiarMM(lista6))
    print("Con la lista: ", lista7)
    print("Regresa: ", intercambiarMM(lista7))
    print("Con la lista: ", lista8)
    print("Regresa: ", intercambiarMM(lista8))
    print("Con la lista: ", lista9)
    print("Regresa: ", intercambiarMM(lista9))
    print("")
    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista1 = [5,4,3,2,1]
    lista2 = [1,2,3]
    lista3 = [1,2,3,4,5,6]
    lista4 = [5,9,3,22,19,31,10,7]
    lista5 = [70,80,90]
    lista6 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista7 = [20, 55, 30, 5, 55, 5]
    lista8 = [5, 9, 1, 8]
    lista9 = []
    print("Problema 5: Regresa una lista con el promedio centro de una lista")
    print("Con la lista: ", lista)
    print("Regresa: ", promediarCentro(lista))
    print("Con la lista: ", lista1)
    print("Regresa: ", promediarCentro(lista1))
    print("Con la lista: ", lista2)
    print("Regresa: ", promediarCentro(lista2))
    print("Con la lista: ", lista3)
    print("Regresa: ", promediarCentro(lista3))
    print("Con la lista: ", lista4)
    print("Regresa: ", promediarCentro(lista4))
    print("Con la lista: ", lista5)
    print("Regresa: ", promediarCentro(lista5))
    print("Con la lista: ", lista6)
    print("Regresa: ", promediarCentro(lista6))
    print("Con la lista: ", lista7)
    print("Regresa: ", promediarCentro(lista7))
    print("Con la lista: ", lista8)
    print("Regresa: ", promediarCentro(lista8))
    print("Con la lista: ", lista9)
    print("Regresa: ", promediarCentro(lista9))
    print("")
    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista1 = [5,4,3,2,1]
    lista2 = [1,2,3]
    lista3 = [1,2,3,4,5,6]
    lista4 = [5,9,3,22,19,31,10,7]
    lista5 = [70,80,90]
    lista6 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista7 = [20, 55, 30, 5, 55, 5]
    lista8 = [5, 9, 1, 8]
    lista9 = []
    print("Problema 6: Regresa el promedio y la desviación estándar de los valores de una lista")
    print("Con la lista: %s, regresa: %s" % (lista, calcularEstadistica(lista)))
    print("Con la lista: %s, regresa: %s" % (lista1, calcularEstadistica(lista1)))
    print("Con la lista: %s, regresa: %s" % (lista2, calcularEstadistica(lista2)))
    print("Con la lista: %s, regresa: %s" % (lista3, calcularEstadistica(lista3)))
    print("Con la lista: %s, regresa: %s" % (lista4, calcularEstadistica(lista4)))
    print("Con la lista: %s, regresa: %s" % (lista5, calcularEstadistica(lista5)))
    print("Con la lista: %s, regresa: %s" % (lista6, calcularEstadistica(lista6)))
    print("Con la lista: %s, regresa: %s" % (lista7, calcularEstadistica(lista7)))
    print("Con la lista: %s, regresa: %s" % (lista8, calcularEstadistica(lista8)))
    print("Con la lista: %s, regresa: %s" % (lista9, calcularEstadistica(lista9)))
    print("")
    print("Problema extra: Regresa la suma de los valores de una lista menos el 13 y los números junto al 13")
    print("Con la lista: %s, regresa: %s" % (listaExtra1, calcularSuma(listaExtra1)))
    print("Con la lista: %s, regresa: %s" % (listaExtra2, calcularSuma(listaExtra2)))
    print("Con la lista: %s, regresa: %s" % (listaExtra3, calcularSuma(listaExtra3)))
    print("Con la lista: %s, regresa: %s" % (listaExtra4, calcularSuma(listaExtra4)))
    print("Con la lista: %s, regresa: %s" % (listaExtra5, calcularSuma(listaExtra5)))
    print("Con la lista: %s, regresa: %s" % (listaExtra6, calcularSuma(listaExtra6)))
    print("")

main()