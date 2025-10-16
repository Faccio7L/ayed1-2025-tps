def buscar_mes(mes:int)->str:
    """
    recibe un mes como entero y lo retorna como un str.
    pre: recibe como parametro un entero.
    post: retorna el mes en forma de string.
    """
    lista_meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    #haria un dict con key numero y value el mes, pero la consigna dice lista.
    try:
        return (lista_meses[mes - 1])#para que coincida con el indice
    except Exception as e:
        return("")

def main()->None:
    """
    Se ingresa un mes y en caso de que sea valido, se invoca la funcion buscar_mes.
    """
    mes = input("Ingrese el numero del mes que desea buscar:")
    try:
        mes = int(mes)
    except Exception as e:
        print(f"Hubo un error por {e}")
    else:
        mes_str = buscar_mes(mes)
        print(f"{mes}.{mes_str}")
main()
