def nueva_cadena(cadena_main:str,a_eliminar:str)->str:
    lista_main = cadena_main.split()
    lista_a_eliminar = a_eliminar.split()
    lista_nueva = ["juan" if palabra in lista_a_eliminar else palabra for palabra in lista_main]

    nueva_lista = " ".join(lista_nueva)
    return nueva_lista

def main():
    cadena_main = input("Ingrese una frase:")
    a_eliminar = input("Ingrese las palabras que quiere eliminar:")
    print(nueva_cadena(cadena_main,a_eliminar))
main()