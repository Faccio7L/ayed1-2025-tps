class ErrorNumeroNegativo(Exception):
    "Indica que un numero es negativo."

def main()->None:
    """
    Se ingresa un numero, se verifica si tiene algun error, y se maneja con excepciones
    numero negativo se considera error.
    """
    numero = input("Ingrese un numero:")
    try:
        numero = int(numero)
        if numero < 0:
            raise ErrorNumeroNegativo("El numero debe ser positivo") #es decir, va a entrar en el except.
    except Exception as e:
        print(f"hubo un error por: {e}")
    

        
main()