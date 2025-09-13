def main(str:str = "aba"):
    lista = list(str)
    lista_copia = lista.copy()
    lista_copia.reverse()
    return lista_copia == lista
print(main())

assert main("hola") == False
assert main("aaa") == True
assert main("") == True
assert main("123") == False
assert main("131") == True