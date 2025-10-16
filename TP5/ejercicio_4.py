def main()->None:
    """
    Se printean muchos numeros consecutivos hasta que haya un keyerror.

    """
    try:
        for x in range(1,1000000000): #puse un num mas grande por que cortaba rapidisimo.
            print(x)
            
    except KeyboardInterrupt:
        input("Ingrese una tecla para confirmar accion.")
main()
        
    