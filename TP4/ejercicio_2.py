def main(columnas=80)->None:
    """
    Centra texto.
    pre: Columnas a printear.
    """
    centrar = lambda x: " " * 78 + x
    for x in range(columnas):
        print(centrar("texto de relleno"))

main()
