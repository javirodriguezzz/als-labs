def decompose(x):
    x_str = str(x)
    x_split = x_str.split()
    print(x_split)


# Dividir entre 10 y tomar el resto hasta agotar el número. 365 -> 36, 5 -- 36 -> 3, 6
# l.insert(0, x)
def decompose_v2(x):
    list = []
    numero = float(x)
    while numero > 0:
        list.insert(0, numero % 10)
        numero = int(numero / 10)
    print(list)


# x = input('Introduce un número: ')
# print('Descompuesto en: ')
# decompose_v2(x)

# Determinar las frecuencias de aparición de palabras en un texto
def word_counter(text):
    list = text.split()
    dict = {}
    for l in list:
        # dict2 = {l: 0}
        # dict.update(dict2)
        if l in dict.keys():
            dict[l] += 1
        else:
            dict[l] = 1
    print(dict)


# word_counter('Esto es una prueba prueba')


# Ejercicio 1. Crea una función decodificadora de fechas. Aceptará fechas del estilo “12 Feb 2015”, y las convertirá
# al sistema ISO-8601, es decir, “2015-02-12” en el ejemplo.
def date_decode(date):
    months = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }

    list = date.split(' ')
    toret = [list.pop(), '-', months[list.pop()], '-', list.pop()]

    toret_str = ''.join(toret)
    print(toret_str)


date_decode('12 Feb 2015')


# Ejercicio 2. Supón las siguientes líneas de datos. La primera especifica los nombres de las empresas, y las
# siguientes la empresa, la fecha del lunes de esa semana, y las ventas para cada día de la semana. Crea una función
# que lea esa información como una cadena de texto separada por cambios de línea, y genere un informe que sea sencillo
# de entender por el ser humano.
def generate_inform(text):
    toret = []
    txt_list = text.splitlines()
    enterprises = txt_list[0].split(',')
    enterprises_dict = {enterprises[i]: enterprises[i + 1] for i in range(0, len(enterprises), 2)}

    for j in range(1, len(txt_list)):
        line = txt_list[j].split(',')
        company = line[0]
        for k in enterprises_dict.keys():
            var = enterprises_dict[k]
            if company == var:
                toret.append(enterprises_dict[k])

    print(toret)


generate_inform('Microsoft, 1, Apple, 2\n1, 2015-01-09, 120, 34, 256, 78, 93, 222, 5\n2, 2015-01-09, 900, 346, 730, 456, 33, 345, 234')


# Ejercicio 3. Crea un programa que permita guardar y hacer búsquedas sobre pares de (nombre, e.mail). El programa
# presentará un menú principal, con las opciones introducir, borrar y buscar. Al introducir datos, se pide un nombre y
# un e.mail, y se guardan. Para borrar, sólo se pide el nombre, se busca y se borra. Para buscar, sólo se pide el
# nombre, se busca y se muestra.
def email_gest():
    email_dict = {}
    while True:
        print('1. Insert email\n2. Delete email\n3. Search email\n4. List emails\n0. Exit')
        c = input('Choose option: ')

        if c == '1':
            name = input('Insert name: ')
            email = input('Insert email: ')
            email_dict.update({name: email})
        if c == '2':
            name = input('Insert name: ')
            del email_dict[name]
        if c == '3':
            name = input('Insert name: ')
            toret = email_dict[name]
            if toret:
                print(f'The email of {name} is {toret}')
            else:
                print('User not found')
        if c == '4':
            for i in email_dict.keys():
                print(f'User: {i}, Email: {email_dict[i]}')
        if c == '0':
            break


email_gest()


# Ejercicio 4. Crea una función que genere números pseudo-aleatorios, puedes obtener varias ideas en la Wikipedia.
# Una vez hayas escrito la función, comprueba cómo de buena es creando una segunda función que compruebe las
# frecuencias de aparición de, por ejemplo, los enteros entre 0 y 100.
# TODO - Implement method