"""
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
Mauro Panzini
"""

edad = input("Ingrese la edad de una persona")

edad = int(edad)
if (edad > 17):
        print("La persona es mayor de edad")
elif edad < 13:
    print("La persona es un niño")
else:
      print("La persona es adolescente")
