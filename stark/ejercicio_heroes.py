from data_stark import lista_personajes

menu = ["B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe\n",
        "C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo\n",
        "D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)\n",
        "E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)\n",
        "F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)\n",
        "H. Calcular e informar cual es el superhéroe más y menos pesado.\n",
        "Z. Salir.\n"]

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
    obtener_char("Ingrese una opción: \n", "Error, ingrese solo un caracter valido.")

def obtener_numero(mensaje, mensaje_error, max, min):
    numero = input(mensaje)
    
    while numero.isdigit() == False:
       print(mensaje_error)
       numero = input(mensaje)
    numero = int(numero)

    while numero > max or numero < min or numero == None:
        print(mensaje_error)
        numero = input(mensaje)
        numero = int(numero)
    
    return numero

def elegir_opcion_numerica(max, min):
    opcion = obtener_numero("Seleccione una opcion: \n", "Error, ingrese una opcion valida: \n", max, min)
    return opcion

def imprimir_nombres(lista):
    for heroe in lista:
        print(heroe["nombre"])

def imprimir_nombre_altura(lista):
     for heroe in lista:
        print(heroe["nombre"], heroe["altura"])

def imprimir_mas_alto(lista):
    bandera = False
    mas_alto = None
    for heroe in lista:
        if bandera == False or altura_mas_alto < float(heroe["altura"]):
            mas_alto = heroe["nombre"]
            altura_mas_alto = float(heroe["altura"])
            bandera = True
    print("El heroe mas alto es", mas_alto, "con una altura de", altura_mas_alto, "\n")

def imprimir_mas_bajo(lista):
    bandera = False
    mas_bajo = None
    for heroe in lista:
        if bandera == False or altura_mas_bajo > float(heroe["altura"]):
            mas_bajo = heroe["nombre"]
            altura_mas_bajo = float(heroe["altura"])
            bandera = True
    print("El heroe mas bajo es", mas_bajo, "con una altura de", altura_mas_bajo, "\n")

def imprimir_altura_promedio(lista):
    acumulador = 0
    contador = 0
    for heroe in lista:
        acumulador += float(heroe["altura"])
        contador += 1
    promedio = acumulador / contador
    print("El promedio de altura es", promedio)

def imprimir_pesado_liviano(lista):
    bandera_pesado = False
    bandera_liviano = False
    nombre_mas_pesado = None
    nombre_mas_liviano = None
    for heroe in lista:
        if bandera_pesado == False or mas_pesado < float(heroe["peso"]):
            mas_pesado = heroe["peso"]
            nombre_mas_pesado = ["nombre"]
            bandera_pesado = True
        if bandera_liviano == False or mas_liviano > float(heroe["peso"]):
            mas_liviano = heroe["peso"]
            nombre_mas_liviano = ["nombre"]
            bandera_liviano = True
    
    print("El heroe mas pesado es", nombre_mas_pesado,"con un peso de", mas_pesado, "kg\n")
    print("El heroe mas liviano es", nombre_mas_liviano,"con un peso de", mas_liviano, "kg\n")

bandera = False
while bandera == False or opcion != 7:
    bandera = True
    mostrar_menu(menu)
    opcion = elegir_opcion_alfanumerica()
    match opcion: 
        case 'b':
            imprimir_nombres(lista_personajes)
        case 'c':
            imprimir_nombre_altura(lista_personajes)
        case 'd':
            imprimir_mas_alto(lista_personajes)
        case 'e':
            imprimir_mas_bajo(lista_personajes)
        case 'f':
            imprimir_altura_promedio(lista_personajes)
        case 'h':
            imprimir_pesado_liviano(lista_personajes)
        case 'z':
            print("Gracias por elegir mi programa!!!!")    
