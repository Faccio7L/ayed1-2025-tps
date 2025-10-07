def sumar_numeros(num,num2):
    try:
        numero = int(num)
        num2 = int(num2)
    except Exception as e:
        print(f"Hubo un error por: {e}")
        return -1
    else:
        print(int(num) + int(num2))


def main():
    numero = input("Ingrese un numero:")
    numero_2 = input("Ingrese otro numero:")
    sumar_numeros(numero,numero_2)
main()