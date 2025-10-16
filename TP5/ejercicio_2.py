def sumar_numeros(num:str,num2:str)->None:
    """
    Se castean y suman numeros, se manejan excepciones.
    pre:Recibe dos numeros en formato string.
    
    """
    try:
        numero = int(num)
        num2 = int(num2)
    except Exception as e:
        print(f"Hubo un error por: {e}")
        print (-1)
    else:
        print(int(num) + int(num2))


def main()->None:
    """
    Genera dos strings que deberian ser numeros. se inova la funcion sumar_numeros
    """
    numero = input("Ingrese un numero:")
    numero_2 = input("Ingrese otro numero:")
    sumar_numeros(numero,numero_2)
main()