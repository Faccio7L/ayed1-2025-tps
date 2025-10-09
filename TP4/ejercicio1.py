def main(str:str = "aba"):
    """
    Verifica si una lista es capicua.
    """
    lista = list(str)
    lista_copia = lista[::]
    lista_copia.reverse()
    return lista_copia == lista
print(main())

assert main("hola") == False
assert main("aaa") == True
assert main("") == True
assert main("123") == False
assert main("131") == True

