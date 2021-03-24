"""
En la sucesión de Tribonacci, cada elemento
es la suma de los tres anteriores, y se empieza
por 0, 1, 1.

In the Tribonacci succesion, each element is the sum
of the three previous instances, and it always
starts with 0, 1, 1.
"""
def tribonacci_iter(n):
    def tribonacci(n):
        """
        Calcular la sucesión de tribonacci hasta n elementos de forma iterativa.
        :param n: número de elementos.
        :return: Una lista de n elementos con la sucesión.
        """
        if n == 0:
            toret = []
        if n == 1:
            toret = [0]
        elif n == 2:
            toret = [0, 1]
        elif n == 3:
            toret = [0, 1, 1]
        else:
            toret = [0, 1, 1]
            for i in range(3, n):
                toret.append(toret[i - 1] + toret[i - 2] + toret[i - 3])

        return toret


def tribonacci_rec(n):
    """
    Calcular la sucesión de tribonacci hasta n elementos de forma recursiva.
    :param n: número de elementos.
    :return: Una lista de n elementos con la sucesión.
    """
    if n <= 0:
        toret = []
    if n == 1:
        toret = [0]
    elif n == 2:
        toret = [0, 1]
    elif n == 3:
        toret = [0, 1, 1]
    else:
        toret = tribonacci_rec(n - 1)
        toret.append(toret[-1] + toret[-2] + toret[-3])

    return toret


def tribonacci(n):
    return tribonacci_rec(n)


if __name__ == "__main__":
    print("Tribonacci(10):", tribonacci(10))
