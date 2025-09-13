def ordenar_por_len(cadena):
    lista = cadena.split()
    lista.sort(key=len) #ordeno por el largo de las palabras!
    lista_a_string = " ".join(lista)
    return lista_a_string



def main():
    cadena = input("Ingrese una cadena de caracteres:")
    print(ordenar_por_len(cadena))
main()