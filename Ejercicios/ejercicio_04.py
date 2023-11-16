"""
Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.
Mauro Panzini
"""
edad = input("Ingrese la edad de la persona: \n")
edad = int(edad)

estado_civil = input("Ingrese el estado civil (soltero, casado, viudo, divorciado): \n")
estado_civil = estado_civil.lower()
while (estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "viudo" and estado_civil != "divorciado"):
    estado_civil = input("Error, ingrese un estado civil válido (soltero, casado, viudo, divorciado))\n")
    estado_civil = estado_civil.lower()
if edad < 18 and estado_civil != "soltero":
    print("Es muy pequeño para NO ser soltero!!!")