def validar_fecha(fecha)-> bool:
    """
    se verifica que una fecha sea correcta o no.
    pre: Obtiene como parametros 3 enteros (dia,mes,año)
    post: Retorna True en caso de que sea una fecha existente. Caso contrario, False.
    """
    a,b,c = fecha
    if b in [1,3,5,7,8,10,12]:
        return a >= 1 and a <= 31 and 1 <= c < 100
    elif b in [4,6,9,11]:         
        return a >= 1 and a <= 30 and 1 <= c < 100
    elif b == 2:
        if c % 4 == 0: 
            return a >= 1 and a <= 29 and 1 <= c < 100
        else: 
            return a >= 1 and a <= 28 and 1 <= c < 100
    else: 
        return False
    
def pasar_fecha_a_str(fecha:tuple,corte:int = 30)->None:
    """
    Muestra en pantalla un año en formato extendido
    pre: Recibe como parametro los ultimos dos dias de un año y un mes en LETRAS.
    post: No.
    """
    meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}

    dia,mes,año = fecha
    if año > corte:
        print(f"{dia} de {meses[mes]} del año 19{año}.")
    else:
        print(f"{dia} de {meses[mes]} del año 20{año}")


def main()->None:
    """
    se ingresa una fecha y se invocan otras funciones.
    pre: no.
    post: no.
    """
    while True:
        dia = int(input("Ingrese un dia."))
        mes = int(input("Ingrese un mes"))
        año = int(input("Ingrese un año(solo dos cifras):"))
        fecha = (dia,mes,año)
        if validar_fecha(fecha):
            print("Fecha validada.")
            pasar_fecha_a_str(fecha)
        else:
            print("Fecha incorrecta.")


main()