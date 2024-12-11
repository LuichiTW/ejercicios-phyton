
#funcion para calcular el pronedio de una lista de numeros
def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma / len(lista)


#llamada a la funcion
lista = [1,2,3,4,5]
print(promedio(lista))
# Output: 3.0