def filtrar_por_comprension(frase,n):
    frase_separada = frase.split() #lista por palabras
    filtrar = [palabra for palabra in frase_separada if len(palabra) >= n]
    return filtrar


def main():
    frase = input("Ingrese una frase:")
    n = int(input("Desee a partir de cuantos caracteres desea filtrar:"))
    print(filtrar_por_comprension(frase,n))
main()