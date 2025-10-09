import random as rn
def main()->None:
    """
    Se generan dos fichitas de domino y se evalua si pueden unirse.
    pre: no.
    post:no.
    """
    flag = False
    fichas = []
    while len(fichas) < 2: 
        ficha = set()
        while len(ficha) < 2:
            cuadradito = rn.randint(1,6)
            ficha.add(cuadradito)
        fichas.append(ficha)
    print(fichas)
    for numero in fichas[0]: #itero el primer set de la lista(sub0,2 iteraciones)
        if numero in fichas[1]: #si el numero se encuentra en el segundo set.
            print("Se pueden unir!")
            flag = True
    if flag == False:
        print("NO se pueden unir.")
main()
    
