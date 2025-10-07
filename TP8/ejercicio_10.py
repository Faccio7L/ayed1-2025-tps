def eliminar_claves(diccionario,claves = ["hola","3","juan","1", "martin"]):
    claves_lista = []
    for clave, valor in diccionario.items(): 
         claves_lista.append(clave)
    
    contador = 0
    
    for claves in claves_lista: #no puedo usar pop MIENTRAS itero el mismo diccionario, por eso iterlo la lista de ahi usar el pop!
        if clave in claves:
            diccionario.pop(clave)
            contador += 1
    
    return diccionario,contador


def main():
    diccionario = dict()
    value = 1
    while True:
        clave = input("Ingrese una clave (0 para salir:)")
        if clave == "0":
            break
        else:

            diccionario[clave] = value
            value += 1 #para completar con values random
    print(diccionario)
    print(eliminar_claves(diccionario))


main()
