import json

def cargar_inventario(nombre_archivo):
    with open(nombre_archivo) as archivo:
        inventario = json.load(archivo)
    return inventario

inventario = cargar_inventario("database.json")

def guardar_nuevo_inventario(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo)

def agregar_producto(inventario, producto):
    for elemento in inventario["data"]:
        if elemento["nombre"] == producto["nombre"]:
            return
    inventario["data"].append(producto)
    guardar_nuevo_inventario("database.json", inventario)
    print("Producto agregado exitosamente.")

def eliminar_producto(inventario, nombre_producto):
    
    for producto in inventario["data"]:
        if producto["nombre"] == nombre_producto:
            inventario["data"].remove(producto)
            producto_encontrado = True
            break
    if producto_encontrado:
        guardar_nuevo_inventario("database.json", inventario)
        print("Producto eliminado exitosamente.")
    else:
        print("El producto no se encontró en el inventario, por lo tanto no podemos removerlo.")

def buscar_producto(inventario, clave, valor):
    resultados = []  
    for item in inventario["data"]:  
        if clave in item and item[clave] == valor:  
            resultados.append(item)  
    return resultados

def actualizar_producto(inventario, nombre_producto, nueva_cantidad, nuevo_precio):
    for item in inventario["data"]:     
        if item["nombre"] == nombre_producto:  
            item["cantidad"] = nueva_cantidad  
            item["precio"] = nuevo_precio  
            guardar_nuevo_inventario("database.json", inventario) 
            print("Perfecto, el producto ha sido agregado con éxito.")  
            
def mostrar_inventario(inventario):
    for item in inventario["data"]:
        if "nombre" in item:
            print("Nombre:", item["nombre"])
        if "categoria" in item:
            print("Categoria:", item["categoria"])
        if "cantidad" in item:
            print("Cantidad:", item["cantidad"])
        if "precio" in item:
            print("Precio:", item["precio"])
        print("-----------------------")