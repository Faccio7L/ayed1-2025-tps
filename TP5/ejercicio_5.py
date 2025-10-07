import math as m
class NumeroNegativoError(Exception):
    "Error por numero negativo"

def cuadrado():
    numero = input("Ingrese un numero:")
    try:
        numero = int(numero)
    except Exception as e:
        numero = float(numero)
    finally:
        if numero >= 0:
            raiz_cuadrada = m.sqrt(numero)
            print(raiz_cuadrada)
        else:
            raise NumeroNegativoError("Error por Numero negativo")
cuadrado()