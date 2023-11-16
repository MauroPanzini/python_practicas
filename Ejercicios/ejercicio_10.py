"""
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]
Mauro Panzini
"""
contador = 0
lista_alumnos =\
[
  {
        "nombre": "",
        "sexo": "",
        "nota": ""
  },
  {
        "nombre": "",
        "sexo": "",
        "nota": ""
  },
  {
       "nombre": "",
        "sexo": "",
        "nota": ""
  },
  {
        "nombre": "",
        "sexo": "",
        "nota": ""
  },
  {
        "nombre": "",
        "sexo": "",
        "nota":""
  }
]
for alumno in lista_alumnos:
    alumno["nombre"] = input("Ingrese el nombre del alumno: \n") 
    alumno["sexo"] = input("Ingrese el sexo del alumno: \n")
    alumno["nota"] = input("Ingrese la nota del alumno: \n")

print(lista_alumnos)
