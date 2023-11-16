"""Se tiene la siguiente lista de diccionarios:
lista_diccionario = [{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
{'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
{'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
{'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
{'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

Hacer una copia deep copy y trabajar con la copia, de acuerdo a lo siguiente:
De debera mapear al precio con iva, sumando el 21% sobre el precio sin iva.
Mostrar los datos por pantalla.
Modificar el nombre de Destornillador por Destornillador Philips.
Mostrar los datos por pantalla.
Agregar una herramienta con sus respectivos datos.
Mostrar los datos.
Eliminar dos herramientas que no sean ni la primera ni la ultima y agregarlas a una lista de herramientas eliminadas.
Mostrar los datos.

Mostrar los datos de la lista original, la lista trabajada y la lista de herramientas eliminadas."""

lista_diccionario = [
    {'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
    {'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
    {'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
    {'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
    {'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

from copy import deepcopy

copia_lista = deepcopy(lista_diccionario)

def calcualr_iva(lista):
    for elemento in lista:
        precio_sin_iva = elemento['precio'].get('sin_iva')
        precio_con_iva = precio_sin_iva + precio_sin_iva * 0.21
        elemento['precio'].update({'con_iva': precio_con_iva})

    for i in range(len(copia_lista)):
        print(lista[i])

def modificar_nombre(lista, criterio:str,reemplazo:str):
    for elemento in lista:
        if elemento.get('nombre') == criterio:
            elemento.update({'nombre': reemplazo})
            break
    print(lista)

def agregar_herramienta(lista, nombre:str, precio_sin_iva:float):
    lista.append({'nombre': nombre, 'precio':{'sin_iva': precio_sin_iva}})
    for elemento in lista:
        print(elemento)

print('-----------------------------------')
calcualr_iva(copia_lista)
print('-----------------------------------')
modificar_nombre(copia_lista, 'Destornillador', 'Destornillador Philips')
print('-----------------------------------')
agregar_herramienta(copia_lista, 'Tenaza', 1200)
print('-----------------------------------')
