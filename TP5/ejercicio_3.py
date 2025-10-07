def buscar_mes(mes):
    lista_meses = ["enero","febrero","marzo","abril","mayo","junio","septiembre","octubre","noviembre","diciembre"]
    #haria un dict con key numero y value el mes, pero la consigna dice lista.
    try:
        print(lista_meses[mes - 1])#para que coincida con el indice
    except Exception as e:
        print(f"Hubo un error por {e}")

def main():
    mes = input("Ingrese el numero del mes que desea buscar:")
    try:
        mes = int(mes)
    except Exception as e:
        print(f"Hubo un error por {e}")
    else:
        buscar_mes(mes)
main()
