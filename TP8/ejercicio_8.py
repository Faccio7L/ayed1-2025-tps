def main()->None:
    """
    Genera un diccionario con keys consecutivas (del 1 al 20) 
    y las claves son los cuadrados de las keys
    """
    diccionario = {
    }
    for x in range(1,21):
        diccionario[x] = x**2
    print(diccionario)
main()