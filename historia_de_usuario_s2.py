inventario=[]
while True:
    print("*"*30)
    print("Bienvenido".center(30))
    print("*"*30)
    print("1. Agrega producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    opcion=input("\n Escoja la opción deseada: ")
    if opcion=="1":
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
        print(inventario)
    elif opcion=="2":
        if inventario==[]:
            print("El inventario está vacío")
        else:
            for i in inventario:
                print(f"Nombre:{i['nombre']} | Precio:{i['precio']} | Cantidad:{i['cantidad']}")