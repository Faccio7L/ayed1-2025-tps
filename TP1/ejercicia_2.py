def validar_dia(a:int,b:int,c:int) ->bool:
    """
    Revisa que el dia ingresado sea correcto.
    pre: Recibe como parametro un dia,mes y año.
    post:Retorna True si es una fecha valida, False si es invalida.
    """
    if b in [1,3,5,7,8,10,12]:
        return c >= 1 and c <= 31 #devuelve true si se c se encuentra en este umbral
    elif b in [4,6,9,11]:         #sino false
        return c >= 1 and c <= 30
    elif b == 2:
        if a % 4 == 0: #es decir, es biciesto.
            return c >= 1 and c <= 29
        else: 
            return c >= 1 and c <= 28
    else: #entraria aca en caso de un mes inexistente!!!
        return False
    
def main() -> None:
    """ 
    Se ingresa un año, mes y dia y se envian a la funcion de validacion.
    pre: No recibe parametros
    post:Printea si es valida la fecha o no
    """
    año = int(input("Ingree un año:"))
    mes = int(input("Ingrese un mes:"))
    dia = int(input("Ingrese un dia"))
    if validar_dia(año,mes,dia): #omito el == True.
        print("Fecha validada correctamente")
    else:
        print("Fecha no valida.")
main()