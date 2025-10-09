def calculo(numero_romano:dict,numero:int)->list:
    """
    transforma un numero en un numero romano
    pre: Numero entero del 1 al 4000. diccionario de numeros enteros y romanos.
    post: retorna el numero romano.
    """
    lista = []
    while numero > 0: # resta hasta que llegue a 0
        for entero, romano in numero_romano.items():
            if numero >= entero:
                lista.append(romano)
                numero -= entero
                break #para que vuelva a evaluar, corto el for, vuelvo al while.
    lista = "".join(lista)
    return lista


def main()->None: 
    """
    Se valida que se ingrese un entero del 1 al 4000. Se invoca la funcion de
    calculo de entero a romano.
    """
    valores_romanos = { #diccionario (obtenido de internet) que contempla todos los numeros necesarios!
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV", 
    1: "I"
      }
    numero = int(input("Ingrese un numero del 1 al 4000:"))
    validacion = lambda x: x >= 1 and x <= 4000
    if validacion(numero):
        print(calculo(valores_romanos,numero))
    else:
        print("Valor invalido.")
main()