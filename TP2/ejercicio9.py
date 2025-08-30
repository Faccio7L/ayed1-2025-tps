def main()->None:
    """
    El usuario ingresa dos numeros, se valida mediante una lambda y se hace una lista
    por comprension de divisibles por 7 y NO divisibles por 5(de manera simultanea)
    pre:No recibe parametros
    """
    num_1 = int(input("Ingrese un numero inicial:"))
    num_2 = int(input("Ingrese un segundo numero(mayor al anterior:)"))
    verificacion = (lambda x,y: x < y)
    if verificacion(num_1,num_2):
        lista = [x for x in range(num_1,num_2 +1) if x % 7 == 0 and x % 5 != 0]
        print(f"la lista es: {lista}")
    else:
        print("Valores mal ingresados.")

main()