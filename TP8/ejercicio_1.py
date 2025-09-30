def validar_fecha(fecha)-> bool:
    """
    se verifica que una fecha sea correcta o no.
    pre: Obtiene como parametros 3 enteros (dia,mes,año)
    post: Retorna True en caso de que sea una fecha existente. Caso contrario, False.
    """
    a,b,c = fecha
    if b in [1,3,5,7,8,10,12]:
        return a >= 1 and a <= 31 
    elif b in [4,6,9,11]:         
        return a >= 1 and a <= 30
    elif b == 2:
        if c % 4 == 0: 
            return a >= 1 and a <= 29
        else: 
            return a >= 1 and a <= 28
    else: 
        return False
def validar_hora(horario):
    hora, minuto = horario
    return 0 <= hora < 24 and 0 <= minuto < 60

#def ver_primer_horario(hor,hor2):
    #return hor > hor2 #retorna True si el horario 1 fue el dia ANTERIOR  a hor 2.


def calcular_diferencia_de_horario(horarios):
    horario1, horario2, = horarios
    contador = 0 #contador de minutos.
    hora, minuto = horario1
    #hora2,minuto2 = horario2
    #recordatorio del funcionamiento de cada tupla... horarios tiene 2 elementos pero a su vez, cada horario tiene 2 elementos adentro! hora y minutos.
    #en conclusion, una tupla con 2 elementos que son tuplas con 2 elementos cada una!
    while horario1 != horario2:
        minuto += 1
        if minuto == 60:
            hora += 1
            minuto = 0
        if hora == 24:
            hora = 0
            minuto = 0
        contador += 1
        horario1 = hora, minuto
    horas = contador // 60
    minutos = contador % 60
    return horas, minutos

    #para que sea mas legible y no leer un "la diferencia es de 302 minutos."
def validar_fecha(fecha)-> bool:
    """
    se verifica que una fecha sea correcta o no.
    pre: Obtiene como parametros 3 enteros (dia,mes,año)
    post: Retorna True en caso de que sea una fecha existente. Caso contrario, False.
    """
    a,b,c = fecha
    if b in [1,3,5,7,8,10,12]:
        return a >= 1 and a <= 31 
    elif b in [4,6,9,11]:         
        return a >= 1 and a <= 30
    elif b == 2:
        if c % 4 == 0: 
            return a >= 1 and a <= 29
        else: 
            return a >= 1 and a <= 28
    else: 
        return False
    
def validar_hora(horario):
    hora, minuto = horario
    return 0 <= hora < 24 and 0 <= minuto < 60

def ver_primer_horario(hor,hor2):
    return hor > hor2 #retorna True si el horario 1 fue el dia ANTERIOR  a hor 2.

def dia_siguiente(a:int,b:int,c:int) ->int:
    """
    notifica cual es la fecha siguiente a la ingresada como parametro.
    pre: recibe como parametro 3 enteros: un dia, un mes, un año.
    post: retorna a, b y c segun el valor de los mismos del dia siguiente al ingresado.
    """
    a += 1
    if b in [1,3,5,7,8,10,12]: #meses con 31 dias.
        if a > 31:
            a = 1
            b += 1

             #ya le sume 1 en la linea 3, asi que funciona.
        #-----------------------MESES CON 30 DIAS!------------------------------
    elif b in [4,6,9,11]:
        if a > 30:
            a = 1
            b += 1
        #----------------------Febrero!!!!-------------------------------------
    else: #ya hay una validacion previa, asi que este else cubre la unica posibilidad.
        if c % 4 == 0:
            if a > 29:
                a = 1 
                b += 1    
        else:
            if a > 28:
                a = 1
                b += 1
    if b > 12:
        b = 1
        c += 1
    return a,b,c
def sumar_N_dias(fecha) -> None:
    """
    Permite sumar X cantidad de dias a la fecha ingresada
    pre: Obtiene como parametro una fecha con su respectivo dia, mes y año.
    post: Printea la diferencia de dias entre una fecha y otra.
    """
    a,b,c = fecha
    numero = int(input("Ingrese cuantos dias quiere sumar:"))
    for x in range(numero): 
        a, b, c = dia_siguiente(a,b,c)
    print(f"El dia obtenido es {a} del mes {b} del año {c}")
    

def main():
    while True:
        año = int(input("Ingrese un año:"))
        mes = int(input("Ingrese un mes:"))
        dia = int(input("Ingrese un dia:"))
        fecha = (dia,mes,año)

        if validar_fecha(fecha):
            print("Dia validado con exito!!!")
            sumar_N_dias(fecha)
            
            hora = int(input("Ingrese un horario:"))
            minuto = int(input("Ingrese el minuto del horario:"))
            horario = (hora,minuto)
            if validar_hora(horario):
                print("Horario validado con exito!!!")
                hora_2 = int(input("Ingrese un horario:"))
                minuto_2 = int(input("Ingrese el minuto del horario:"))
                horario_2 = (hora_2,minuto_2)
                if validar_hora(horario_2):
                    # if ver_primer_horario(horario,horario_2):
                    diferencia = (horario,horario_2)
                        #else:
                            #diferencia = (horario,horario_2)
                    horas,minutos = calcular_diferencia_de_horario(diferencia)
                    print(f"La diferencia horaria es de {horas} horas y {minutos} minutos.")
main()
            

