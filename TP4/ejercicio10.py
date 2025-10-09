def nueva_cadena(cadena_main:str,a_eliminar:str)->str:
    """
    Se reemplazan palabras de una lista que esten en otra lista por la palabra "hola"
    pre:recibe 2 cadenas.
    post: Retorna la nueva lista y el contador
    """
    lista_main = cadena_main.split()
    contador = lista_main.count("hola")
    lista_a_eliminar = a_eliminar.split()
    lista_nueva = ["hola" if palabra in lista_a_eliminar else palabra for palabra in lista_main]
    contador = lista_nueva.count("hola") - contador #se cuentan la cantidad de apariciones de hola al principio y al final, asi veo cuantas se adiciono!
    nueva_lista = " ".join(lista_nueva)
    return nueva_lista,contador

def main()->None:
    """
    Se ingresa una cadena principal y una cadena a eliminar.
    """
    cadena_main = input("Ingrese una frase:")
    a_eliminar = input("Ingrese las palabras que quiere eliminar:")
    print(nueva_cadena(cadena_main,a_eliminar))
main()