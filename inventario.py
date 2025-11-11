#solicita datos al usuario y evalúa el ingreso de almenos 1 caracter
while True:
    nombre=input("Ingrese el nombre del producto\n")
    if nombre=="":
        print("Debes ingresar algún nombre en el espacio")
    else:
        break
#Solicita datos al usuario, evalúa que sea valor numérico
while True:
    try:
        precio=float(input("¿Qué precio tiene la unidad?\n"))
        break
    except:
        print("El valor ingresado debe ser un número")
#Solicita datos al usuario, evalúa que sea valor numérico
while True:
    try:
        cantidad=int(input(f"¿Cuántas unidades de {nombre} hay?\n"))
        break
    except:
        print("El valor ingresado debe ser un número entero")
#calcula el costo total e imprime los datos antes guardados
costo_total=precio*cantidad
print(f"Producto:{nombre}\nprecio:{precio}\ncantidad:{cantidad}\ntotal:{costo_total}")

"""El programa recolecta diferentes datos de un producto(nombre, precio, cantidad), evalúa 
el correcto ingreso de estos y al final imprime el producto, sus caracteristicas y el costo total"""