"""
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
Mauro Panzini
"""

contador = 0
bandera_menor_numero = False
bandera_pares = False
cantidad_pares = 0
cantidad_impares = 0
suma_positivos = 0
producto_negativos = 1

while contador < 5:
    numero = input("Ingrese un numero entero distinto de 0: \n")
    numero = int(numero)
    while numero == 0:
        numero = input("Error, ingrese un numero entero distinto de 0: \n")
        numero = int(numero)
    
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
    
    if bandera_menor_numero == False:
       menor_numero = numero
       bandera_menor_numero = True
    elif menor_numero > numero:
        menor_numero = numero

    if bandera_pares == False and numero % 2 == 0:
        mayor_par = numero
        bandera_pares = True
    elif numero % 2 == 0 and mayor_par < numero:
        mayor_par = numero
     
    if numero > 0:
        suma_positivos += numero

    if numero < 0:
        producto_negativos = producto_negativos * numero

    contador += 1
print("\nHay un total de", cantidad_pares, "numeros pares, y", cantidad_impares, "numeros impares")
print("\nEl menor numero ingresado fue", menor_numero)
print("\nEl mayor numero par ingresado fue el", mayor_par)
print("\nLos números positivos suman un total de", suma_positivos)
print("\nEl producto de los numeros negativos es de", producto_negativos)