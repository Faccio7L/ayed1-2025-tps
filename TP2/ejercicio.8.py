def main()->None:
    """
    Genera una lista por comprension de impares del 100 al 200.
    pre: no recibe parametros.
    """
    lista_por_comprension = [x for x  in range(100,200) if x % 2 == 1]
    print(lista_por_comprension)
main()