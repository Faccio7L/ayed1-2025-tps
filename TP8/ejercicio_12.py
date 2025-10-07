def incremento_cuadernos(diccionario):
    for clave , values in diccionario.items():
        if values["es cuaderno"] == "si":
            values["precio"] = values["precio"] * 1.15
    print(diccionario)



def llenar_diccionario():
    validar_precio = lambda x: x > 0
    diccionario = {}
    while True:
        nombre_del_producto = input("Ingrese el nombre del producto(0 para salir):")
        if nombre_del_producto == "0":
            break
        precio = int(input("Ingrese el precio:"))
        if validar_precio(precio):
            es_libro = input("¿Es un cuaderno?(1 si,0 u otra opcion no):")
            if es_libro == "1":
                diccionario[nombre_del_producto] = {"precio": precio, "es cuaderno" :"si"} #puse un value llamado es cuaderno para que no se aplique el incremento solo a un elemento llamado cuaderno, sino que a TODOS los cuadernos.
            else:
                diccionario[nombre_del_producto] = {"precio" : precio, "es cuaderno" : "no"}
        for key, value in diccionario.items():
            print(f"{key} {value}")
    incremento_cuadernos(diccionario)
llenar_diccionario()