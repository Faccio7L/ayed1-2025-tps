def nueva_cadena(cadena:str, caracteres:int)->str:
    """
    Se muestran los ultimos caracteres de un string.
    pre: Una cadena y la cantidad de caracteres a mostrar.
    post: Texto nuevo.
    """
    texto_nuevo = cadena[-caracteres::]
    return texto_nuevo

def main()->None:
    """
    Se ingresa una cadena y la cantidad de caracteres que se desea ver. Tambien se
    invoca la funcion "nueva cadena."
    
    """
    cadena = input("Ingrese un texto")
    caracteres = int(input("Seleccione cuantos caracteres quiere ver:"))
    print(nueva_cadena(cadena,caracteres))
main()