"""
Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido
Mauro Panzini
"""
lista = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

numeros_vistos = set()

for num in lista:
    if num in numeros_vistos:
        print("El numero", num, "está repetido")
        break
    numeros_vistos.add(num)
