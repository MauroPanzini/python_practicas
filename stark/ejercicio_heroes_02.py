"""
Desafío #01:
Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
utilizando un menú (genérico) que permita acceder a cada uno de los puntos por
separado. Cada uno de los puntos debe ser desarrollado en una función distinta.
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
"""

from data_stark import lista_personajes

def mostrar_menu(lista):
    for elemento in lista:
        print(elemento)

def obtener_char(mensaje, mensaje_error):
    caracter = input(mensaje)
    caracter = caracter.lower()
    while len(caracter) > 1:
        caracter = input(mensaje_error)
        caracter = caracter.lower()
    return caracter

def elegir_opcion_alfanumerica():
    opcion = obtener_char("Ingrese una opción: \n", "Error, ingrese solo un caracter valido.")
    return opcion

def imprimir_masculinos(lista):
    for heroe in lista:
        if heroe["genero"] == 'M': 
            print(heroe["nombre"])

def imprimir_femeninos(lista):
    for heroe in lista:
        if heroe["genero"] == 'F':
            print(heroe["nombre"])

def determinar_alto_masculino(lista):
    mas_alto = None
    bandera = False
    for heroe in lista:
        if heroe["genero"] == 'M' and ( bandera == False or float(heroe["altura"]) > altura_mas_alto):
            bandera = True
            altura_mas_alto = float(heroe["altura"])
            mas_alto = heroe["nombre"]
    return mas_alto

def determinar_alto_femenino(lista):
    mas_alto = None
    bandera = False
    for heroe in lista:
        if heroe["genero"] == 'F' and (bandera == False or float(heroe["altura"]) > altura_mas_alto):
            bandera = True
            altura_mas_alto = float(heroe["altura"])
            mas_alto = heroe["nombre"]
    return mas_alto

def determinar_bajo_masculino(lista):
    mas_bajo = None
    bandera = False

    for heroe in lista:
        if heroe["genero"] == 'M' and (bandera == False or float(heroe["altura"]) < altura_mas_bajo):
            mas_bajo = heroe["nombre"]
            altura_mas_bajo = float(heroe["altura"])
            bandera = True
    return mas_bajo

def determinar_bajo_femenino(lista):
    mas_bajo = None
    bandera = False

    for heroe in lista:
        if heroe["genero"] == 'F' and (bandera == False or float(heroe["altura"]) < altura_mas_bajo):
            mas_bajo = heroe["nombre"]
            altura_mas_bajo = float(heroe["altura"])
            bandera = True
    return mas_bajo

def altura_promedio_masculino(lista):
    promedio = 0
    altura = 0
    contador = 0
    for heroe in lista:
        if heroe["genero"] == 'M':
            auxAltura = float(heroe["altura"])
            altura += auxAltura
            contador += 1
    promedio = altura/contador

    return promedio

def altura_promedio_femenino(lista):
    promedio = 0
    altura = 0
    contador = 0
    for heroe in lista:
        if heroe["genero"] == 'F':
            auxAltura = float(heroe["altura"])
            altura += auxAltura
            contador += 1
    promedio = altura/contador

    return promedio

def informar_nombres(c,d,e,f):
    print("\nEl superheroe masculino mas alto es", c)
    print("\nEl superheroe femenino mas alto es", d)
    print("\nEl superheroe masculino mas bajo es", e)
    print("\nEl superheroe femenino mas bajo es", f)

def determinar_cantidad_por_color_ojos(lista):
    lista_color_ojos = {}

    for heroe in lista:
        color_ojos = heroe["color_ojos"]
        if color_ojos in lista_color_ojos:
            lista_color_ojos[color_ojos] += 1
        else:
            lista_color_ojos[color_ojos] = 1
    
    return lista_color_ojos

def determinar_cantidad_por_color_pelo(lista):
    lista_color_pelo = {}

    for heroe in lista:
        color_pelo = heroe["color_pelo"]
        if color_pelo in lista_color_pelo:
            lista_color_pelo[color_pelo] += 1
        else:
            lista_color_pelo[color_pelo] = 1
    
    return lista_color_pelo

