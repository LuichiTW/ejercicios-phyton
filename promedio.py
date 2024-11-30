
#funcion para calcular el pronedio de una lista de numeros
def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)