def validar_socio(socio:int)-> bool:
    """
    verifica que el numero de socio sea valido.
    pre: Recibe un entero(num de socio)
    post: Retorna True en caso de existir, caso contrario False.
    """
    return 10000 < socio < 99999 #mucho mejor escribirlo asi que socio 2 veces!

def contar_ingresos(socio:int,lista_socios:list[int],cant_visitas:list[int])->None:
    """
    Cuenta la cantidad de ingresos, si es la primera vez que viene lo appendea y le
    pone una visita, si ya vino solo suma una visita.
    post: No retorna nada, pero si modifica y agrega datos a las listas.
    """
    if socio in lista_socios:
        i = lista_socios.index(socio)
        cant_visitas[i] += 1
    else:
        lista_socios.append(socio)
        cant_visitas.append(1)

def socio_de_baja(socio:int,lista_socio:list[int],lista_visitas:list[int])->None:
    """
    Verifica que el socio exista y lo da de baja.
    pre: recibe como parametro el socio a eliminar, su elemento de la lista de socios y sus visitas.
    post: Modifica la listas y elimina datos.
    """
    if socio in lista_socio:
        i = lista_socio.index(socio)
        lista_socio.remove(socio)
        lista_visitas.pop(i) #aca uso pop por que elimino el indice i, con remove elimino EL VALOR del indice.          
    

    

def main()->None:
    """
    Se generan las listas vacias de socios y visitas, se cargan invocando al resto
    de funciones!
    pre: No parametros
    post: No retorna nada, printea las listas cargadas.
    """
    lista_socios = []
    lista_visitas = []

    while True:
        socio = int(input("Ingrese su numero de socio:"))
        if socio == 0:
            break
        else:
            if validar_socio(socio):
                contar_ingresos(socio,lista_socios,lista_visitas)
            else:
                print("Numero de socio invalido.")
    
    for s, v in zip(lista_socios,lista_visitas):
        print(f"La cantidad de veces que ingreso el socio {s} es de {v} veces")
    
    dar_de_baja = int(input("Ingrese un numero de socio para dar de baja:"))
    socio_de_baja(dar_de_baja,lista_socios,lista_visitas)
    for s, v in zip(lista_socios,lista_visitas): #printeo las listas actualizadas solo para demostrar que funciona mi funcion.
        print(f"La cantidad de veces que ingreso el socio {s} es de {v} veces")

            
main()