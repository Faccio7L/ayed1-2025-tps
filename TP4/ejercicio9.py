def ordenar_por_len(cadena:str)->str:
    """
    Se ordenan palabras por el len
    pre: recibe como parametros un str.
    
    """
    lista = cadena.split()
    sorted(lista, key=len) #ordeno por el largo de las palabras y no por el "valor!
    lista_a_string = " ".join(lista)
    return lista_a_string



def main()->None:
    """
    se ingresa una cadena y se invoca la funcion ordenar_por_len
    
    """
    cadena = input("Ingrese una cadena de caracteres:")
    print(ordenar_por_len(cadena))
main()