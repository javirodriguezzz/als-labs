"""
Cree la clase Préstamo, que acepta un número de cuotas, un importe,
y un interés. Se calcula el importe total añadiendo el interés al importe.
Y se divide el importe total por el número de cuotas para obtener el
importe de cada cuota.

Propiedades:
num_cuotas: Devuelve las cuotas restantes.
cuota: Devuelve el importe de cada cuota.
importe_total: Devuelve el importe total a pagar.

Métodos:
paga_cuota(): reduce el importe total con el importe de a cuota, y reduce
el número de cuotas.
amortiza(x): reduce el importe total con x, y se recalcula el importe de
cada cuota según el número de cuotas.
"""


class Prestamo:
    def __init__(self, importe, num_cuotas, interes):
        self._num_cuotas = num_cuotas
        self._importe_total = importe + ((interes/100) * importe)
        self._cuota = self._importe_total / self._num_cuotas

    def __str__(self):
        return f"Total: {self.importe_total:5.2f}, en {self.num_cuotas} cuotas, de {self.cuota:5.2f}€"

    @property
    def importe_total(self):
        return self._importe_total

    @property
    def num_cuotas(self):
        return self._num_cuotas

    @property
    def cuota(self):
        return self._cuota

    def paga_cuota(self):
        self._importe_total -= self._cuota
        self._num_cuotas -= 1

    def amortiza(self, x):
        self._importe_total -= x
        self._cuota = self.importe_total / self._num_cuotas


if __name__ == "__main__":
    p1 = Prestamo(1000, 12, 10)
    print(p1)
    p1.paga_cuota()
    print(p1)
    p1.amortiza(200)
    print(p1)
