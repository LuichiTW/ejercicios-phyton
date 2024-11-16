
pisos = 4
posicionElevador = 0

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

#imprimir a quantidad de andares