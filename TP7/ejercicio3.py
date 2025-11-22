def suma(num)->int:
    """
    suma un numero desde el 1 hasta el mismo.
    pre:recibe un entero
    post:retorna su suma.
    """
    if num == 1:
        return 1
    else:
        return num + suma(num-1)


def main()->None:
    """
    solicita un numero del 1 al 1000 e invoca a una funcion para sumar desde el 1
    hasta ese numero
    """
    while True:
        try:
            num = int(input("Ingrese un numero entre 1 y 999:")) #para que no exceda la pila
            if num >= 1 and num <= 999:
                break
            else:
                print("Rango invalido")
        except Exception as e:
            print("Debe ser entero.")
    suma_ = suma(num)
    print(f"La suma desde el 1 hasta el {num} es:{suma_}")
main()