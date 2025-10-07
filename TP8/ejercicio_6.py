def main():
    set_= set()
    frase = input("Ingrese una frase:")
   
    frase_separada = frase.split() #hago una lista de palabras.
    for palabra in frase_separada:
        set_.add(palabra)
    set_unido = " ".join(set_)
    print(set_unido)

main()