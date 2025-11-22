def cant_digitos(n:int)->int:
    """
    Cuenta la cantidad de digitos de un numero de manera recursiva.
    pre:recibe un numero entero
    post:retorna la cantidad de digitos.
    """
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + cant_digitos(n/10)



def main()->None:
    """
    Solicita un numero entero e invoca a la funcion contar digitos
    """
    while True:
        try:
            n = int(input("Ingrese un numero entero:"))
        except Exception as e:
            print("Debe ingresar un numero entero.")
        else:
            break
    cantidad = cant_digitos(n)
    print(f"La cantidad de digitos del numero {n} son: {cantidad}")
    
main()