def determinar_cantidad_por_inteligencia(lista):
    lista_inteligencia = {}

    for heroe in lista:
        if heroe["inteligencia"] == "":
            heroe["inteligencia"] = "No tiene"
        
        inteligencia = heroe["inteligencia"]
        if inteligencia in lista_inteligencia:
            lista_inteligencia[inteligencia] += 1
        else:
            lista_inteligencia[inteligencia] = 1
    
    return lista_inteligencia

def listar_por_color_pelo(lista):
    heroes_por_pelo = {}

    for heroe in lista:
        color_pelo = heroe["color_pelo"]
        if color_pelo in heroes_por_pelo:
            heroes_por_pelo[color_pelo].append(heroe["nombre"])
        else:
            heroes_por_pelo[color_pelo] = [heroe["nombre"]]
    
    print(heroes_por_pelo)

def listar_por_color_ojos(lista):
    heroes_por_ojos = {}

    for heroe in lista:
        color_ojos = heroe["color_ojos"]
        if color_ojos in heroes_por_ojos:
            heroes_por_ojos[color_ojos].append(heroe["nombre"])
        else:
            heroes_por_ojos[color_ojos] = [heroe["nombre"]]
    
    print(heroes_por_ojos)

def listar_por_inteligencia(lista):
    heroes_por_inteligencia = {}
        
    for heroe in lista:
        if heroe["inteligencia"] == "":
            heroe["inteligencia"] = "No tiene"
        inteligencia = heroe["inteligencia"]
        if inteligencia in heroes_por_inteligencia:
            heroes_por_inteligencia[inteligencia].append(heroe["nombre"])
        else:
            heroes_por_inteligencia[inteligencia] = [heroe["nombre"]]
    
    print(heroes_por_inteligencia)


def main(lista):
    lista_menu =   ["A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M",
                    "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F",
                    "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M",
                    "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F",
                    "E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M",
                    "F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F",
                    "G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M",
                    "H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F",
                    "I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)",
                    "J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.",
                    "K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.",
                    "L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).",
                    "M. Listar todos los superhéroes agrupados por color de ojos.",
                    "N. Listar todos los superhéroes agrupados por color de pelo.",
                    "O. Listar todos los superhéroes agrupados por tipo de inteligencia"
    ]
    opcion = ''
    while opcion != 'z':
        mostrar_menu(lista_menu)
        opcion = elegir_opcion_alfanumerica()
        match opcion:
            case 'a':
                imprimir_masculinos(lista)
            case 'b':
                imprimir_femeninos(lista)
            case 'c':
                alto_masculino = determinar_alto_masculino(lista)
            case 'd':
                alto_femenino = determinar_alto_femenino(lista)
            case 'e':
                bajo_masculino = determinar_bajo_masculino(lista)
            case 'f':
                bajo_femenino = determinar_bajo_femenino(lista)
            case 'g':
                altura_masculino = altura_promedio_masculino(lista)
            case 'h':
                altura_femenino = altura_promedio_femenino(lista)
            case 'i':
                informar_nombres(alto_masculino,alto_femenino,bajo_masculino,bajo_femenino)
            case 'j':
                colores_ojos = determinar_cantidad_por_color_ojos(lista)
                print(colores_ojos)
            case 'k':
                colores_pelo = determinar_cantidad_por_color_pelo(lista)
                print(colores_pelo)
            case 'l':
                inteligencias = determinar_cantidad_por_inteligencia(lista)
                print(inteligencias)
            case 'm':
                listar_por_color_ojos(lista)
            case 'n':
                listar_por_color_pelo(lista)
            case 'o':
                listar_por_inteligencia(lista)
            case 'z':
                print("Gracias por elegir \033[31mStark Industries\033[0m")

        
main(lista_personajes)

