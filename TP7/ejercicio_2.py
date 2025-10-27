try:
    while True:
        try:
            palabras_cant = int(input("Ingrese de a cuantas palabras quiere dividir el texto:")) #la consigna no aclara si palabras o caracteres, lo voy a hacer con palabras.
        except Exception as e:
            print("Debe ser un numero entero.")
        else:
            break
    
    with open("ej2.txt","rt",encoding="utf-8") as prueba: #uso un txt random que puse en esta carpeta.
        texto = prueba.read() 
        texto = texto.split() #el texto separado en lista.
    contador = 1
    desde = 0
    while True:
        with open(f"prueba{contador}.txt","wt", encoding="utf-8") as separado:
            try:
                for x in range(desde,desde + palabras_cant):
                    separado.write(texto[x] + " ")
                desde += palabras_cant
            except Exception as e:
                break #creo que solo podria ser un indexerror. ahi hay que dejar de crear.
            else:
                print("Archivo creado con exito.")
                contador +=1

except Exception as e:
    print(f"Hubo un error:{e}")