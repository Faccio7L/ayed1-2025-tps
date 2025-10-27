ARCHIVO_COPIADO = "vacio.txt"

try:
    with open("ejercicio_1.py","rt",encoding= "utf-8")as prueba: #paso el ejercicio 1 para tener algo comentado
        with open(ARCHIVO_COPIADO,"wt",encoding= "utf-8")as copia:
            #linea = prueba.readline()
            for linea in prueba:
                copia.write(linea)
except Exception as e:  
    print("Hubo un error.")



try:
    with open(ARCHIVO_COPIADO,"r+t",encoding= "utf-8") as arch:
        with open("sin_comentarios.txt","w+t",encoding= "utf-8") as WOComentarios:
            for linea in arch:
                encontrado = False  
                palabras = linea.split() #separo en palabras.
                palabras_a_dejar = []
                for palabra in palabras:
                    if "#" in palabra :
                        encontrado = True #flag para eliminar desde el # EN ADELANTE.
                    if not encontrado:
                        palabras_a_dejar.append(palabra)
                nueva_linea = " ".join(palabras_a_dejar)
                WOComentarios.write(f"{nueva_linea}\n")
except Exception as e:
    print("Hubo un error.")
                
        

