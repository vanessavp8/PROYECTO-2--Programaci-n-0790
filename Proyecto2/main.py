from inventario.crud import cargar_inventario, agregar_producto, eliminar_producto, buscar_producto, actualizar_producto, mostrar_inventario

def menu_principal():
    print("¿Cómo podemos ayudarte? Selecciona que deseas hacer.")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Buscar Producto")
    print("4. Actualizar Producto")
    print("5. Mostrar Inventario")
    print("6. Salir")
    return input("Seleccione una opción: ")

# Cargar el inventario desde el archivo JSON
inventario = cargar_inventario("database.json")

while True:
    opcion = menu_principal()

    if opcion == "1":
        nuevo_producto = {
            "nombre": (input("Ingrese el nombre del producto: ")),
                "categoría": (input("Ingrese la categoría del producto: ")),
            "precio": float(input("Ingrese el precio del producto: ")),
            "cantidad": int(input("Ingrese la cantidad en stock del producto: "))
        }
        agregar_producto(inventario, nuevo_producto)

    elif opcion == "2":
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
        eliminar_producto(inventario, nombre_producto)
        
    elif opcion == "3":
        tipo_busqueda = input("¿Desea buscar por nombre o categoría? ")
        key_value = input("Ingrese ahora de forma específica lo que desea ver: ")
        resultados = buscar_producto(inventario, tipo_busqueda, key_value)
        if len(resultados) == 0:
            print("No encontramos ningún resultado.")
        else:
            print("Resultados encontrados:")
            for resultado in resultados:
                print(resultado)
           

    elif opcion == "4":
        nombre_producto = input("Ingrese el nombre del producto a actualizar: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        actualizar_producto(inventario, nombre_producto, nueva_cantidad, nuevo_precio)

    elif opcion == "5":
        mostrar_inventario(inventario)

    elif opcion == "6":
        print("Esperamos poder haberte ayudado. ¡Vuelve pronto!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")