def oblongo(num:int) -> bool:
    """
    determina si un num es oblongo.
    pre: Recibe un entero.
    post: retorna True en caso de ser oblongo. Caso contrario retorna False.
    """
    if num < 1:
        return False
    for x in range(1, num):
       oblongo =  x * (x + 1) 
       if num == oblongo:
           return True
    return False

def triangular(num:int) -> bool:
    """
    define si un numero es triangular.
    pre: recibe un entero
    post: retorna True en caso de ser triangular. Caso contrario retorna False.
    """
    if num < 1:
        return False
    for x in range(1, num):   #recorre desde el 1 hasta num ingresado
        suma = 0
        for i in range(1, x+1): #suma hasta el valor de x, primero suma 1, despues 1 y 2...etc y compara
            suma += i
        if suma == num:
            return True
    return False


def main() -> None:
    """
    Se ingresa un numero entero, luego invoca la funcion oblongo y triangular
    pre:No recibe parametros.
    post: Printea si es oblongo o no, si es triangular o no.
    """
    num = int(input("Ingrese un numero, se notificara si es oblongo y/o triangular:"))
    if oblongo(num):
        print("El numero es oblongo.")
    else:
        print("No es oblongo.")
    if triangular(num):
        print("El numero es Triangular")
    else:
        print("El numero no es Triangular.")

    
main()