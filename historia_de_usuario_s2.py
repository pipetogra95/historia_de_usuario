inventario=[]
total=0
productos=0
def agregar_producto():
    producto={}
    nombre=input("Nombre del producto: ")
    precio=(input("Precio del producto: "))
    while not precio.replace(".","",1).isdigit() or float(precio)==0:
        print("Debe ser un valor numérico mayor a cero")
        precio=(input("Precio del producto: "))
    precio=float(precio)
    cantidad=(input("¿Cúantas unidades hay?: "))
    while not cantidad.isdigit() or int(cantidad)==0:
        print("Debe ser un número entero mayor a cero")
        cantidad=(input("¿Cúantas unidades hay?: "))
    cantidad=int(cantidad)
    producto.update({
        "nombre":nombre,
        "precio":precio,
        "cantidad":cantidad    
    })
    inventario.append(producto)
def mostrar_inventario():
    if inventario==[]:
        print("El inventario está vacío")
    else:
        for i in inventario:
            print(f"Nombre:{i['nombre']} | Precio:{i['precio']} | Cantidad:{i['cantidad']}")
def calcular_estadisticas():
    global productos, total
    if inventario==[]:
        print("El inventario está vacío")
    else:    
        for i in inventario:
            valor1 =i["precio"]*i["cantidad"]
            total +=valor1
            productos +=1
        print(f"la suma total del inventario es: {total}")
    print(f"Se agregaron {productos} nuevos productos")
def menu():
    while True:
        print("*"*30)
        print("Bienvenido".center(30))
        print("*"*30)
        print("1. Agrega producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        print("*"*30)
        opcion=input("Escoja la opción deseada: ")
        print("\n")
        if opcion=="1":
            agregar_producto()
        elif opcion=="2":
            mostrar_inventario()
        elif opcion=="3":
            calcular_estadisticas()
        elif opcion=="4":
            print("Salida exitosa")
            break
        else:
            print("Opción inválida")
menu()
