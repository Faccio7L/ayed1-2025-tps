def en_letras(numero:int)->str:
    """
    convierte un entero a un numero en letras.
    pre: recibe como parametro un entero positivo
    post: Retorna el numero en letras.
    """
    diccionario = {
    900: "novecientos",
    800: "ochocientos",
    700: "setecientos",
    600: "seiscientos",
    500: "quinientos",
    400: "cuatrocientos",
    300: "trescientos",
    200: "doscientos",
    100: "cien",
    90: "noventa",
    80: "ochenta",
    70: "setenta",
    60: "sesenta",
    50: "cincuenta",
    40: "cuarenta",
    30: "treinta",
    29: "veintinueve",
    28: "veintiocho",
    27: "veintisiete",
    26: "veintiseis",
    25: "veinticinco",
    24: "veinticuatro",
    23: "veintitres",
    22: "veintidos",
    21: "veintiuno",
    20: "veinte",
    19: "diecinueve",
    18: "dieciocho",
    17: "diecisiete",
    16: "dieciseis",
    15: "quince",
    14: "catorce",
    13: "trece",
    12: "doce",
    11: "once",
    10: "diez",
    9: "nueve",
    8: "ocho",
    7: "siete",
    6: "seis",
    5: "cinco",
    4: "cuatro",
    3: "tres",
    2: "dos",
    1: "uno",
    0: "cero"
}    
    num_separado = list()

    
    while numero > 0: #grupo de a 3 empezando desde atras.
        grupo = numero % 1000
        num_separado.append(grupo)
        numero = numero // 1000
    
    num_separado.reverse() #se da vuelta.
    num_en_letras = []
    for bloque in num_separado: #se iteran los grupos de a 3.
        for key ,value in diccionario.items(): #se itera a su vez el diccionario para ir reemplazando valores.
            if bloque == 0:
                break
            if bloque >= key:
                bloque = bloque - key
                num_en_letras.append(value)
    ##print(num_en_letras)
    #a partir de aca, se agregan miles, cien miles etc
    if len(num_separado) >= 5:
        print("Un billon.")
        return
    
    if len(num_separado) >= 2:
         num_en_letras[1:1] = ["mil"]
         #num_en_letras = " ".join(num_en_letras)

    if len(num_separado) >= 3:
        num_en_letras[2:2] = ["millones"]

    if len(num_separado) >= 4:
        num_en_letras[3:3] = ["mil millones"]

    num_en_letras = " ".join(num_en_letras)
    return num_en_letras

def main()->None:
    """
    Se ingresa un numero entero y se invoca la funcion en_letras para convertir
    ese numero en letras.
    """
    try:
        numero = int(input("Ingrese un numero:"))
    except Exception as e:
        print("Debe ser un numero entero.")
    else:
        print(en_letras(numero))

main()