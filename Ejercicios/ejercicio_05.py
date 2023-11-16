"""
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos
Mauro Panzini
"""
precio_base = 15000
precio_final = 0
estacion = input("Ingrese la estación del año en la que viajará:\n")
estacion = estacion.lower()
while estacion != "invierno" and estacion != "verano" and estacion != "primavera" and estacion != "otoño":
    estacion = input("Error, ingrese una estación válida:\n")
    estacion = estacion.lower()
localidad = input("Ingrese el destino del viaje (Bariloche/Cataratas/Mar del Plata/Córdoba):\n")
localidad = localidad.lower()
while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "cordoba":
    localidad = input("Error, ingrese un destino válido:\n")
    localidad = localidad.lower()

match estacion:
    case "invierno":
        match localidad:
            case "bariloche":
                precio_final = precio_base + (precio_base * 20) / 100
            case "cataratas" | "cordoba":
                precio_final = precio_base - (precio_base * 10) / 100
            case "mar del plata":
                precio_final = precio_base - (precio_base * 20) / 100
    case "verano": 
        match localidad:
            case "bariloche":
                precio_final = precio_base - (precio_base * 20) / 100
            case "cataratas" | "cordoba":
                precio_final = precio_base + (precio_base * 10) / 100
            case "mar del plata":
                precio_final = precio_base + (precio_base * 20) / 100
    case _:
        match localidad:
            case "cordoba":
                precio_final = 15000
            case _:
                precio_final = precio_base + (precio_base * 10) / 100

print("El destino elegido fue", localidad, "en", estacion, ", entonces el precio por día queda en $", precio_final)









"""
continuar = True
contador_numeros = 0
acumulador_numeros = 0
promedio = 0
while continuar == True:
    numero = input("Ingrese un número: ")
    numero = int(numero)
    contador_numeros += 1
    acumulador_numeros += numero
    continuar = input("Desea ingresar mas números? s/n: ")
    if continuar == 's':
        continuar = True
    elif continuar == 'n':
        continuar = False
        promedio = acumulador_numeros/contador_numeros
        contador_numeros = str(contador_numeros)
        acumulador_numeros = str(acumulador_numeros)
        promedio = str(promedio)
        print ("Se acumularon en total " + contador_numeros + " numero/s")
        print ("La suma da un total de " + acumulador_numeros)
        print ("El promedio es de " + promedio)
    else: 
         continuar = input("Desea ingresar mas números? s/n: ")
"""