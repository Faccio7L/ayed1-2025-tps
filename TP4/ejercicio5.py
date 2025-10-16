def filtrar_por_ciclos_normales(frase:str,n:int)->list:
    """
    Se filtra mediante un for palabras mas cortas que N.
    pre: Recibe la frase y la cantidad de caracteres que se desean filtrar.
    post: retorna una lista por comprension con los elementos filtrados.
    """
    lista = []
    frase = frase.split()
    for palabra in frase:
        if len(palabra) >= n:
            lista.append(palabra)
    lista = " ".join(lista)
    return lista


def filtrar_por_comprension(frase:str,n:int)->list:
    """
    Se filtra a partir de los caracteres deseados con listas por comprension.
    pre: Recibe la frase y la cantidad de caracteres que se desean filtrar.
    post: retorna una lista por comprension con los elementos filtrados.
    """
    frase_separada = frase.split() #lista por palabras
    filtrar = [palabra for palabra in frase_separada if len(palabra) >= n]
    filtrar = " ".join(filtrar)
    return filtrar

def filtrar_con_filter(frase:str,n:int)->list:
    """
    Se filtra a partir de los caracteres deseados con la funcion filter y muestra
    el resultado en pantalla.
    pre: Recibe la frase y la cantidad de caracteres que se desean filtrar.
    post: retorna una lista por comprension con los elementos filtrados.
    """
    frase = frase.split()
    #filtrar = (lambda frase,n: len(frase) >= n)
    
    
    frase = list(filter(lambda frase: len(frase) >= n ,frase))
    frase = " ".join(frase)
    return frase
    

def main()->None:
    """
    Se ingresa una frase y los caracteres minimos seran filtrados. Se invocan las funciones
    para filtrar
    """
    frase = input("Ingrese una frase:")
    n = int(input("Desee a partir de cuantos caracteres desea filtrar:"))
    print(filtrar_por_ciclos_normales(frase,n))
    print(filtrar_por_comprension(frase,n))
    print(filtrar_con_filter(frase,n))
main()