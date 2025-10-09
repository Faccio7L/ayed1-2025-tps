def filtrar_por_comprension(frase:str,n:int)->list:
    """
    Se filtra a partir de los caracteres deseados con listas por comprension.
    pre: Recibe la frase y la cantidad de caracteres que se desean filtrar.
    """
    frase_separada = frase.split() #lista por palabras
    filtrar = [palabra for palabra in frase_separada if len(palabra) >= n]
    return filtrar

def filtrar_con_filter(frase:str,n:int)->None:
    """
    Se filtra a partir de los caracteres deseados con la funcion filter y muestra
    el resultado en pantalla.
    pre: Recibe la frase y la cantidad de caracteres que se desean filtrar.

    """
    frase = frase.split()
    #filtrar = (lambda frase,n: len(frase) >= n)
    
    
    print(list(filter(lambda frase: len(frase) >= n ,frase)))
    

def main()->None:
    """
    Se ingresa una frase y los caracteres minimos seran filtrados. Se invocan las funciones
    para filtrar
    """
    frase = input("Ingrese una frase:")
    n = int(input("Desee a partir de cuantos caracteres desea filtrar:"))
    print(filtrar_por_comprension(frase,n))
    print(filtrar_con_filter(frase,n))
main()