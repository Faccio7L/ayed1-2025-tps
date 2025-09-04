#No se me ocurrio como hacerlo
def normalizar_lista(lista:list[int] = [3,2,6,3,4]) -> list[float]:
    """
    toma una lista y utiliza la formula de normalizacion de datos.
    pre: Recibe como parametro una lista de enteros.
    post: Retorna una lista de flotantes, el ultimo elemento es la suma de los mismos.
    """
    
    minimo = min(lista)
    maximo = max(lista)
    for i,x in enumerate(lista):
        normalizar_elemento = (x - minimo) / (maximo - minimo)
        lista[i] = normalizar_elemento #reemplazo en el sub i (primero 0, despues 1) el valor normalizado.
    return lista


def main()-> None:
    """
    Crea una lista vacia (podria ser completada) e invoca a la funciion normalizar_lista
    pre: No paramatros
    post: Printea el resultado de la normalizacion de la lista
    """
    lista = [] # podria ser completada, voy a usar una de manera predeterminada.
    print(f"La lista normalizada es: {normalizar_lista()}")


main()
#el max es 1!!! (o muy proximo a uno, ya que a veces se redondean decimales.)
resultado =  max(normalizar_lista([9,2,9,3]) )
assert resultado > 0.99 and resultado < 1.01
resultado =  max(normalizar_lista([13,11,1,28]))
assert resultado > 0.99 and resultado < 1.01
resultado = max(normalizar_lista([4,2,3,1,2])) == 1
assert resultado > 0.99 and resultado < 1.01