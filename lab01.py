from math import pi

# # # Ejercicio 1. El programa escribirá la famosa frase '¡Hola Mundo!' por pantalla
print('<--  EJERCICIO 1  -->')
print('¡Hola Mundo!')

# # # Ejercicio 2. Escribe un programa en Python que visualice el mensaje Dime tu nombre,
# # # y que acepte el nombre del usuario almacenándolo como texto.
print('<--  EJERCICIO 2  -->')
nombre = input('Dime tu nombre: ')
print(f'Hola {nombre}!')

# # Ejercicio 3. Divide el anterior programa en funciones: una función para pedir el nombre,
# # y otra, para visualizarlo, pasándosele por parámetro.
print('<--  EJERCICIO 3  -->')


def pedir_nombre():
    nombre = input('Dime tu nombre: ')
    return nombre


def visualizar_nombre(name):
    print(f'Hola {name}!')


aux = pedir_nombre()
visualizar_nombre(aux)

# # # Ejercicio 4. Escribe un programa que pida el radio de una circunferencia, y visualice su área y perímetro.
# # # Escribe dos funciones, que calculen respectivamente cada uno de esos resultados.
print('<--  EJERCICIO 4  -->')


def calcular_area(r):
    return pi * float(r) * float(r)


def calcular_perimetro(r):
    return float(2) * pi * float(r)


radio = input('Introduce el radio de una circunferencia: ')
area = calcular_area(radio)
perimetro = calcular_perimetro(radio)
print(
    f'El área de la circunferencia con radio {radio} es: {area}\n El perímetro es {perimetro}')

# # Ejercicio 5. Escribe un programa que tiene una función a la que se le pasan dos parámetros numéricos,
# # y devuelve una cadena con los parámetros entre paréntesis y separados por una coma. La función se llama
# # fmt_coordenadas(), y consumirá dos números introducidos por teclado.
print('<--  EJERCICIO 5  -->')


def fmt_coordenadas1(num1, num2):
    return '({},{})'.format(num1, num2)


def fmt_coordenadas2(num1, num2):
    return '(' + str(num1) + ',' + num2 + ')'


num1 = input('Introduce el primer dígito: ')
num2 = input('Introduce el segundo dígito: ')

print(fmt_coordenadas1(num1, num2))
print(fmt_coordenadas2(num1, num2))

# Ejercicio 6. Escribe un programa que acepte tres entradas: dos números y un carácter. Si el carácter es '+'
# los números se suman, con '-' se restan, con '*' se multiplican, con '/' se dividen, y con '^' se eleva el primero
# al segundo. Crea una función que acepte estos tres datos y devuelva el resultado del cálculo. Crea otra función
# que pida los datos necesarios.
print('<--  EJERCICIO 6  -->')


def calculadora(num1, num2, op):
    if op == '+':
        return float(num1) + float(num2)
    elif op == '-':
        return float(num1) - float(num2)
    elif op == '*':
        return float(num1) * float(num2)
    elif op == '/':
        return float(num1) / float(num2)
    elif op == '^':
        return float(num1) ** float(num2)
    else:
        return '¡Operador inválido!'


n1 = input('Introduce el primer número: ')
n2 = input('Introduce el segundo número: ')
c = input('Introduce el carácter de la operación deseada: ')

print(calculadora(n1, n2, c))


# Ejercicio 7. Un formateador de números de teléfono básicamente agrupa los dígitos en grupos de tres, e ignora
# cualquier carácter que no sea un dígito. Por ejemplo, (988) 387001 se convertiría en 988 387 001. Además, el número
# puede estar precedido o no por el código de páis (dos dígitos), mediante el formato ‘+’ o ‘00’: +34 (988) 387001 o
# 0034 (988) 387001 deben convertirse en +34 988 387 001. Finalmente, pueden encontrarse letras de la a a la z en el
# número, que deben traducirse a dígitos siguiendo la convención: 2: a, b, c; 3: d, e, f; 4: g, h, i; 5: j, k, l; 6:
# m, n, o; 7: p, q, r, s; 8: t, u, v; y 9: w, y, z. Así, 900 ESI NFO sería 900 374 636.
print('<--  EJERCICIO 7  -->')


def phone_format(tlf):
    toret = []
    count = 0
    abecedario = 'abcdefghijklmnopqrstuvxwyz'

    if str(tlf[0]) == '+':
        toret.append(str(tlf[0:3]))
        toret.append(' ')
        count = 3
    elif str(tlf[0:2]) == '00':
        toret.append('+')
        toret.append(str(tlf[2:4]))
        toret.append(' ')
        count = 3

    for n in str(tlf[3:len(tlf)]):
        if n.isdigit():
            toret.append(str(n))
            if count == 2 or count == 5 or count == 8:
                toret.append(' ')
            count += 1

        else:
            for i in range(26):
                if abecedario[i] == n:
                    toret.append(str(int((i / 3) + 1)))
                    count += 1

    return ''.join(toret)


tlf = input('Introduce el número de telefono: ')
print(phone_format(tlf))
