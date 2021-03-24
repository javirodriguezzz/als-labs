"""
Un almacén guarda piezas de fontanería, en concreto tuberías, tuercas, y codos.
Es necesario llevar un servicio de inventario que permita el alta, baja y modificación de
piezas. Crea la jerarquía de herencia necesaria, y para la clase Inventario, reescribe
los métodos necesarios, de tal forma que se comporte como una lista de piezas.
"""


class Pieza:

    def __init__(self, nombre):
        self._nombre = nombre


class Tornillo(Pieza):

    def __init__(self, nombre, cm):
        super().__init__(nombre)
        self._lenght = cm

    def __str__(self):
        return f"Tornillo {self._nombre} de tamaño {self._lenght} cm"


class Tuerca(Pieza):

    def __init__(self, nombre, cm):
        super().__init__(nombre)
        self._radio = cm

    def __str__(self):
        return f"Tuerca {self._nombre} de radio {self._radio} mm"


class Codo(Pieza):

    def __init__(self, nombre, grados):
        super().__init__(nombre)
        self._angulo = grados

    def __str__(self):
        return f"Codo {self._nombre} de ángulo {self._angulo} grados"


class Inventario:

    def __init__(self):
        self.piezas = []

    def __len__(self):
        return len(self.piezas)

    def __getitem__(self, item):
        return self.piezas[item]

    def __add__(self, other):
        self.piezas.append(other)

    def __str__(self):
        toret = ""
        for p in self.piezas:
            toret = toret + f"{p}\n"

        return toret


if __name__ == "__main__":
    inv = Inventario()
    tor1 = Tornillo("DIN-84", 6)
    tuer1 = Tuerca("RS PRO", 10)
    codo1 = Codo("A-304", 90)

    inv.__add__(tor1)
    inv.__add__(tuer1)
    inv.__add__(codo1)

    print(inv)
