
class cronometro:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0

    def set_hora(self, horas):
        self.horas = horas

    def set_minuto(self, minutos):
        self.minutos = minutos

    def set_segundo(self, segundos):
        self.segundos = segundos

    def get_hora(self):
        return self.horas

    def get_minuto(self):
        return self.minutos

    def get_segundo(self):
        return self.segundos

    def incrementar(self):
        self.segundos += 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1
                if self.horas == 24:
                    self.horas = 0

    def decrementar(self):
        self.segundos -= 1
        if self.segundos == -1:
            self.segundos = 59
            self.minutos -= 1
            if self.minutos == -1:
                self.minutos = 59
                self.horas -= 1
                if self.horas == -1:
                    self.horas = 23

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.horas, self.minutos, self.segundos)