def diadelasemana(dia:int, mes:int, año:int)-> int:
    """
    Informa en que dia especifico de la semana "cae" un dia.
    pre: Recibe como parametro un dia, un mes y un año especifico
    post: retorna un numero del 0 al 6 que representan cada dia de la semana.
    """
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def validar_fecha(mes:int) -> bool:
    """
    Valida que una fecha sea correcta
    pre: Recibe como parametro un entero que representa un mes.
    post: Retorna True en caso de ser un mes valido, caso contrario False.
    """
    return mes >= 1 and mes <= 12

def cantidad_dias(mes:int,año:int)-> int:
    """
    calcula la cantidad de dias que hay en un mes y año especifico(a excepcion que sea febrero, el año no es relevante)
    pre: recibe como parametro dos enteros, un mes y un año
    post: retorna la cantidad de dias que hay en un mes
    """
    if mes in [1,3,5,7,8,10,12]:
        return 31
    elif mes in [4,6,9,11]:
        return 30
    else: 
        if año % 4 == 0:
            return 29
        else:
            return 28
    
def numero_a_dia(num:int)-> str:
    """ 
     convierte un numero en un string que representa un dia de la semana
     pre: recibe como parametro un numero del 0 al 6, representan los 7 dias de la semana
    post: Retorna un string, el dia de semana de manera explicita
    """

    dia_en_str = ["domingo","lunes","martes","niercoles", "jueves", "viernes","sabado"]
    return dia_en_str[num]

def main() -> None:
    """
    se ingresa un mes y un año, se invocan otras funciones para finalmente poder informar el calendario completo de un mes.
    pre: no recibe parametros.
    post:printea el mes.
    """
    lista = []
    mes = int(input("Ingrese un mes:"))
    anio = int(input("Ingrese un año:"))
    if validar_fecha(mes):
        lista_numerica = [x for x in range(1,cantidad_dias(mes,anio) + 1)]
        for x in range(1, cantidad_dias(mes,anio) + 1):    
            num = (diadelasemana(x,mes,anio)) #x (osea dia) vale uno mas con cada iteracion.
            lista.append(numero_a_dia(num))
        for num, dia in zip(lista_numerica,lista):
            print(f"{num,dia}")
    else:
        print("Fecha invalida.")

main()