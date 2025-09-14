import random as rn

def modificar_lista(lista:list[int],lista_2:list[int])->tuple:
    """
    Modifica una lista en base a los numeros que hay en comun en ambas, por cada elemento
    repetido lo elimina UNA vez de la lista, a no ser que vuelva a encontrarse en la lista 2.
    principal.
    pre: Recibe como parametro dos listas de enteros.
    post: Retorna la lista sin los elementos repetidos.
    """
   
    lista_modificada = [x for x in lista if x not in lista_2]
            
    return lista_modificada

def main()->None:
    """
    Genera y llena lista con numeros random, invoca a una funcion que las modifica.
    pre: No parametros.
    post: Printea el resultado de las listas generadas y del resultado de la funcion modificar_lista.
    """
    lista = []
    lista_2 = []
    for x in range(20):
        num = rn.randint(1,15)
        lista.append(num)
    print(lista)
    for x in range(12):
        num = rn.randint(1,15)
        lista_2.append(num)
    print(f"La lista 1 generada automaticamente es:{lista}")
    print(f"La lista 2 generada automaticamente es:{lista_2}")
    lista_nueva  = modificar_lista(lista,lista_2)
    print(f"La lista 1 sin los numeros en comun entre ambas es:{lista_nueva}")    
    
main()