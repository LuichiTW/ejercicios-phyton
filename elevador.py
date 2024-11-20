
pisos = 4
listaPisos = [1, 0, 0, 0, 0]
posicionElevador = 0
# 0 = detenido, 1 = subiendo, 2 = bajando
estadoElevador = 0


def subir():
    global posicionElevador
    if posicionElevador < pisos:
        posicionElevador += 1
    else:
        print("El elevador ya está en el último piso")

def bajar():
    global posicionElevador
    if posicionElevador > 0:
        posicionElevador -= 1
    else:
        print("El elevador ya está en el primer piso")

def pedirElevador():
    global posicionElevador
    andar = int(input("Ingrese el número de andar al que desea ir: "))
    if andar > pisos:
        print("El edificio solo tiene", pisos, "pisos")
    else:
        if andar > posicionElevador:
            while posicionElevador < andar:
                subir()
        elif andar < posicionElevador:
            while posicionElevador > andar:
                bajar()
        print("Llegamos al andar", andar)

#imprimir la posición del elevador
def imprimirPosicion():
    global posicionElevador
    print("Posición del elevador:", posicionElevador)

#imprimir a quantidad de andares
def imprimirPisos():
    global listaPisos
    for element in listaPisos:
        print("Andar", element)

#cambiar el estado del elevador
def cambiarEstado():
    global estadoElevador
    print("Estado actual del elevador:", estadoElevador)
    estadoElevador = int(input("Ingrese el estado del elevador: "))
    print("Estado del elevador cambiado a:", estadoElevador)