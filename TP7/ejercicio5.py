def resto(dividendo:int,divisor:int): #voy reduciendo el dividendo
    """
    Obtiene el resto de una division.
    pre: dos enteros, un dividendo y un divisor.
    """
    if dividendo < divisor:
        return dividendo
    else:
        return resto(dividendo - divisor,divisor)

def main()->None:
    """
    Solicita dos numeros enteros e invoca a resto.
    """
    while True:
        try:
            num1 = int(input("Ingrese un numero entero:"))
            num2 = int(input("Ingrese otro numero entero:"))
        except Exception as e:
            print("Deben ser dos numeros enteros.")
        else:
            break
    print(resto(num1,num2))
main()