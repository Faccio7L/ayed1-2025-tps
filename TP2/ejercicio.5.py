import random as rn
def ordenada_ascendente(lista:list[int] = [3,5,6])-> bool: #recibe una lista default. Podria ingresar una el usuario!!
    """
    evalua si una lista entera esta ordenada, aunque podria ser strings 
    pre: Recibe como parametro una lista.
    post: Retorna True en caso de que este ordenada, caso contrario False.
    """
    lista_ordenada = lista[::1] #utilizo "rebanada" de toda la lista para no modificar la original.
    lista_ordenada.sort()
    return lista_ordenada == lista



def main()->None:
    """
    Invoca la funcion ordenada_ascendante y devuelve un mensaje segun lo retornado por la misma.
    pre: No parametros.
    post: Printea segun lo retornado por "ordenada_ascendente"
    """
    if ordenada_ascendente():
        print("La lista esta ordenada.")
    else:
        print("La lista esta desordenada.")

main()
lista = []
assert ordenada_ascendente([1,3,5]) == True
assert ordenada_ascendente([2,2,9]) == True
assert ordenada_ascendente([2,2,1]) == False
assert ordenada_ascendente(["a","c","z"]) == True
assert ordenada_ascendente(["c","a","d"]) == False
#Segun lo visto en la clase 3, con strings mas largos y/o mayusculas es mas dificil 
#de predecir el resultado esperado por el valor de los caracteres 
# puede parecer "ilogico". EJEMPLO:
assert ordenada_ascendente(["a","B","c"]) == False