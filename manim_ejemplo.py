

#ejemplo usando manin para hacer una animacion de un cuadrado que se mueve
from manim import *

class CuadradoMovil(Scene):
    def construct(self):
        cuadrado = Square()
        self.play(Create(cuadrado))
        self.play(cuadrado.animate.shift(UP))
        self.play(cuadrado.animate.shift(LEFT))
        self.play(cuadrado.animate.shift(DOWN))
        self.play(cuadrado.animate.shift(RIGHT))
        self.play(FadeOut(cuadrado))
    
#para ejecutar el script se debe usar el siguiente comando en la terminal

