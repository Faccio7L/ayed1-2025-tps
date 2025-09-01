import random as rn
def cuatro_numeros_random(lista:list) ->list[int]:
    """
    recibe una lista vacia y appendea una con 4 numeros random de 1000 a 9999
    pre: Recibe una lista vacia
    post: Retorna una lista con 4 numero.
    """
    for x in range(rn.randint(1,100)):
        lista.append(rn.randint(1000,9999))
    return lista


def eliminar_de_La_lista(lista:list[int]) -> bool:
    """
    Elimina un numero de una lista en caso de que exista.
    pre: recibe la lista de enteros
    post: Retorna la lista con el numero eliminado.
    """
    numero_a_eliminar = int(input("Ingrese un numero que desea eliminar:"))
    if numero_a_eliminar in lista:
        lista.remove(numero_a_eliminar)
    return lista
    
def lista_capicua(lista:list[int]) -> bool:
    """
    Verifica si una lista es capicua.
    pre: Recibe como parametro una lista.
    post: Retorna True o False, True en caso de que sea capicua.
    """
    return lista == lista[::-1]

def calcular_producto(lista:list[int])-> int: #interpreto que la consigna se refiere a esto.
    """
    Calcula el producto de una lista(funciona con cualquier iterable)
    pre:Recibe como parametro una lista de enteros.
    post: retorna el producto (entero) de la lista.
    """
    producto = 1
    for numero in lista:
        producto *= numero
    return producto     
    
def main()-> None:
    """
    Crea una lista vacia, invoca el resto de funciones y printea su return.
    pre: No recibe parametros.
    post: Printea informacion sobre el resto de funciones
    """
    lista = []
    print(f"La lista generada de manera aleatoria es {cuatro_numeros_random(lista)}")
    print(f"El producto de la lista anterior es {calcular_producto(lista)}")
    print(f"Ahora la lista es {eliminar_de_La_lista(lista)}")
    if lista_capicua(lista):
        print("Su lista es capicua")
    else:
        print("Su lista no es capicua")
#test
assert lista_capicua([1,3,1]) == True
assert calcular_producto([2,5,3]) == 30


main()
