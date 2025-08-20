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
            
             #ya le sume 1 en la linea 3, asi que funciona joya.
        #-----------------------MESES CON 30 DIAS!------------------------------
    if b in [4,6,9,11]:
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
            


def validar_fecha(a:int,b:int,c:int)-> bool:
    """
    se verifica que una fecha sea correcta o no.
    pre: Obtiene como parametros 3 enteros (dia,mes,año)
    post: Retorna True en caso de que sea una fecha existente. Caso contrario, False.
    """
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

def verificar_mayor(a:int,b:int,c:int,a_1:int,b_2:int,c_2:int)-> bool:
    """
    Revisa que fecha entre 2 es mayor.
    pre: Obtiene como parametro 2 fechas con su respectivo dia, mes y año.
    post: Retorna True en caso de que la fecha original ingresada sea mayor, caso contrario False.
    """
    #retorna True si la fecha original es mayor.
    if c > c_2:
        return True
    if c < c_2:
        return False
    else:
        if b > b_2:
            return True
        elif b < b_2:
            return False
        else:
            if a > a_1:
                return True
            elif a < a_1:
                return False
            else:print("Son el mismo dia")
            
        



def dia_que_sigue(a:int, b:int, c:int) -> None:
    """
    almacena en una variable la tupla devuelta por dia_siguiente y printea.
    pre: Obtiene una fecha con su respectivo dia mes y año
    post: printea los datos del dia siguiente.
    """
    tupla_dia_siguiente = dia_siguiente(a, b, c)
    print(f"El dia siguiente corresponde al dia {tupla_dia_siguiente[0]}")
    print(f"del mes {tupla_dia_siguiente[1]} ")
    print(f"del año {tupla_dia_siguiente[2]}")


def sumar_N_dias(a:int,b:int,c:int) -> None:
    """
    Permite sumar X cantidad de dias a la fecha ingresada
    pre: Obtiene como parametro una fecha con su respectivo dia, mes y año.
    post: Printea la diferencia de dias entre una fecha y otra.
    """
    numero = int(input("Ingrese cuantos dias quiere sumar:"))
    for x in range(numero): #esta parte se complico un poco... la funcion dia siguiente esta preparada para pasar de a un num  y la consigna pide que no la modifique, asi que le paso los num de una.
        lista_dia_usuario = dia_siguiente(a,b,c)
        a = lista_dia_usuario[0]
        b = lista_dia_usuario[1]
        c = lista_dia_usuario[2]
    print(f"El dia obtenido es {lista_dia_usuario[0]} del mes {lista_dia_usuario[1]} del año {lista_dia_usuario[2]}")

def diferencia_entre_dos_fechas(a:int,b:int,c:int) -> None:
    """
    calcula la diferencia entre 2 fechas, la segunda se solicitara aqui
    pre: recibe como parametro una fecha (dia,mes,año)
    post: Printea la diferencia de dias entre una fecha y otra.
    """
    print("Ingrese su segunda fecha para evaluar la diferencia entre ambas.")
    a_2 = int(input("Ingrese un dia:"))
    b_2 = int(input("Ingrese un mes:"))
    c_2 = int(input("Ingrese un año:"))
    if validar_fecha(a_2,b_2,c_2): #si la validacion da True
        if verificar_mayor(a,b,c,a_2,b_2,c_2): #es mayor la primera, entonces parto de la fecha 2
            fecha_inicial = (a_2, b_2, c_2) 
            fecha_final = (a, b, c)
        else: #caso contrario al anterior o misma fecha!!
            fecha_inicial = (a, b, c)
            fecha_final = (a_2, b_2, c_2)

        # Si las fechas son iguales, la diferencia es 0.
        if fecha_inicial == fecha_final:
            print("Las fechas son las mismas. La diferencia es de 0 días.")
        else:

            contador_dias = 0
            while fecha_inicial != fecha_final:
                fecha_inicial = dia_siguiente(fecha_inicial[0],fecha_inicial[1],fecha_inicial[2])
                contador_dias += 1
            print(f"La diferencia de dias es de {contador_dias} dias")
           

def main() -> None:
    """
    Se ingresan una fecha y se selecciona una opcion.
    pre: No recibe parametros
    post: invoca al resto de funciones.
    """
    dia = int(input("Ingrese un dia:"))
    mes = int(input("Ingrese un mes:"))
    año = int(input("Ingrese un año"))
    if validar_fecha(dia,mes,año):
        print("Dia validado con exito")
        print("Seleccione una opcion:")
        print("1.Saber el dia siguiente")
        print("2. Sumas N dias a un dia")
        print("3.Calcular la diferencia entre 2 dias.")
        op = input("Ingrese opcion:")
        if op == "1":
            dia_que_sigue(dia,mes,año)
        elif op == "2":
            sumar_N_dias(dia,mes,año)
        elif op == "3":
            diferencia_entre_dos_fechas(dia,mes,año)
        else:
            print("Opcion no valida.")
    else:
        print("Dia invalido.")
main()
