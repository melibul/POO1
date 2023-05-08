class Ventana:
    def __init__(self, titulo, x1=0, y1=0, x2=100, y2=100):
        self.titulo = titulo
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.x1 < 0:
            self.x1 = 0
        if self.y1 < 0:
            self.y1 = 0
        if self.x2 > 500:
            self.x2 = 500
        if self.y2 > 500:
            self.y2 = 500
        if self.x1 >= self.x2:
            self.x2 = self.x1 + 100
        if self.y1 >= self.y2:
            self.y2 = self.y1 + 100

    def mostrar(self):
        print('Ventana {}: ({}, {}) - ({}, {})'.format(self.titulo, self.x1, self.y1, self.x2, self.y2))

    def getTitulo(self):
        return self.titulo

    def alto(self):
        return self.y2 - self.y1

    def ancho(self):
        return self.x2 - self.x1

    def moverDerecha(self, unidades=1):
        self.x1 += unidades
        self.x2 += unidades

        if self.x2 > 500:
            dif = self.x2 - 500
            self.x1 -= dif
            self.x2 -= dif

    def moverIzquierda(self, unidades=1):
        self.x1 -= unidades
        self.x2 -= unidades

        if self.x1 < 0:
            dif = abs(self.x1)
            self.x1 += dif
            self.x2 += dif

    def bajar(self, unidades=1):
        self.y1 += unidades
        self.y2 += unidades

        if self.y2 > 500:
            dif = self.y2 - 500
            self.y1 -= dif
            self.y2 -= dif

    def subir(self, unidades=1):
        self.y1 -= unidades
        self.y2 -= unidades

        if self.y1 < 0:
            dif = abs(self.y1)
            self.y1 += dif
            self.y2 += dif