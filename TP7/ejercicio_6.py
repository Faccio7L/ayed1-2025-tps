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

def verificar_mayor(fecha1:tuple[int],fecha2:tuple[int])-> bool:
    """
    Revisa que fecha entre 2 es mayor.
    pre: Obtiene como parametro 2 fechas con su respectivo dia, mes y año.
    post: Retorna True en caso de que la fecha original ingresada sea mayor, caso contrario False.
    """
    #retorna True si la fecha original es menor.
    a, b ,c = fecha1 
    a_2, b_2, c_2 = fecha2
    if c > c_2:
        return False
    if c < c_2:
        return True
    else:
        if b > b_2:
            return False
        elif b < b_2:
            return True
        else:
            if a > a_2:
                return False
            elif a < a_2:
                return True
            else:
                return True
def modificar_txt(flia:tuple,reserva:tuple)->None:
        """
        modifica el .txt
        pre: recibe como parametro dos tuplas con toda la info necesaria para modificar el txt
        """ 
        cantidad, dni, apellido, nombre = flia
        piso, cuarto, dia, mes, diaS, mesS = reserva
        nombre_completo = apellido,nombre 
        ingreso = str(dia) , str(mes), "2025"
        egreso = str(dia), str(mes), "2025"
        #estructura de datos a completar:
        dni_cliente = dni
        nombre_completo = " ".join(nombre_completo) #uno la tupla
        ingreso = " ".join(ingreso)
        egreso = " ".join(egreso)
        ocupantes = cantidad
        #ahora busco PISO Y CUARTO.
        try:
            with open("hotel.txt","rt",encoding="utf-8") as h:
                texto = [linea for linea in h]
        except Exception as e:
            print("Ocurrio un error.")
        cuarto_a_buscar = f"CUARTO {cuarto} PISO {piso}\n"
        indice_a_buscar = texto.index(cuarto_a_buscar)
        texto_a_agregar = [
            f"    DNI: {dni_cliente}\n",
                f"    Nombre: {nombre_completo}\n",
                f"    Ingreso: {ingreso}\n",
                f"    Egreso: {egreso}\n",
                f"    Ocupantes: {ocupantes}\n"
            ]
        texto[indice_a_buscar+1:indice_a_buscar+1] = texto_a_agregar#slice vacio
        try:
            with open("hotel.txt","wt",encoding="utf-8") as h:
               h.writelines(texto) #reescritura.
        except Exception as e:
            print(f"Ocurrio un error:{e}")


            
def inicializar_programa()->None:
    """
    primera vez que corres el programa, crea el .txt
    
    """
    with open("hotel.txt","wt",encoding="utf-8") as h:
            for x in range(1,11):
                for y in range(1,7):
                    h.write(f"CUARTO {y} PISO {x}\n")
    main()
    
    #cuando termina!
    print("Gracias por usar Nuestro super sistema de hotel!")
        



def main()->None:
    """
    Se invoca desde la inicializacion o una vez terminada la carga de datos.

    """
    dni = 0
    try:
        dnis = set()
        while True:
            while True:
                try:
                    dni = int(input("Ingrese un dni:"))
                    
                        
                except Exception as e:
                    print("Debe ser un numero entero.")
                else:
                    if dni == -1: #si cae aca, termina

                        return
                    elif dni in dnis:
                        print("Dni ya registrado.")
                    else:
                        dnis.add(dni)
                        apellido = input("Ingrese su apellido:")
                        nombre = input("Ingrese su nombre:")
                        while True:
                            print("-DATOS DE ENTRADA-")
                            dia = int(input("Ingrese un dia:"))
                            mes = int(input("Ingrese un mes:"))
                            if validar_fecha(dia,mes,2025):
                                print("-DATOS DE SALIDA-")
                                diaS = int(input("Ingrese un dia:"))
                                mesS = int(input("Ingrese un mes:"))
                                if validar_fecha(dia,mes,2025):
                                    fecha1 = (dia,mes,2025)
                                    fecha2 = (diaS,mesS,2025)
                                    if validar_fecha(diaS,mesS,2025):
                                        if verificar_mayor(fecha1,fecha2):
                                            print("Datos ingresados correctamente.")
                                            while True:
                                                try:
                                                    cantidad = int(input("Ingrese la cantidad de ocupantes(10 maximo):"))
                                                except Exception as e:
                                                    print("Debe ser un numero entero.")
                                                else:
                                                    if cantidad >=1 and cantidad <= 10: #si se ingresa bien.
                                                        break
                                                    else:
                                                        print("cantidad invalida.")
                                            #si llega hasta aca, se ingreso todo ok
                                            while True:
                                                        try:
                                                            piso =int(input("Ingrese un piso para hacer su reserva del 1 al 10:"))
                                                            cuarto = int(input("Ingrese un cuarto del 1 al 6:"))
                                                            if piso > 10 or piso < 1 or cuarto > 6 or cuarto < 1:
                                                                print("Datos invalidos.")
                                                                input("Enter para continuar...")
                                                            else:
                                                                break #ingreso bien los datos!
                                                        except Exception as e:
                                                            print("Hubo un error.")
        #--------------------------HASTA ACA BIEN, INVOCAMOS FUNCION PARA AHORA SI MODIFICAR LOS DATOS-------------
                                            info_flia = (cantidad,dni,apellido,nombre)
                                            info_reserva = (piso,cuarto,dia,mes,diaS,mesS)
                                            modificar_txt(info_flia,info_reserva) #para manejar pocos parametros
                                            print("reserva exitosa.")
                                            break
                                            

                                    else:
                                        print("Dia de entrada mayor al de salida.")

                            else:
                                print("Dia invalido.")
                                
    except Exception as e:
        print(f"ocurrio un error: {e}")
inicializar_programa()