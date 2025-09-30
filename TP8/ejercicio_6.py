def eliminacion_de_palabras(frase,palabras_a_eliminar):
    for palabra in palabras_a_eliminar:
        while palabra in frase:
            frase.remove(palabra)
    
    return frase

         


def main():
    a_eliminar = set()
    frase = input("Ingrese una frase:")
   
    frase_separada = frase.split() #hago una lista de palabras.
    while True:
        palabra_a_eliminar = input("Ingrese una palabra a eliminar(0 para salir):")
        if palabra_a_eliminar == "0":
            break
        else:
         a_eliminar.add(palabra_a_eliminar)
    frase = eliminacion_de_palabras(frase_separada,a_eliminar)
    frase = sorted(frase)
    print(" ".join(frase))
main()