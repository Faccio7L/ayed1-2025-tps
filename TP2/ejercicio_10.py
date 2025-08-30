import random as rn

def main()->None:
    """
    Genera una lista vacia, la llena y despues filtra los impares
    pre: No parametros.
    post: Muestra en pantalla la lista filtrada.
    """
    lista = []
    for x in range(50):
        lista.append(rn.randint(1,100))
    print(list(filter(lambda x:  x % 2 == 1, lista)))
    print(lista) #lo hice en este orden para ver si el filter altera la lista original, conclusion: No la altera.
main()
    