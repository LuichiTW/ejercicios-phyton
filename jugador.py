class juego:
    jugador
    objetosColeccionables
    objetosMobibles
    objetosSolidos

class jugador:
    posicionx
    posiciony
    direccion
    def moverse_adelante():
        #comprobar si hay objeto enfrente
        if dirreccion == sur and posiciony - 1:
            pass
        #actualizar la posicion basada en la direccion en la que esta mirando
        
    def girar_izquierda():
        #actualizar el sprite del jugador dependiento en que direccion esta

    def girar_derecha():
        #actualizar el sprite del jugador dependiento en que direccion esta

    def gritar(palabra):
        print(palabra + "!")

    def empujar():
        # comprobar si hay una roca enfrente
        # roca.mover()


#creo un objeto jugador
jugadorConejo = jugador()
#inicializar todas las variables

#creo un objeto juego
juegoConejo = juego()
#inicializar todas las variables

#asigno el jugador al juego
juegoConejo.jugador = jugadorConejo
