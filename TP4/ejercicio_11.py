
def buscar_subcadena(cadena,subcadena):
    repeticiones_totales = 0
    while True:
        contador = 0
        for letra in subcadena: #una vez que itero cada letra de subcadena, comparo a ver si termine la subcadena o no, en caso de que si. Sigo buscando mas subcadenas,sino break!
            if letra in cadena:
                contador += 1
                cadena.remove(letra)
            else:
                break #si no se encuentra una letra, termina la busqueda!
        if contador == len(subcadena):
            repeticiones_totales += 1
        else:
            break

    return repeticiones_totales


def main():
    cadena_main = input("Ingrese una cadena:")
    subcadena = input("Ingrese una subcadena:")
    cadena_por_caracteres = list(cadena_main)
    subcadena_por_caracteres = list(subcadena)
    print(buscar_subcadena(cadena_por_caracteres,subcadena_por_caracteres))
main()