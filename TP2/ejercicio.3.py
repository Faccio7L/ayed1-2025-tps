def verificacion_lista_hasta(lista_hasta:int) -> bool:
    """
    Chequea que la lista pueda generarse correctamente.
    pre: recibe como parametro un entero, que representa la cant de numeros de la lista.
    post: Retorna True si la lista puede generarse. Caso contrario, False.
    """
    return lista_hasta > 1

def lista_cuadrados(lista:list,desde:int, hasta:int)->list[int]:
    """
    completa una lista con la potencia de la posicion que ocupa cada numero.(posicion, no indice.)
    pre: Recibe como parametro una lista vacia, y un numero de posicion inicial y final.
    post: Retorna la lista completa.
    """
    for x in range(desde,hasta + 1):
        lista.append(x**2)
    return lista
def ultimos_diez_lista(lista:list[int])->list[int]:
    """
    Busca los ultimos numeros de una lista entera.
    pre: recibe como parametro una lista de numeros enteros.
    post: retorna la lista con los ultimos diez numeros de la misma.
    """
    return lista[-10:] #desde menos 10 hasta que termine.
    
def main()->None:
    """
    Crea una lista vacia, genera el limite de la lista e invoca al resto de funciones
    pre: No recibe parametros.
    post: Printea el retorno del resto de las funciones.
    """
    lista = []
    lista_desde = 1 #lo trabajo como variable, por si se desea modificar el valor.
    lista_hasta = int(input("Ingrese un numero para terminar la lista:"))
    if verificacion_lista_hasta(lista_hasta):
        print(f"La lista es: {lista_cuadrados(lista,lista_desde, lista_hasta)} ")
        print(f"los ultimos diez numeros de la lista son {ultimos_diez_lista(lista)}")
    else:
        print("Ingrese un numero mayor a uno.")
    
main()