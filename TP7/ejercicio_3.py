try:
    with open("alturas.txt","wt",encoding="utf-8") as alt:
        while True:
            contador = 1
            deporte = input("ingrese el nombre del deporte:(enter para salir):").capitalize()
            if not deporte:
                break
            alt.write(f"{deporte}\n")
            while True:
                try:
                    altura = input(f"Ingrese la altura del atleta numero {contador}(si no existe presione enter):")
                    if not altura:
                        break
                    altura = float(altura)
                except Exception as e:
                    print("Debe ser un numero entre 1.4 y 2.5")
                else:
                    if altura >= 1.4 and altura <= 2.5:
                        print("Altura registada correctamente.")
                        alt.write(f"{altura},deportista {contador}\n")
                        contador += 1
                    else:
                        print("Debe ser un numero entre 1.4 y 2.5")
except Exception as e:
    print("Hubo un error.")