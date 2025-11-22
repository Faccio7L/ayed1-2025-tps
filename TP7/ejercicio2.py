def pasar_a_decimal(n:int,contador = 0)->int:
    """
    recibe un numero binario y lo "castea" a entero.
    pre:numero entero
    post:retorna un numero entero que (el binario en sistema decimal)
    """
    if n == 0:
        return 0
    else:
        ultimo_num = n %10
        valor_parcial = ultimo_num * 2 ** contador  #el ultimo numero multiplicado por 2 elevado a su posicion.
        
        return valor_parcial + pasar_a_decimal(n//10,contador +1)


def main()->None:
        """
        Solicita un numero binario e invoca a la funcion pasar_a_decimal para castearlo
        """
        num = input("Ingrese un numero compuesto por 1 y 0:")#para que no exceda la pila
        invalido = False
        for elemento in num:
            if elemento not in ("0","1"):
                invalido = True
        if invalido:
            print("Numero invalido.")
        else:
            num = int(num)
            print(pasar_a_decimal(num))
        
main()