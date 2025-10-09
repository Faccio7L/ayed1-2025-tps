def buscar_clave(diccionario:dict,valor:str ="hola")->list:
    """
    Busca las claves que tengan el value pasado como parametro(default hola)
    pre: diciconario, value a buscar.
    post: lista de claves que contienen ese value.
    """
    lista_de_claves = []
    for clave, value in diccionario.items():
        if value == valor:
            lista_de_claves.append(clave)
    return lista_de_claves

def main()->None:
    """
    Genera un diccionario que los key son numeros consecutivos(desde 0) y el usuario
    los completa con los value que desee. 
    """
    diccionario = dict()
    clave = 0
    while True:
        value = input("Ingrese un value(0 para salir.)")
        if value == "0":
            break
        else:
            diccionario[clave] = value
            clave += 1
    print(diccionario)
    print(buscar_clave(diccionario))
main()

