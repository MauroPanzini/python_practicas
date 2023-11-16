"""
Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven
Mauro Panzini
"""
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
bandera = False
contador = 0

for edad in edades:
    if bandera == False or edad < edad_minima:
        indice = contador
        edad_minima = edad
        bandera = True
    contador += 1
    
print(f"La persona mas joven es {nombre[indice]} y tiene {edades[indice]} años")

