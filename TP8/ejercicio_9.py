def main()->None:
    """
    se muestra la tabla del 1 al 12 de N numero ingresado por teclado.
    
    """
    n = int(input("Ingrese un numero:"))
    diccionario_por_comprension = {x:x*n for x in range(1,13)}
    print("Lista Por Comprension:")
    for clave, valor in diccionario_por_comprension.items(): #sin items solo veo valor!
        print(f"Clave: {clave} Value:{valor}")

main()