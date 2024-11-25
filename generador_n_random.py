class numeros_random:
    def __init__(self, n):
        self.n = n
    def generar(self):
        import random
        return [random.randint(0, 100) for _ in range(self.n)]


numero = numeros_random(10)