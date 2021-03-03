from math import sqrt

# Ejercicio 1. Escribe un programa en Python que acepte una secuencia de números, y cuando el usuario teclee un cero
# calcule su media, mayor, menor, y su desviación típica (el último cero no debe estar incluido en los cálculos).
print('<--  EJERCICIO 1  -->')


def sequence_calc():
    inp = 1
    arr = []
    op1 = 0

    while inp != '0':
        inp = input('Introduce número: ')
        if inp != '0':
            arr.append(inp)

    for i in arr:
        op1 += float(i)

    op2 = len(arr)

    media = op1 / op2
    std = sqrt(media)
    print(
        f'La media de la secuencia es: {media}\nLa desviación típica es {std}')


# sequence_calc()

# Ejercicio 2. Escribe una función es_anagrama(s1, s2) que determine si son anagramas dos cadenas pasadas como
# argumento. Dos cadenas son anagramas la una de la otra, si tienen las mismas letras pero en distinto orden.
print('<--  EJERCICIO 2  -->')


def es_anagrama(s1, s2):
    array1 = []
    array2 = []
    cont = 0

    for i in range(len(s1)):
        array1.append(s1[i:i + 1])
        array2.append(s2[i:i + 1])

    for c1 in array1:
        for c2 in array2:
            if c1 == c2:
                cont += 1

    if cont == len(s2):
        print('Son anagramas')
    else:
        print('No son anagramas')

    print(f'1: {array1}\n2: {array2}')


# es_anagrama('javi', 'iavj')

# Ejercicio 3. El programa aceptará una expresión numérica del usuario, la evaluará y devolverá el resultado.
# cadena utilizará el formato prefijo, con lo que no serán necesarios los paréntesis. Un ejemplo podría ser: + 1 2.
# Otro, más complejo, + 1 - 5 * 2 4, que se evalúa de izquierda a derecha como: sumarle a uno el resultado de restarle
# a cinco el producto de 2 por 4. Será obligatorio utilizar espacios como delimitadores entre signos y valores
# numéricos. Todas las operaciones soportadas emplearán dos operandos.
print('<--  EJERCICIO 3  -->')


def prefix_calculator(expr):
    expr_list = expr.split()
    operation = []
    nums = []
    infix_operation = []

    while len(expr_list) != 0:
        pop = expr_list.pop()
        if pop == '+' or pop == '*' or pop == '/' or pop == '-':
            operation.append(pop)
        else:
            nums.append(pop)

    for i in range(len(nums)):
        infix_operation.append(nums[i])
        if i < len(operation):
            infix_operation.append(operation[i])

    infix_operation.reverse()
    infix_string = ''.join(infix_operation)

    print(f'Operadores: {operation}, numeros: {nums}\nInfijo: {infix_string}')


prefix_calculator('* + 1 3 / 5 6')
