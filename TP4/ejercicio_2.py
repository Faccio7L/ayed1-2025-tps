def main(columnas=80):
    centrar = lambda x: " " * 78 + x
    for x in range(columnas):
        print(centrar("texto de relleno"))

main()
