contador_vueltas = 0
contador_jabon = 0
contador_barbijo = 0
contador_alcohol = 0
bandera_precio_barbijos = False
bandera_unidades = False

while contador_vueltas < 5:

    producto = input("Ingrese el producto: \n")
    producto = producto.lower()
    print(producto)
    while (producto != "jabon" and producto != "barbijo" and producto != "alcohol"):
        producto = input("Error, ingrese el producto correctamente: \n")
        producto = producto.lower()

    precio = input("Ingrese el precio del producto: \n")
    precio = int(precio)
    while precio > 300 or precio < 100:
        precio = input("Error, ingrese el precio del producto (debe estar entre 100 y 300): \n")
        precio = int(precio)
    
    cantidad_unidades = input("Ingrese la cantidad de unidades: \n")
    cantidad_unidades = int(cantidad_unidades)    
    while cantidad_unidades > 1000 or cantidad_unidades < 1:
        cantidad_unidades = input("Error, ingrese la cantidad de unidades (no puede ser inferior a 1 ni superior a 1000 unidades): \n")
        cantidad_unidades = int(cantidad_unidades) 
    
    marca = input("Ingrese la marca del producto: \n")
    fabricante = input("Ingrese el fabricante del producto: \n")

    match producto:
        case "jabon":
            contador_jabon += cantidad_unidades
        case "barbijo":
            contador_barbijo += cantidad_unidades
        case "alcohol":
            contador_alcohol += cantidad_unidades
    
    if producto == "barbijo" and bandera_precio_barbijos == False:
        barbijo_fabricante = fabricante
        barbijo_unidades = cantidad_unidades
        barbijo_precio = precio
        bandera_precio_barbijos = True
    elif producto == "barbijo" and barbijo_precio < precio:
        barbijo_fabricante = fabricante
        barbijo_unidades = cantidad_unidades
        barbijo_precio = precio
    
    if bandera_unidades == False:
        item_mas_unidades = fabricante
        cantidad_mas_unidades = cantidad_unidades
        bandera_unidades = True
    elif cantidad_mas_unidades < cantidad_unidades:
        item_mas_unidades = fabricante
        cantidad_mas_unidades = cantidad_unidades

    contador_vueltas += 1 

print("\nEl mas caro de los barbijos tiene una cantidad de ", barbijo_unidades, "y es fabricado por ",barbijo_fabricante,"\n") 
print("El item con mas unidades es del fabricante ", item_mas_unidades, ", con ", cantidad_mas_unidades, " unidades")
if contador_jabon > 0:
    print("La cantidad de jabones es ", contador_jabon)