import random as rn

def lista_numeros(cant_numeros:int,lista:list)-> list[int]:
    """
    Completa con la cantidad de numeros elegidos por el usuario una lista    
    pre: Recibe como parametro la lista vacia y la cantidad de numeros a appendear.
    post: Retorna la lista llena con numeros aleatorios del 1 al 100
    """

    for x in range(cant_numeros):
        lista.append(rn.randint(1,100))
    return lista

def verificar_elementos_repetidos(lista:list[int])-> bool:   
    """
    Verifica si hay numeros repetidos.
    pre: Recibe como parametro una lista de enteros.
    post: Retorna True en caso de que haya repetidos, caso contrario retorna False.
    """
    for x in lista:
        contar_cant = lista.count(x)
        if contar_cant >= 2:
            return True
    else:
        return False

def lista_no_repetidos(lista:list[int]) -> list[int]:
    """
    Toma una lista de enteros y genera una nueva sin repetidos
    pre: toma como parametros una lista de enteros.
    post: retorna una lista de numeros SIN repetir.
    """
    lista_sin_repetir = []
    for elemento in lista:
        contar_cant = lista.count(elemento)
        if contar_cant == 1:
            lista_sin_repetir.append(elemento)
    return lista_sin_repetir




def main()->None:
    """
    Genera una lista vacia, invoca al resto de funciones.
    pre: No recibe parametros.
    post: Printea los valores retornados por el resto de funciones.
    """
    lista = []
    cantidad_de_numeros = int(input("Ingrese cuantos numeros desea en la lista:"))
    print(f"La lista generada es:{lista_numeros(cantidad_de_numeros,lista)}")
    if verificar_elementos_repetidos(lista):
        print("Hay elementos repetidos.")
    else:
        print("NO hay elementos repetidos.")
    print(f"la lista sin repetidos es {lista_no_repetidos(lista)}")
main()