"""Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona."""

nombre = input("Ingrese el nombre del empleado: \n")
sueldo = input("Ingrese el sueldo del empleado: \n")

sueldo = int(sueldo)

sueldo_incrementado = sueldo + (sueldo * 10)/100

print("Se aplicó el aumento del 10%, el sueldo de",nombre ,"es ahora de", sueldo_incrementado)