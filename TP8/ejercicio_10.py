#HACER ASSERTS.
def eliminar_claves(diccionario:dict,claves:list = ["hola","3","juan","1", "martin"])->tuple:
    """
    Elimina claves de un diccionario.
    pre: Recibe como parametro un diccionario y claves a eliminar(lista)
    post:Retorna el diccionario con claves eliminadas y contador de claves eliminadas.

        
    """
    claves_lista = []
    for clave, valor in diccionario.items(): 
         claves_lista.append(clave)
    
    contador = 0
    
    for claves in claves_lista: #no puedo usar pop MIENTRAS itero el mismo diccionario, por eso iterlo la lista de ahi usar el pop!
        if clave in claves:
            diccionario.pop(clave)
            contador += 1
    
    return diccionario,contador


def main()->None:
    """
    Se genera un diccionario con values consecutivos(1,2,3) y claves ingresadas por el
    usuario, tambien se invoca la funcion eliminar_claves.
    """
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

