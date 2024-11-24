
#algoritmo para ordenar una lista de numeros
def ordenar(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return

#hash sort
def hash_sort(lista):
    hash = {}
    for i in lista:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    lista = []
    for i in sorted(hash.keys()):
        lista += [i] * hash[i]

#quick sort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        return quicksort([x for x in lista[1:] if x < lista[0]]) + [lista[0]] + quicksort([x for x in lista[1:] if x >= lista[0]])