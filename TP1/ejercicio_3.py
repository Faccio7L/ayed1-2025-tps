def cant_viajes(viajes):
    if viajes >= 1 and viajes <= 20:
        return viajes * 1000 #utilizo $1000 como precio standard ya que la consigna no especifica
    elif viajes >= 21 and viajes <= 30:
        return viajes * 800
    elif viajes >= 31 and viajes <= 40:
        return viajes * 700
    elif viajes > 40:
        return viajes * 600
    else:
        print("Ingrese un numero de viajes valido.")
    

def main():
    cantidad_de_viajes = int(input("Ingrese la cantidad de viajes del mes:"))
    if cant_viajes(cantidad_de_viajes) != None: #si entra en el Else retorna None
        print(f"El monto a abonar es: ${cant_viajes(cantidad_de_viajes)}")

main()