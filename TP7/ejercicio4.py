def multiplicacion_recursiva(n1:int,n2:int)->int:
    """
    Multiplica dos numeros utilizando suma recursiva
    pre: Recibe 2 enteros.
    """
    if n2 == 0:
        return 0
    else:
        return n1 + multiplicacion_recursiva(n1,n2-1)


def main()->None:
    """
    Solicita dos numeros enteros e invoca a la funcion multiplicacion_recursiva.
    """
    while True:
        try:
            num1 = int(input("Ingrese un numero entero:"))
            num2 = int(input("Ingrese otro numero entero:"))
        except Exception as e:
            print("Deben ser dos numeros enteros")
        else:
            break
    print(multiplicacion_recursiva(num1,num2))
main()