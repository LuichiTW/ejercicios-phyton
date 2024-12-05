import pygame

class juego:
    def __init__(self):
        self.jugador
        self.objetosColeccionables
        self.objetosMobibles
        self.objetosSolidos
    
    def iniciar(self):
        #inicializar todas las variables
        pass

    def actualizar(self):
        #actualizar todas las variables
        pass

class objeto:
    def __init__(self) -> None:
        self.posicionx
        self.posiciony
        self.tipo

    def mover(self):
        pass

class roca(objeto):
    def __init__(self) -> None:
        super().__init__()
        self.tipo = "roca"
        self.peso

    def mover(self):
        #comprobar si hay un espacio vacio enfrente
        #actualizar la posicion basada en la direccion en la que esta mirando
        pass


class jugador:
    def __init__(self) -> None:
        self.posicionx
        self.posiciony
        self.direccion

    def moverse_adelante(self):
        #comprobar si hay objeto enfrente
        if self.dirreccion == self.sur and self.posiciony - 1:
            pass
        #actualizar la posicion basada en la direccion en la que esta mirando
        
    def girar_izquierda():
        #actualizar el sprite del jugador dependiento en que direccion esta
        pass

    def girar_derecha():
        #actualizar el sprite del jugador dependiento en que direccion esta
        pass

    def gritar(palabra):
        print(palabra + "!")
        pass

    def empujar():
        # comprobar si hay una roca enfrente
        # roca.mover()
        pass

class enemigo:
    def __init__(self) -> None:
        self.posicionx
        self.posiciony
        self.direccion

    def moverse_adelante(self):
        #comprobar si hay objeto enfrente
        #actualizar la posicion basada en la direccion en la que esta mirando
        pass

    def girar_izquierda():
        #actualizar el sprite del enemigo dependiento en que direccion esta
        pass

    def girar_derecha():
        #actualizar el sprite del enemigo dependiento en que direccion esta
        pass

    def gritar(palabra):
        print(palabra + "!")
        pass

    def empujar():
        # comprobar si hay una roca enfrente
        # roca
        pass

#creo un objeto jugador
jugadorConejo = jugador()
#inicializar todas las variables

#creo un objeto juego
juegoConejo = juego()
#inicializar todas las variables

#asigno el jugador al juego
juegoConejo.jugador = jugadorConejo
