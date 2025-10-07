class ErrorNumeroNegativo(Exception):
    "Indica que un numero es negativo."

def main():
    numero = input("Ingrese un numero:")
    try:
        numero = int(numero)
        if numero < 0:
            raise ErrorNumeroNegativo("El numero debe ser positivo") #es decir, va a entrar en el except.
    except Exception as e:
        print(f"hubo un error por: {e}")
    
        

        
main()