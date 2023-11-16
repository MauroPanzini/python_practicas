from data_stark import lista_personajes
import re

def mostrar_menu(lista):
    for elemento in lista:
        print(elemento)

def obtener_char(mensaje:str, mensaje_error:str):
    caracter = input(mensaje)
    caracter = caracter.lower()
    while len(caracter) > 1:
        caracter = input(mensaje_error)
        caracter = caracter.lower()
    return caracter

def elegir_opcion_alfanumerica():
    opcion = obtener_char("Ingrese una opción: \n", "Error, ingrese solo un caracter valido.")
    return opcion

def extraer_iniciales(nombre):
    if nombre != '':
        nombre = nombre.replace("-", " ")
        
        nombre = re.sub(r"\bThe\b\s?", "", nombre)
        
        partes = nombre.split()
        
        initials = [parte[0] for parte in partes]
        
        iniciales_con_punto = ".".join(initials) + "."
    else:
        iniciales_con_punto = 'N/A'
    
    return iniciales_con_punto

def definir_iniciales_nombre(heroe):
    if not isinstance(heroe, dict):
        return False
    
    if 'nombre' not in heroe:
        return False
    
    iniciales = extraer_iniciales(heroe['nombre'])
    
    heroe['iniciales'] = iniciales
    
    return True

def agregar_iniciales_nombre(lista_heroes):
 
    if not isinstance(lista_heroes, list):
        print("El origen de datos no contiene el formato correcto")
        return False
    
    if len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")
        return False
    
    for heroe in lista_heroes:
        if not definir_iniciales_nombre(heroe):
            print("El origen de datos no contiene el formato correcto")
            return False
    
    return True

def stark_imprimir_nombres_con_iniciales(lista_heroes):
    if not isinstance(lista_heroes, list):
        print("El origen de datos no contiene el formato correcto")
        return
    
    if len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")
        return
    
    if not agregar_iniciales_nombre(lista_heroes):
        return
    
    for heroe in lista_heroes:
        nombre = heroe.get("nombre")
        iniciales = heroe.get("iniciales")
        print(f"* {nombre} ({iniciales})")

def generar_codigo_heroe(id_heroe, genero_heroe):
    if not isinstance(id_heroe, int) or not genero_heroe or genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'
    
    codigo = f"{genero_heroe}-{'0'*(9-len(str(id_heroe)))}{id_heroe}"
    if len(codigo) > 10:
        codigo = codigo[-10:]
    
    return codigo

def agregar_codigo_heroe(heroe, id_heroe):
    if not heroe:
        return False
    
    codigo = generar_codigo_heroe(id_heroe, heroe.get('genero_heroe', ''))
    
    if len(codigo) != 10:
        return False
    
    heroe['codigo_heroe'] = codigo
    return True

def stark_generar_codigos_heroes(lista_heroes):
    if not isinstance(lista_heroes, list) or len(lista_heroes) == 0:
        print("El origen de datos no contiene el formato correcto")
        return

    for i, heroe in enumerate(lista_heroes):
        if not isinstance(heroe, dict) or 'genero' not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return

        id_heroe = i + 1
        codigo_heroe = generar_codigo_heroe(id_heroe, heroe['genero'])

        if not agregar_codigo_heroe(heroe, id_heroe):
            print("El origen de datos no contiene el formato correcto")
            return

    cantidad_codigos = len(lista_heroes)
    print(f"Se asignaron {cantidad_codigos} códigos")
    print(f"* El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}")
    print(f"* El código del último héroe es: {lista_heroes[-1]['codigo_heroe']}")

def sanitizar_entero(numero_str):
    numero_str = numero_str.strip() 
    if not numero_str.isnumeric():
        return -1
    numero = int(numero_str)
    if numero < 0:
        return -2
    return numero

def sanitizar_flotante(numero_str):
    numero_str = numero_str.strip() 
    try:
        numero = float(numero_str)
        if numero < 0:
            return -2
        return numero
    except ValueError:
        return -1
    except TypeError:
        return -3

