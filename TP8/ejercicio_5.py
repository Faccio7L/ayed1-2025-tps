def son_ortogonales(vectorial1:tuple,vectorial2:tuple) ->bool:
    """
    Verifica si dos vectoriales son ortogonales
    pre: dos tuplas compuestas por coordenadas de un vectorial
    """
    return vectorial1[0] * (vectorial2[0]) + vectorial1[1] * vectorial2[1] == 0


def main()->None:
    """
    Se ingresan dos vectoriales y se invoca una funcion para ver si son ortogonales.
    pre: no.
    post:no.
    """
    x_1 = int(input("Ingrese el valor de X del vectorial 1:"))
    y_1 = int(input("Ingrese el valor de y del vectorial 1:"))
    vectorial_1 = (x_1,y_1)

    x_2 = int(input("Ingrese el valor de X del vectorial 2:"))
    y_2 = int(input("Ingrese el valor de y del vectorial 2:"))
    vectorial_2 = (x_2,y_2)

    if son_ortogonales(vectorial_1,vectorial_2):
        print("Son ortogonales")
    else:
        print("No son ortogonales.")
main()

assert son_ortogonales((3,2),(2,3)) == True
assert son_ortogonales((42,2),(-3,99)) == False
