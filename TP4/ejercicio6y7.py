def eliminar_subcadena_a(cadena_principaL:str,desde:int,hasta:int)->str:
    """
    Elimina de elementos de una cadena con slice.
    pre: recibe la cadena, desde que string eliminar y cuantos.
    post: Retorna la nueva cadena.
    """
    primera_parte = cadena_principaL[:desde:1]
    segunda_parte = cadena_principaL[hasta::1]
    nueva_cadena = primera_parte + segunda_parte
    return nueva_cadena
def eliminar_subcadena_b(cadena_principal:str,desde,hasta):
    """
    Elimina de elementos de una cadena con listas por comprension
    pre: recibe la cadena, desde que string eliminar y cuantos.
    post: Retorna la nueva cadena.
    """
    
    nueva_cadena = [e for i, e in enumerate(cadena_principal) if i < desde or i >= hasta ]
    nueva_cadena = "".join(nueva_cadena)
    return nueva_cadena

def main()->None:
    """
    Genera una cadena y se indica desde donde y hasta donde se cortan.
    """
    cadena_principal = input("Ingrese un texto:")
    desde = int(input("A partir de que letra quiere eliminar?"))
    hasta = int(input("Cuantos caracteres?"))
    hasta += desde
    print(eliminar_subcadena_a(cadena_principal,desde,hasta))
    print(eliminar_subcadena_b(cadena_principal,desde,hasta))
assert(eliminar_subcadena_a("me llamo juan",1,2)) == "m llamo juan"
assert(eliminar_subcadena_b("me llamo juan",1,2)) == "m llamo juan"
assert(eliminar_subcadena_a("me llamo juan",10,22)) == "me llamo j"
assert(eliminar_subcadena_b("me llamo juan",1,2)) == "m llamo juan"


main()

