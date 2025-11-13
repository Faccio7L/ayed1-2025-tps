def main()->None:
    """
    Se crea un archivo de alturas con el deporte y la altura de cada deportista
    ese dato se utiliza para calcular promedios por disciplina.
    """
    try:
        with open("alturas.txt","wt",encoding="utf-8") as alt:
            while True:
                contador = 1
                deporte = input("ingrese el nombre del deporte:(enter para salir):").capitalize()
                total_alt = 0
                if not deporte:
                    break
                alt.write(f"{deporte}\n")
                while True:
                    #total_alt = 0
                    try:
                        altura = input(f"Ingrese la altura del atleta numero {contador}(si no existe presione enter):")
                        if not altura:
                            promedio(total_alt,contador-1, deporte)
                            break
                        altura = float(altura)
                    except Exception as e:
                        print("Debe ser un numero entre 1.4 y 2.5")
                    else:
                        if altura >= 1.4 and altura <= 2.5:
                            print("Altura registada correctamente.")
                            alt.write(f"{altura},deportista {contador}\n")
                            contador += 1
                            total_alt += altura
                        else:
                            print("Debe ser un numero entre 1.4 y 2.5")
    except Exception as e:
        print(f"Hubo un error:{e}")

def promedio(total:float,contador:int,deporte:str)->None:
    """
    Calcula el promedio de altura de un deporte y lo muestra en un archivo con un formato 
    amigable.
    """
    if contador > 0:
        promedio = total / contador 
    else:
        promedio = "no info"
    try:
        with open("promedios.txt","at",encoding="utf-8") as prom:
            prom.write(f"{deporte},{promedio}\n")
    except Exception as e:
            print(f"Ocurrio un error:{e}")

main()