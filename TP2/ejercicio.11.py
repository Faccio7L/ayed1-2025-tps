def cantidad_de_consultas(lista_afiliados:list[int], lista_cantidades:list[int], afiliado:int) ->None:
    """
    Se ingresan nuevos afiliados en la lista de afiliados y se cuentan sus consiltas y emergencias
    pre: Recibe como parametro las listas de afiliados, el numero de afiliados y la lista de CANTIDADES.
    post: No retorna nada, solo actualiza la listas.
    """
    if afiliado in lista_afiliados: #si esta, no duplico. pero si busco indice
        i = lista_afiliados.index(afiliado)
        lista_cantidades[i] += 1 #sumo 1 en vez de appendear.
    else: #no busco indice por que no esta, appendeo 1 en cantidad
        lista_afiliados.append(afiliado) 
        lista_cantidades.append(1)

    

def validar_numero_de_afiliado(num_afiliado:int) -> bool:
    """
    Retorna True en caso de que el numero de afiliado sea valido.
    pre: recibe un entero, numero de afiliado.
    post: retorna True si es valido, caso contrario retorna False.
    """
    return num_afiliado > 999 and num_afiliado < 10000


def eleccion_urgencia_o_turno(opcion:int) -> None:
    """
    verifica si la opcion ingresa es correcta.
    pre:toma como parametro un entero.
    post: Si es 0 o 1(es decir, opcion valida) retorna True.
    """
    return opcion in [0,1]
def main()->None:
    """
    Genera 4 listas vacias. los afiliados que tuvieron turnos, afiliados que tuvieron
    urgencias, la cantidad de turnos y la cantidad de urgencias de los mismos. Invoca
    al resto de funciones.
    pre: no parametros
    post: Las listas se completan con datos, muestra por pantalla las listas mediante
    el zip.
    """
    lista_turnos = []
    lista_urgencias = []
    lista_cantidad_turnos = []
    lista_cantidad_urgencias = []
    while True:
        num_afiliado = int(input("Ingrese su numero de afiliado:"))
        if num_afiliado == -1:
              break
        if validar_numero_de_afiliado(num_afiliado):
            urgencia_o_turno = int(input("Ingrese 1 si usted tiene turno, ingrese 0 si es una urgencia."))
            if eleccion_urgencia_o_turno(urgencia_o_turno):
                if urgencia_o_turno == 1: #si op = 1. Envio lista_turnos para actualizar esta.
                    cantidad_de_consultas(lista_turnos, lista_cantidad_turnos, num_afiliado)
                else: #si la opcion es 0, envio lista_urgencia para lista_afiliados.
                    cantidad_de_consultas(lista_urgencias, lista_cantidad_urgencias, num_afiliado)
            else:
                print("Ingrese una opcion valida.")

        else:
         print("Ingrese un numero de afiliado valido.")
    
    for l, c in zip(lista_urgencias,lista_cantidad_urgencias):
        print(f"el paciente {l} se atendio por urgencias {c} vez/veces")
    for l, c in zip(lista_turnos,lista_cantidad_turnos):
        print(f"El paciente {l} se atendio con turno {c} vez/veces")
   
main()