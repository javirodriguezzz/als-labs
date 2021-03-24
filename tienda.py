"""
Es necesario desarrollar un sistema de facturación para una tienda de reparación
de aparatos de imagen, en concreto televisores y reproductores de DVD. Cada factura
tiene un detalle que refleja el aparato reparado (cada tipo de aparato supone un
precio de reparación por hora distinto), además del total. Crea un sistema que permita
crear facturas según los aparatos reparados.
"""


class Aparato:

    def __init__(self, nombre, cliente):
        self._nombre = nombre
        self._cliente = cliente

    @property
    def getNombre(self):
        return self._nombre

    @property
    def getCliente(self):
        return self._cliente


class Televisor(Aparato):

    def __init__(self, nombre, cliente):
        super().__init__(nombre, cliente)
        self._tarifa = 6.5

    @property
    def getTarifa(self):
        return self._tarifa

    def __str__(self):
        return f"Televisor: {self._nombre} del cliente {self._cliente}"


class ReproductorDvd(Aparato):

    def __init__(self, nombre, cliente):
        super().__init__(nombre, cliente)
        self._tarifa = 8

    @property
    def getTarifa(self):
        return self._tarifa

    def __str__(self):
        return f"Reproductor DVD: {self._nombre} del cliente {self._cliente}"


class Reparacion:

    def __init__(self):
        self.aparatos = []
        self.num_horas = []

    def __len__(self):
        return len(self.aparatos)

    def __getitem__(self, item):
        return self.aparatos[item]

    def __add__(self, aparato, tiempo):
        self.aparatos.append(aparato)
        self.num_horas.append(tiempo)

    def _calcular_precio(self, aparato):
        """
        Calcula el precio de la reparación de un aparato (puede haber varias reparaciones del mismo).
        :param aparato: el aparato reparado
        :return: precio de la reparación (10€ cuota fija + numero de horas * tarifa)
        """
        toret = 0
        for i in range(len(self.aparatos)):
            if self.aparatos[i] == aparato:
                toret += 10 + (self.aparatos[i].getTarifa * self.num_horas[i])

        return str(toret)

    def factura(self):
        """
        Genera una factura con las reparaciones existentes
        :return: texto de la factura
        """
        toret = ""

        for ap in self.aparatos:
            precio = self._calcular_precio(ap)
            nombre_aparato = ap.getNombre
            cliente = ap.getCliente
            toret += f"Reparacion de {cliente} del aparato {nombre_aparato}\nPrecio: {precio}€\n\n"

        return toret


if __name__ == "__main__":

    tv1 = Televisor("SAMSUNG X21", "Javier Rodríguez")
    dvd1 = ReproductorDvd("Panasonic DVD-20", "Elon Musk")

    reparacion = Reparacion()

    reparacion.__add__(tv1, 3)
    reparacion.__add__(dvd1, 1)

    print(reparacion.factura())
