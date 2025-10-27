try:
    with open("nombres.txt","wt",encoding = "utf-8") as nom:
        while True:
            apellido = input("Ingrese un apellido(0 para salir):")
            if apellido == "0":
                break
            nombre = input("Ingrese un nombre:")
            if not apellido or not nombre:
                break
            else:
                nom.write(f"{apellido},{nombre}\n")
except Exception as e:
    print("hubo un error")


NOMBRES = 'nombres.txt'  
ARMENIA = 'ARMENIA.TXT'
ITALIA = 'ITALIA.TXT'
ESPANIA = 'ESPAÑA.TXT' 

try:
    with open(NOMBRES, 'rt', encoding='utf-8-sig') as nom: #auto-recordatorio para usar -sig
        while True:
            linea = nom.readline() #leer una linea a la vez.
            if not linea: # si no encuentra una linea, termina
                break
            linea = linea.split(",")
            apellido,nombre = linea[0],linea[1]
            if apellido.endswith("ian"):

                with open(ARMENIA,"at", encoding="utf-8") as arm:
                    arm.write(f"{apellido}),{nombre}\n")
            elif apellido.endswith("ini"):
                with open(ITALIA,"at",encoding="utf-8") as ita:
                    ita.write(f"{apellido},{nombre}\n")
            elif apellido.endswith("ez"):
                with open(ESPANIA,"at",encoding="utf-8") as es:
                    es.write(f"{apellido},{nombre}\n")
            else:
                pass
except Exception as e:
    print("Hubo un error.")